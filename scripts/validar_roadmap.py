"""Valida estrutura, navegacao e artefatos do roadmap sem dependencias externas."""

from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MONTH_RE = re.compile(
    r"^(?P<complete>OK - )?(?P<order>\d{2}) - .+ (?P<year>\d{4}) "
    r"\[(?P<done>\d+)-(?P<total>\d+)\]$"
)
DAY_RE = re.compile(r"^(?:OK - )?Dia (?P<day>\d{2})-(?P<month>\d{2}) - .+$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\((?P<target><[^>]+>|[^)\s]+)(?:\s+['\"][^)]*['\"])?\)")

# A agenda vive no README raiz. Uma sessao diaria nunca depende de reabrir outra.
FORBIDDEN_DAILY_PATTERNS = {
    "calendario antigo": re.compile(r"calend[aá]rio-base", re.IGNORECASE),
    "ordem paralela": re.compile(r"ordem de estudo", re.IGNORECASE),
    "instrucao para voltar": re.compile(
        r"\b(?:volte|retorne|retome|voltar|retornar|retomar)\b.{0,40}"
        r"\b(?:Dia\s+#?\d+|README|pasta|sess[aã]o|encontro|exerc[ií]cio\s+#?\d+)",
        re.IGNORECASE,
    ),
    "referencia a outro dia": re.compile(r"\bDia\s+#?\d+\b", re.IGNORECASE),
    "link interno do VS Code": re.compile(r"file\+\.vscode-resource", re.IGNORECASE),
}
FORBIDDEN_README_PATTERNS = {
    "boilerplate adaptativo": re.compile(r"(?:Rota|Escopo) adaptativ[oa]", re.IGNORECASE),
    "metanavegacao diaria": re.compile(
        r"README (?:na raiz|do dia|di[aá]rio)|n[aã]o a data da pasta", re.IGNORECASE
    ),
    "link interno do VS Code": re.compile(r"file\+\.vscode-resource", re.IGNORECASE),
}
COMPLETION_RE = re.compile(
    r"(?ms)^## Conclu[ií]do quando\s*\n(?P<body>.*?)(?=^##\s|\Z)"
)
CHECKBOX_RE = re.compile(r"(?m)^\s*-\s+\[[ xX]\]")
PRIMARY_ARTIFACT_RE = re.compile(
    r"(?m)^\s*-\s+\*\*(?:Pasta/arquivo principal|Enunciado local|Arquivo principal):\*\*"
    r"(?P<body>.*)$"
)
CODE_SPAN_RE = re.compile(r"`([^`]+)`")
AI_PROJECT = ROOT / "projetos" / "assistente-suporte-ia"
CORPUS_DIR = AI_PROJECT / "data" / "corpus"

# Restringe a regra a rotulos de atividade. Assim, expressoes tecnicas como
# "dependencia opcional" continuam permitidas quando nao nomeiam uma tarefa.
ACTIVITY_TEXT_EXTENSIONS = {".md", ".py", ".sql", ".ipynb"}
OPTIONAL_ACTIVITY_MARKER_RE = re.compile(
    r"(?im)^\s*(?:"
    r"(?:\#{1,6}|//+|--|/\*+|\*+)\s*|"
    r"[-+*]\s+(?:\[[ xX]\]\s*)?|"
    r">+\s*(?:\[[^\]]+\]\s*)?"
    r")\*{0,2}(?:"
    r"refor[cç]o\s+direcionado|"
    r"desafios?\s+opciona(?:l|is)|"
    r"pr[aá]ticas?\s+opciona(?:l|is)|"
    r"apresenta[cç](?:[aã]o|[oõ]es)\s+opciona(?:l|is)|"
    r"rotas?\s+alternativas?|"
    r"(?:atividades?|exerc[ií]cios?|amplia[cç](?:[aã]o|[oõ]es)|registros?|roteiros?|"
    r"relat[oó]rios?|retrospectivas?|resumos?\s+executivos?)"
    r"[^\n]{0,40}\s+opciona(?:l|is)"
    r")\b"
)


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def activity_text_files() -> list[Path]:
    """Lista textos de estudo nos meses e no projeto de IA."""
    roots = [
        path
        for path in ROOT.iterdir()
        if path.is_dir() and MONTH_RE.match(path.name)
    ]
    if AI_PROJECT.is_dir():
        roots.append(AI_PROJECT)

    files: set[Path] = set()
    for root in roots:
        files.update(
            path
            for path in root.rglob("*")
            if path.is_file()
            and path.suffix.lower() in ACTIVITY_TEXT_EXTENSIONS
            and ".git" not in path.parts
            and ".ipynb_checkpoints" not in path.parts
            and "__pycache__" not in path.parts
        )
    return sorted(files)


def activity_text(source: Path) -> str:
    """Extrai texto visivel, inclusive das celulas de notebooks."""
    if source.suffix.lower() != ".ipynb":
        return source.read_text(encoding="utf-8-sig")

    notebook = json.loads(source.read_text(encoding="utf-8-sig"))
    chunks: list[str] = []
    for cell in notebook.get("cells", []):
        raw_source = cell.get("source", []) if isinstance(cell, dict) else []
        if isinstance(raw_source, str):
            chunks.append(raw_source)
        elif isinstance(raw_source, list):
            chunks.extend(part for part in raw_source if isinstance(part, str))
    return "".join(chunks)


def validate_optional_activity_markers(errors: list[str]) -> None:
    for source in activity_text_files():
        try:
            text = activity_text(source)
        except (OSError, UnicodeError, json.JSONDecodeError, TypeError) as exc:
            # Validadores de sintaxe tambem registram o problema; esta mensagem
            # preserva o contexto caso a leitura falhe antes da busca de rotulos.
            errors.append(
                f"Texto de atividade invalido: {source.relative_to(ROOT)} ({exc})"
            )
            continue
        for match in OPTIONAL_ACTIVITY_MARKER_RE.finditer(text):
            marker = " ".join(match.group(0).split())
            errors.append(
                "Marcador de atividade opcional: "
                f"{source.relative_to(ROOT)} -> {marker}"
            )


def daily_readmes() -> list[Path]:
    result: list[Path] = []
    for month in ROOT.iterdir():
        if not month.is_dir() or not MONTH_RE.match(month.name):
            continue
        for day in month.iterdir():
            if day.is_dir() and DAY_RE.match(day.name):
                result.append(day / "README.md")
    return sorted(result)


def local_link_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target[1:-1] if raw_target.startswith("<") else raw_target
    target = unquote(target.split("#", 1)[0]).strip()
    if not target or target.startswith(("http://", "https://", "mailto:")):
        return None
    return (source.parent / target).resolve()


def validate_ai_project(errors: list[str]) -> None:
    required = [
        AI_PROJECT / "README.md",
        AI_PROJECT / "pyproject.toml",
        AI_PROJECT / "requirements.txt",
        AI_PROJECT / "governanca" / "gate-fundamentos.md",
        AI_PROJECT / "governanca" / "reforco-fundamentos.md",
        AI_PROJECT / "data" / "chamados_teste.json",
        AI_PROJECT / "data" / "perguntas_avaliacao.csv",
        AI_PROJECT / "config" / "configuracao.json",
        AI_PROJECT / "outputs" / "avaliacao" / "avaliacao_rag.csv",
        AI_PROJECT / "src" / "assistente_suporte_ia" / "__init__.py",
        AI_PROJECT / "src" / "assistente_suporte_ia" / "assistente.py",
        AI_PROJECT / "src" / "assistente_suporte_ia" / "avaliar_rag.py",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"Artefato do projeto de IA ausente: {path.relative_to(ROOT)}")

    manifest = CORPUS_DIR / "corpus_manifest.csv"
    expected_manifest = [
        "doc_id",
        "arquivo",
        "titulo",
        "origem",
        "licenca",
        "versao",
        "sha256",
    ]
    if manifest.is_file():
        try:
            with manifest.open(encoding="utf-8-sig", newline="") as source:
                reader = csv.DictReader(source)
                rows = list(reader)
                if reader.fieldnames != expected_manifest:
                    errors.append("Schema invalido: projetos/assistente-suporte-ia/data/corpus/corpus_manifest.csv")
                if len(rows) != 15:
                    errors.append(f"Manifesto de corpus deve ter 15 linhas ({len(rows)})")
                if len({row.get("doc_id") for row in rows}) != len(rows):
                    errors.append("doc_id duplicado no manifesto do corpus")
                corpus_root = CORPUS_DIR.resolve()
                for row in rows:
                    document = (CORPUS_DIR / (row.get("arquivo") or "")).resolve()
                    if not document.is_relative_to(corpus_root) or not document.is_file():
                        errors.append(f"Documento do manifesto ausente ou inseguro: {row.get('arquivo')}")
                        continue
                    observed = hashlib.sha256(document.read_bytes()).hexdigest()
                    if observed != row.get("sha256"):
                        errors.append(f"SHA-256 divergente no corpus: {row.get('arquivo')}")
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"Manifesto de corpus invalido: {exc}")
    else:
        errors.append("Manifesto do corpus ausente")

    chamados = AI_PROJECT / "data" / "chamados_teste.json"
    if chamados.is_file():
        try:
            cases = json.loads(chamados.read_text(encoding="utf-8"))
            groups = Counter(case.get("grupo_teste") for case in cases if isinstance(case, dict))
            if len(cases) != 20 or groups != Counter({"claro": 10, "ambiguo": 5, "fora_do_dominio": 5}):
                errors.append("chamados_teste.json deve conter 10 casos claros, 5 ambiguos e 5 fora do dominio")
        except (json.JSONDecodeError, UnicodeError, OSError, TypeError) as exc:
            errors.append(f"chamados_teste.json invalido: {exc}")

    csv_contracts = {
        AI_PROJECT / "data" / "perguntas_avaliacao.csv": [
            "pergunta_id", "pergunta", "resposta_esperada", "doc_ids_esperados", "tipo", "deve_recusar"
        ],
        AI_PROJECT / "outputs" / "avaliacao" / "avaliacao_rag.csv": [
            "pergunta_id", "docs_esperados", "docs_obtidos", "resposta", "fontes",
            "precision_at_k", "recall_at_k", "fundamentada", "recusou", "latencia_ms", "status"
        ],
    }
    for path, expected in csv_contracts.items():
        if not path.is_file():
            continue
        try:
            with path.open(encoding="utf-8-sig", newline="") as source:
                header = next(csv.reader(source), [])
            if header != expected:
                errors.append(f"Schema invalido: {path.relative_to(ROOT)}")
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"CSV invalido: {path.relative_to(ROOT)} ({exc})")

    config = AI_PROJECT / "config" / "configuracao.json"
    if config.is_file():
        try:
            json.loads(config.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeError, OSError) as exc:
            errors.append(f"Configuracao do projeto de IA invalida: {exc}")


def main() -> int:
    errors: list[str] = []
    dates: list[str] = []
    readmes = daily_readmes()

    month_candidates = sorted(
        path
        for path in ROOT.iterdir()
        if path.is_dir() and re.match(r"^(?:OK - )?\d{2} - ", path.name)
        and not re.match(r"^(?:OK - )?00 - ", path.name)
    )
    for month in month_candidates:
        month_match = MONTH_RE.match(month.name)
        if not month_match:
            errors.append(f"Contador mensal ausente ou invalido: {month.name}")
            continue
        day_dirs = [
            path for path in month.iterdir()
            if path.is_dir() and DAY_RE.match(path.name)
        ]
        actual_done = sum(path.name.startswith("OK - ") for path in day_dirs)
        stated_done = int(month_match.group("done"))
        stated_total = int(month_match.group("total"))
        if (stated_done, stated_total) != (actual_done, len(day_dirs)):
            errors.append(
                f"Contador mensal incorreto: {month.name} "
                f"(esperado [{actual_done}-{len(day_dirs)}])"
            )
        marked_complete = bool(month_match.group("complete"))
        actually_complete = bool(day_dirs) and actual_done == len(day_dirs)
        if marked_complete != actually_complete:
            expected_prefix = "OK - " if actually_complete else "sem prefixo OK - "
            errors.append(f"Status mensal incorreto: {month.name} ({expected_prefix})")

    for readme in readmes:
        day_match = DAY_RE.match(readme.parent.name)
        month_match = MONTH_RE.match(readme.parent.parent.name)
        assert day_match and month_match
        date_key = (
            f"{month_match.group('year')}-"
            f"{day_match.group('month')}-{day_match.group('day')}"
        )
        dates.append(date_key)
        try:
            date.fromisoformat(date_key)
        except ValueError:
            errors.append(f"Data invalida: {readme.parent.relative_to(ROOT)}")
        if not readme.is_file():
            errors.append(f"README ausente: {readme.relative_to(ROOT)}")
            continue
        try:
            text = readme.read_text(encoding="utf-8")
        except UnicodeError as exc:
            errors.append(f"README nao esta em UTF-8: {readme.relative_to(ROOT)} ({exc})")
            continue
        headings = re.findall(r"(?m)^# [^#].*$", text)
        if len(headings) != 1:
            errors.append(
                f"Esperado um unico H1: {readme.relative_to(ROOT)} ({len(headings)})"
            )
        elif re.search(r"\bDia\s+#?\d+\b|\b\d{2}/\d{2}/20\d{2}\b", headings[0]):
            errors.append(f"Titulo diario com numero/data: {readme.relative_to(ROOT)}")

        completion = COMPLETION_RE.search(text)
        completion_count = len(CHECKBOX_RE.findall(completion.group("body"))) if completion else 0
        if completion_count != 3:
            errors.append(
                "Criterio de conclusao deve ter tres provas: "
                f"{readme.relative_to(ROOT)} ({completion_count})"
            )
        for artifact_line in PRIMARY_ARTIFACT_RE.finditer(text):
            for raw_path in CODE_SPAN_RE.findall(artifact_line.group("body")):
                local_candidate = (readme.parent / raw_path).resolve()
                root_candidate = (ROOT / raw_path).resolve()
                if not local_candidate.exists() and not root_candidate.exists():
                    errors.append(
                        "Artefato principal ausente: "
                        f"{readme.relative_to(ROOT)} -> {raw_path}"
                    )
        for label, pattern in FORBIDDEN_DAILY_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{label}: {readme.relative_to(ROOT)}")

    for duplicated_date, count in Counter(dates).items():
        if count > 1:
            errors.append(f"Data duplicada: {duplicated_date} ({count} pastas)")

    markdown = markdown_files()
    for source in markdown:
        try:
            text = source.read_text(encoding="utf-8")
        except UnicodeError as exc:
            errors.append(f"Markdown nao esta em UTF-8: {source.relative_to(ROOT)} ({exc})")
            continue
        if source.name == "README.md":
            for label, pattern in FORBIDDEN_README_PATTERNS.items():
                if pattern.search(text):
                    errors.append(f"{label}: {source.relative_to(ROOT)}")
        for match in LINK_RE.finditer(text):
            target = local_link_target(source, match.group("target"))
            if target is not None and not target.exists():
                errors.append(
                    "Link local quebrado: "
                    f"{source.relative_to(ROOT)} -> {match.group('target')}"
                )

    python_files = sorted(
        path
        for path in ROOT.rglob("*.py")
        if ".git" not in path.parts
        and "__pycache__" not in path.parts
        and not any(part in {".venv", "venv", "env"} for part in path.parts)
    )
    for source in python_files:
        try:
            ast.parse(source.read_text(encoding="utf-8-sig"), filename=str(source))
        except (SyntaxError, UnicodeError) as exc:
            errors.append(f"Python invalido: {source.relative_to(ROOT)} ({exc})")

    notebooks = sorted(
        path
        for path in ROOT.rglob("*.ipynb")
        if ".git" not in path.parts and ".ipynb_checkpoints" not in path.parts
    )
    for source in notebooks:
        try:
            json.loads(source.read_text(encoding="utf-8-sig"))
        except (json.JSONDecodeError, UnicodeError) as exc:
            errors.append(f"Notebook invalido: {source.relative_to(ROOT)} ({exc})")

    validate_optional_activity_markers(errors)
    validate_ai_project(errors)

    if errors:
        print(f"FALHOU: {len(errors)} problema(s).")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"OK: {len(readmes)} sessoes, {len(markdown)} Markdown, "
        f"{len(python_files)} arquivos Python e {len(notebooks)} notebooks; "
        "datas, estrutura, sintaxe, links e navegacao validos."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
