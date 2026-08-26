"""Valida estrutura, navegacao e artefatos do roadmap sem dependencias externas."""

from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import unquote

try:
    from gerar_indices import (
        FILE_MAP,
        ROOT_README,
        generate_map,
        generate_root,
        sessions as generated_sessions,
    )
except ModuleNotFoundError:  # Permite importar como scripts.validar_roadmap em testes.
    from scripts.gerar_indices import (
        FILE_MAP,
        ROOT_README,
        generate_map,
        generate_root,
        sessions as generated_sessions,
    )


ROOT = Path(__file__).resolve().parents[1]
MONTH_RE = re.compile(
    r"^(?P<complete>OK - )?(?P<order>\d{2}) - (?P<label>.+?) (?P<year>\d{4}) "
    r"\[(?P<done>\d+)-(?P<total>\d+)\]$"
)
DAY_RE = re.compile(r"^(?:OK - )?Dia (?P<day>\d{2})-(?P<month>\d{2}) - .+$")
DAY_CANDIDATE_RE = re.compile(r"^(?:OK - )?Dia")
LINK_RE = re.compile(r"!?\[[^\]]*\]\((?P<target><[^>]+>|[^)\s]+)(?:\s+['\"][^)]*['\"])?\)")

ROADMAP_START = date(2026, 8, 3)
ROADMAP_END = ROADMAP_START.replace(year=ROADMAP_START.year + 1) - timedelta(days=1)
LINKEDIN_POST_DATES = {
    "2026-09-03",
    "2026-09-15",
    "2026-09-24",
    "2026-10-06",
    "2026-10-19",
    "2026-10-26",
    "2026-11-09",
    "2026-11-19",
    "2026-12-01",
    "2026-12-08",
    "2026-12-22",
    "2026-12-31",
    "2027-01-11",
    "2027-01-19",
    "2027-02-04",
    "2027-02-16",
    "2027-03-01",
    "2027-03-08",
    "2027-03-16",
    "2027-03-25",
    "2027-04-06",
    "2027-04-22",
    "2027-04-26",
}
MONTH_NUMBERS = {
    "janeiro": 1,
    "fevereiro": 2,
    "marco": 3,
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubro": 10,
    "novembro": 11,
    "dezembro": 12,
}

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
LEGACY_COMPLETION_RE = re.compile(
    r"(?ms)^## Conclu[ií]do quando\s*\n(?P<body>.*?)(?=^##\s|\Z)"
)
FINALIZATION_RE = re.compile(
    r"(?ms)^## Finaliza[cç][aã]o\s*\n(?P<body>.*?)(?=^##\s|\Z)"
)
CHECKBOX_RE = re.compile(r"(?m)^\s*-\s+\[[ xX]\]")
PRIMARY_ARTIFACT_RE = re.compile(
    r"(?m)^\s*-\s+\*\*(?:Pasta/arquivo principal|Enunciado local|Arquivo principal):\*\*"
    r"(?P<body>.*)$"
)
CODE_SPAN_RE = re.compile(r"`([^`]+)`")
AI_PROJECT = ROOT / "projetos" / "assistente-suporte-ia"
CORPUS_DIR = AI_PROJECT / "data" / "corpus"
ACTIVITY_MANIFEST = ROOT / "00 - Recursos Compartilhados" / "manifesto-reorganizacao-2026.json"
ACTIVITY_DIR_RE = re.compile(
    r"^(?P<order>\d{2})-(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)$"
)
INTERNAL_ACTIVITY_ID_RE = re.compile(
    r"\b(?:E(?:0[1-9]|[1-9][0-9]|1[0-2][0-9]|13[0-8])|"
    r"N(?:0[1-9]|1[0-9]|2[0-9]))\b"
)
LEGACY_ACTIVITY_DIR_RE = re.compile(
    r"(?:^|-)(?:e\d{2,3}|n\d{2})(?:-|$)", re.IGNORECASE
)
LEGACY_GENERIC_DIR_NAMES = {
    "modulos",
    "01-exercicios",
    "02-pratica",
    "02-pratica-sem-consulta",
    "03-evidencias",
}
FORBIDDEN_FUTURE_HEADINGS = {
    "como estudar",
    "assuntos para pesquisar",
    "preparacao",
    "aprenda agora",
    "nucleo essencial",
    "nucleo obrigatorio",
    "pratica",
    "pratica obrigatoria",
    "trabalho obrigatorio",
    "entrega obrigatoria",
    "sequencia didatica",
    "atividades obrigatorias",
    "roteiro obrigatorio",
    "checklist do bloco",
    "checklist final",
    "criterio de aceite",
    "criterios de aceite",
    "resultado esperado",
    "integracao",
    "concluido quando",
}
CURSO_EM_VIDEO_CHALLENGES = {
    "Dia 24-08 - Break, sentinelas e tuplas": {
        "01-break-e-sentinelas": ("066", "069", "070"),
        "02-tuplas": ("072", "075", "077"),
    },
    "Dia 27-08 - Listas e matrizes": {
        "01-listas": ("078", "079", "081"),
        "02-listas-compostas-e-matrizes": ("084", "086"),
    },
    "Dia 31-08 - Dicionarios, sets e funcoes com parametros": {
        "01-dicionarios-e-set": ("090",),
        "02-funcoes-com-parametros": ("096", "098", "100"),
    },
    "Dia 01-09 - Retorno, modulos e pacotes": {
        "01-funcoes-com-retorno": ("104", "105"),
        "02-modulos-e-pacotes": ("107", "111"),
    },
    "Dia 03-09 - Excecoes e menu": {
        "01-excecoes-e-menu": ("113", "115a"),
    },
    "Dia 07-09 - Arquivos e projeto final de Python basico": {
        "01-arquivos-e-projeto-final": ("115b", "115c"),
    },
}

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


def validate_internal_activity_ids(errors: list[str]) -> None:
    """Impede que IDs de migracao vazem para materiais destinados ao aluno."""

    excluded = {ACTIVITY_MANIFEST.resolve(), FILE_MAP.resolve()}
    text_extensions = ACTIVITY_TEXT_EXTENSIONS | {".json", ".txt", ".yaml", ".yml"}
    for source in sorted(ROOT.rglob("*")):
        if (
            not source.is_file()
            or source.suffix.lower() not in text_extensions
            or source.resolve() in excluded
            or "scripts" in source.relative_to(ROOT).parts
            or ".git" in source.parts
            or ".ipynb_checkpoints" in source.parts
            or "__pycache__" in source.parts
            or any(part in {".venv", "venv", "env"} for part in source.parts)
        ):
            continue
        try:
            text = activity_text(source)
        except (OSError, UnicodeError, json.JSONDecodeError, TypeError):
            continue
        # Títulos públicos de cursos podem usar rótulos como ``S1 E10``
        # (temporada/episódio). Eles não são IDs internos da antiga estrutura
        # do roadmap e precisam permanecer literais para o aluno copiá-los.
        text_without_episode_labels = re.sub(
            r"\bS\d+\s+E\d+\b", "", text, flags=re.IGNORECASE
        )
        internal_ids = sorted(
            set(INTERNAL_ACTIVITY_ID_RE.findall(text_without_episode_labels))
        )
        if internal_ids:
            errors.append(
                "ID interno fora do manifesto: "
                f"{source.relative_to(ROOT)} -> {', '.join(internal_ids)}"
            )


def validate_project_markdown_checkboxes(errors: list[str]) -> None:
    """Centraliza o controle de progresso fora dos documentos de projeto."""

    projects = ROOT / "projetos"
    if not projects.is_dir():
        return
    for source in sorted(projects.rglob("*.md")):
        try:
            text = source.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        checkbox_count = len(CHECKBOX_RE.findall(text))
        if checkbox_count:
            errors.append(
                "Checkbox paralelo em documentacao de projeto: "
                f"{source.relative_to(ROOT)} ({checkbox_count})"
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


def month_number(label: str) -> int | None:
    normalized = "".join(
        character
        for character in unicodedata.normalize("NFKD", label)
        if not unicodedata.combining(character)
    ).casefold()
    return MONTH_NUMBERS.get(normalized)


def validate_generated_indices(errors: list[str]) -> None:
    """Confere os indices gerados sem alterar o repositorio."""
    try:
        items = generated_sessions()
        expected = {
            ROOT_README: generate_root(items),
            FILE_MAP: generate_map(items),
        }
    except (OSError, UnicodeError) as exc:
        errors.append(f"Nao foi possivel gerar indices em memoria: {exc}")
        return

    labels = {
        ROOT_README: "Agenda principal desatualizada",
        FILE_MAP: "Mapa de arquivos desatualizado",
    }
    for path, expected_text in expected.items():
        if not path.is_file():
            errors.append(f"Indice gerado ausente: {path.relative_to(ROOT)}")
            continue
        try:
            observed_text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Indice gerado invalido: {path.relative_to(ROOT)} ({exc})")
            continue
        if observed_text != expected_text:
            errors.append(
                f"{labels[path]}: {path.relative_to(ROOT)} "
                "(execute python scripts/gerar_indices.py)"
            )


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


def normalized_heading(value: str) -> str:
    """Normaliza um titulo para comparar secoes sem depender de acentos."""

    return "".join(
        character
        for character in unicodedata.normalize("NFKD", value)
        if not unicodedata.combining(character)
    ).casefold().strip()


def study_days_by_date(errors: list[str]) -> dict[str, Path]:
    """Indexa dias pela data, independentemente do prefixo mutavel ``OK -``."""

    observed: dict[str, Path] = {}
    for month in ROOT.iterdir():
        month_match = MONTH_RE.match(month.name) if month.is_dir() else None
        if not month_match:
            continue
        for day_dir in month.iterdir():
            day_match = DAY_RE.match(day_dir.name) if day_dir.is_dir() else None
            if not day_match:
                continue
            try:
                key = date(
                    int(month_match.group("year")),
                    int(day_match.group("month")),
                    int(day_match.group("day")),
                ).isoformat()
            except ValueError:
                continue
            previous = observed.get(key)
            if previous is not None:
                errors.append(
                    "Data de atividade duplicada: "
                    f"{key} ({previous.relative_to(ROOT)} e {day_dir.relative_to(ROOT)})"
                )
                continue
            observed[key] = day_dir
    return observed


def validate_activity_manifest(errors: list[str]) -> None:
    """Valida o inventario E/N sem expor IDs nos nomes das atividades."""

    try:
        manifest = json.loads(ACTIVITY_MANIFEST.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"Manifesto de atividades ausente: {ACTIVITY_MANIFEST.relative_to(ROOT)}")
        return
    except (json.JSONDecodeError, UnicodeError, OSError) as exc:
        errors.append(f"Manifesto de atividades invalido: {exc}")
        return

    if not isinstance(manifest, dict):
        errors.append("Manifesto de atividades deve ser um objeto JSON")
        return
    activities = manifest.get("activities")
    if not isinstance(activities, dict):
        errors.append("Manifesto de atividades sem o objeto 'activities'")
        return

    expected_legacy = {f"E{index:02d}" for index in range(1, 139)}
    expected_market = {f"N{index:02d}" for index in range(1, 30)}
    expected_ids = expected_legacy | expected_market
    observed_ids = {key for key in activities if isinstance(key, str)}
    if observed_ids != expected_ids:
        missing = sorted(expected_ids - observed_ids)
        extra = sorted(observed_ids - expected_ids)
        errors.append(
            f"Inventario E/N incorreto no manifesto: ausentes={missing}, extras={extra}"
        )
    if manifest.get("source_modules") != len(expected_legacy):
        errors.append("Contagem source_modules incorreta no manifesto")
    if manifest.get("added_modules") != len(expected_market):
        errors.append("Contagem added_modules incorreta no manifesto")
    if manifest.get("schema_version") != 2:
        errors.append("Versao do schema do manifesto deve ser 2")

    days = study_days_by_date(errors)
    if manifest.get("total_study_days") != len(days):
        errors.append(
            "Contagem total_study_days incorreta no manifesto "
            f"(esperado {len(days)})"
        )
    expected_local: dict[Path, str] = {}
    occupied_slots: dict[tuple[str, int], str] = {}
    checked_workspaces: set[Path] = set()
    manifest_study_dates: set[str] = set()

    for activity_id in sorted(expected_ids):
        entry = activities.get(activity_id)
        if not isinstance(entry, dict):
            errors.append(f"Entrada de atividade invalida no manifesto: {activity_id}")
            continue

        expected_origin = "legacy" if activity_id.startswith("E") else "market"
        if entry.get("origin") != expected_origin:
            errors.append(
                f"Origem incorreta no manifesto: {activity_id} "
                f"(esperado {expected_origin})"
            )
        if activity_id.startswith("E") and not isinstance(entry.get("legacy_path"), str):
            errors.append(f"Caminho legado ausente no manifesto: {activity_id}")

        raw_date = entry.get("study_date")
        order = entry.get("order")
        slug = entry.get("slug")
        title = entry.get("title")
        try:
            study_date = date.fromisoformat(raw_date) if isinstance(raw_date, str) else None
        except ValueError:
            study_date = None
        if study_date is None:
            errors.append(f"Data invalida no manifesto: {activity_id} -> {raw_date!r}")
            continue
        manifest_study_dates.add(study_date.isoformat())
        if type(order) is not int or not 1 <= order <= 99:
            errors.append(f"Ordem invalida no manifesto: {activity_id} -> {order!r}")
            continue
        if not isinstance(slug, str) or not re.fullmatch(
            r"[a-z0-9]+(?:-[a-z0-9]+)*", slug
        ):
            errors.append(f"Slug invalido no manifesto: {activity_id} -> {slug!r}")
            continue
        if not isinstance(title, str) or not title.strip():
            errors.append(f"Titulo ausente no manifesto: {activity_id}")
            continue

        slot = (study_date.isoformat(), order)
        previous_id = occupied_slots.get(slot)
        if previous_id is not None:
            errors.append(
                f"Posicao de atividade duplicada: {slot} ({previous_id} e {activity_id})"
            )
        else:
            occupied_slots[slot] = activity_id

        day_dir = days.get(study_date.isoformat())
        if day_dir is None:
            errors.append(
                f"Dia do manifesto ausente: {activity_id} -> {study_date.isoformat()}"
            )
            continue
        day_readme = day_dir / "README.md"
        try:
            day_text = day_readme.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            day_text = ""

        block_re = re.compile(
            rf"(?m)^### (?:Atividade {order}|Bloco {order}|Conteúdo e atividades)"
            rf"\s+[\u2014-]\s+{re.escape(title.strip())}\s*$"
        )
        if not block_re.search(day_text):
            errors.append(
                f"Bloco do manifesto ausente no README: {activity_id} -> "
                f"{day_readme.relative_to(ROOT)}"
            )

        workspace_value = entry.get("workspace")
        if workspace_value is not None:
            if not isinstance(workspace_value, str) or not workspace_value.strip():
                errors.append(f"Workspace invalido no manifesto: {activity_id}")
                continue
            workspace_relative = Path(workspace_value)
            workspace = (ROOT / workspace_relative).resolve()
            if (
                workspace_relative.is_absolute()
                or ".." in workspace_relative.parts
                or not workspace.is_relative_to(ROOT.resolve())
            ):
                errors.append(f"Workspace inseguro no manifesto: {activity_id}")
                continue
            if workspace not in checked_workspaces:
                checked_workspaces.add(workspace)
                if not workspace.is_dir():
                    errors.append(
                        f"Workspace central ausente: {workspace.relative_to(ROOT)}"
                    )
                elif not (workspace / "README.md").is_file():
                    errors.append(
                        f"README do workspace central ausente: {workspace.relative_to(ROOT)}"
                    )
            workspace_reference = workspace_relative.as_posix()
            if workspace_reference not in day_text:
                errors.append(
                    f"Workspace nao referenciado no README: {activity_id} -> "
                    f"{day_readme.relative_to(ROOT)}"
                )
            local_duplicate = (
                day_dir / "atividades" / f"{order:02d}-{slug}"
            )
            if local_duplicate.exists():
                errors.append(
                    "Atividade central duplicada na pasta do dia: "
                    f"{local_duplicate.relative_to(ROOT)}"
                )
            continue

        activity_dir = day_dir / "atividades" / f"{order:02d}-{slug}"
        resolved_activity = activity_dir.resolve()
        previous_activity_id = expected_local.get(resolved_activity)
        if previous_activity_id is not None:
            errors.append(
                f"Destino de atividade duplicado: {previous_activity_id} e {activity_id}"
            )
        else:
            expected_local[resolved_activity] = activity_id

        folder_reference = f"atividades/{activity_dir.name}/"
        if folder_reference not in day_text:
            errors.append(
                f"Atividade ausente no README diario: {activity_id} -> "
                f"{day_readme.relative_to(ROOT)}"
            )
        if not activity_dir.is_dir():
            errors.append(
                f"Pasta de atividade ausente: {activity_id} -> "
                f"{activity_dir.relative_to(ROOT)}"
            )
            continue
        if not any(path.is_file() for path in activity_dir.rglob("*")):
            errors.append(
                f"Atividade sem arquivo pratico: {activity_dir.relative_to(ROOT)}"
            )
        if (activity_dir / "README.md").exists():
            errors.append(
                f"README interno redundante: {(activity_dir / 'README.md').relative_to(ROOT)}"
            )

    if manifest_study_dates:
        first_session = min(manifest_study_dates)
        last_session = max(manifest_study_dates)
        if manifest.get("first_future_session") != first_session:
            errors.append(
                "first_future_session incorreta no manifesto "
                f"(esperado {first_session})"
            )
        if manifest.get("last_session") != last_session:
            errors.append(
                f"last_session incorreta no manifesto (esperado {last_session})"
            )
        if manifest.get("future_sessions_reorganized") != len(manifest_study_dates):
            errors.append(
                "future_sessions_reorganized incorreto no manifesto "
                f"(esperado {len(manifest_study_dates)})"
            )

    actual_local: set[Path] = set()
    for day_dir in days.values():
        if not day_dir.name.startswith("OK - "):
            for directory in day_dir.rglob("*"):
                if directory.is_dir() and directory.name in LEGACY_GENERIC_DIR_NAMES:
                    errors.append(
                        f"Pasta generica antiga: {directory.relative_to(ROOT)}"
                    )

        activities_dir = day_dir / "atividades"
        if not activities_dir.is_dir():
            continue
        for loose_file in activities_dir.iterdir():
            if loose_file.is_file():
                errors.append(
                    f"Arquivo solto na raiz de atividades: {loose_file.relative_to(ROOT)}"
                )
        for activity_dir in activities_dir.iterdir():
            if not activity_dir.is_dir():
                continue
            actual_local.add(activity_dir.resolve())
            if LEGACY_ACTIVITY_DIR_RE.search(activity_dir.name):
                errors.append(
                    f"Nome de atividade contem ID interno: {activity_dir.relative_to(ROOT)}"
                )
            if not ACTIVITY_DIR_RE.fullmatch(activity_dir.name):
                errors.append(
                    f"Nome de atividade invalido: {activity_dir.relative_to(ROOT)}"
                )

    for orphan in sorted(actual_local - set(expected_local), key=str):
        errors.append(f"Atividade orfa: {orphan.relative_to(ROOT)}")


def validate_portfolio_projects_and_credentials(errors: list[str]) -> None:
    """Protege apenas evidencias reais de portfolio e credenciais."""

    project_roots = [
        ROOT / "projetos" / "telecom-customer-intelligence",
        ROOT / "projetos" / "energy-forecastops",
        ROOT / "projetos" / "entity-matching-lab",
        ROOT / "projetos" / "assistente-suporte-ia" / "extensao-visao-computacional",
        ROOT / "projetos" / "telecom-customer-intelligence" / "entrega-tcc",
    ]
    common = [
        Path("README.md"),
        Path("README.en.md"),
        Path("data_card.md"),
        Path("backlog.md"),
        Path("docs") / "presentation-en.md",
    ]
    for project in project_roots:
        for relative in common:
            path = project / relative
            if not path.is_file():
                errors.append(
                    f"Artefato de projeto de portfolio ausente: {path.relative_to(ROOT)}"
                )

    for project in project_roots[:-1]:
        for folder in ("src", "tests", "data"):
            path = project / folder
            if not path.is_dir():
                errors.append(
                    f"Diretorio de projeto de portfolio ausente: {path.relative_to(ROOT)}"
                )

    credential_root = ROOT / "00 - Recursos Compartilhados"
    credential_files = [
        credential_root / "credenciais-gratuitas-e-simulados.md",
        credential_root / "simulados-credenciais" / "simulado-microsoft-power-bi.md",
        credential_root / "simulados-credenciais" / "simulado-dbt-fundamentals.md",
        credential_root / "simulados-credenciais" / "simulado-google-skills-bigquery.md",
        credential_root / "simulados-credenciais" / "simulado-databricks-fundamentals.md",
        credential_root / "simulados-credenciais" / "simulado-ef-set.md",
        credential_root / "simulados-credenciais" / "roteiros-listening-ef-set.md",
        credential_root / "simulados-credenciais" / "registro-de-tentativas.md",
    ]
    for path in credential_files:
        if not path.is_file():
            errors.append(
                f"Preparacao de credencial ausente: {path.relative_to(ROOT)}"
            )


def validate_future_readmes_and_video_challenges(errors: list[str]) -> None:
    """Protege o formato limpo dos dias futuros e os starters de Python."""

    for month in ROOT.iterdir():
        if not month.is_dir() or not MONTH_RE.match(month.name):
            continue
        for day in month.iterdir():
            if not day.is_dir() or not DAY_RE.match(day.name):
                continue
            day_readme = day / "README.md"
            if not day_readme.is_file():
                continue
            if day.name.startswith("OK - "):
                continue
            try:
                text = day_readme.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                continue

            activities_headings = len(
                re.findall(r"(?m)^## Atividades do dia\s*$", text)
            )
            if activities_headings != 1:
                errors.append(
                    "README futuro deve ter uma secao 'Atividades do dia': "
                    f"{day_readme.relative_to(ROOT)} ({activities_headings})"
                )

            finalizations = list(FINALIZATION_RE.finditer(text))
            if len(finalizations) != 1:
                errors.append(
                    "README futuro deve ter uma secao 'Finalizacao': "
                    f"{day_readme.relative_to(ROOT)} ({len(finalizations)})"
                )
            else:
                completion_count = len(
                    CHECKBOX_RE.findall(finalizations[0].group("body"))
                )
                if completion_count != 1:
                    errors.append(
                        "Finalizacao deve ter um unico checkbox: "
                        f"{day_readme.relative_to(ROOT)} ({completion_count})"
                    )

            h2_titles = re.findall(r"(?m)^## ([^#].*?)\s*$", text)
            if h2_titles and normalized_heading(h2_titles[-1]) != "finalizacao":
                errors.append(
                    f"Finalizacao deve ser a ultima secao: {day_readme.relative_to(ROOT)}"
                )
            for heading in re.findall(r"(?m)^#{2,6} ([^#].*?)\s*$", text):
                clean_heading = re.sub(r"\s+#+$", "", heading).strip()
                if normalized_heading(clean_heading) in FORBIDDEN_FUTURE_HEADINGS:
                    errors.append(
                        "Secao antiga ou redundante: "
                        f"{day_readme.relative_to(ROOT)} -> {clean_heading}"
                    )

            activities_dir = day / "atividades"
            if activities_dir.is_dir():
                for nested_markdown in activities_dir.rglob("*.md"):
                    try:
                        nested_text = nested_markdown.read_text(encoding="utf-8")
                    except (OSError, UnicodeError):
                        continue
                    nested_checkboxes = len(CHECKBOX_RE.findall(nested_text))
                    if nested_checkboxes:
                        errors.append(
                            "Checkbox deve existir somente no README diario: "
                            f"{nested_markdown.relative_to(ROOT)} "
                            f"({nested_checkboxes})"
                        )
                    for nested_heading in re.findall(
                        r"(?m)^#{1,6} ([^#].*?)\s*$", nested_text
                    ):
                        clean_nested_heading = re.sub(
                            r"\s+#+$", "", nested_heading
                        ).strip()
                        normalized_nested_heading = normalized_heading(
                            clean_nested_heading
                        )
                        if (
                            normalized_nested_heading == "pratica obrigatoria"
                            or normalized_nested_heading.startswith(
                                "pratica obrigatoria "
                            )
                            or "nucleo essencial" in normalized_nested_heading
                        ):
                            errors.append(
                                "Heading pedagogico antigo em atividade: "
                                f"{nested_markdown.relative_to(ROOT)} -> "
                                f"{clean_nested_heading}"
                            )
                    if re.search(
                        r"n[aã]o faz parte do n[uú]cleo obrigat[oó]rio",
                        nested_text,
                        re.IGNORECASE,
                    ):
                        errors.append(
                            "Frase pedagogica antiga em atividade: "
                            f"{nested_markdown.relative_to(ROOT)} -> "
                            "nao faz parte do nucleo obrigatorio"
                        )

    month_dirs = [
        path
        for path in ROOT.iterdir()
        if path.is_dir() and MONTH_RE.match(path.name)
    ]
    for day_name, activities in CURSO_EM_VIDEO_CHALLENGES.items():
        candidates = tuple(
            candidate
            for month in month_dirs
            for candidate in (month / day_name, month / f"OK - {day_name}")
        )
        day = next((candidate for candidate in candidates if candidate.is_dir()), ROOT / day_name)
        readme = day / "README.md"
        text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
        for activity_name, numbers in activities.items():
            for number in numbers:
                relative = f"atividades/{activity_name}/DESAFIO{number}.py"
                challenge = day / relative
                if not challenge.is_file():
                    errors.append(
                        f"Starter do Curso em Video ausente: {challenge.relative_to(ROOT)}"
                    )
                if relative not in text:
                    errors.append(
                        "Link do desafio ausente no README diario: "
                        f"{readme.relative_to(ROOT)} -> {relative}"
                    )


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
        child_dirs = [path for path in month.iterdir() if path.is_dir()]
        for child in child_dirs:
            if DAY_CANDIDATE_RE.match(child.name) and not DAY_RE.match(child.name):
                errors.append(
                    f"Diretorio de dia malformado: {child.relative_to(ROOT)}"
                )

        month_match = MONTH_RE.match(month.name)
        if not month_match:
            errors.append(f"Contador mensal ausente ou invalido: {month.name}")
            continue

        expected_month = month_number(month_match.group("label"))
        if expected_month is None:
            errors.append(
                f"Nome de mes desconhecido: {month.name} "
                f"({month_match.group('label')})"
            )

        day_dirs = [
            path for path in child_dirs if DAY_RE.match(path.name)
        ]
        for day_dir in day_dirs:
            day_match = DAY_RE.match(day_dir.name)
            assert day_match
            observed_month = int(day_match.group("month"))
            if expected_month is not None and observed_month != expected_month:
                errors.append(
                    "Data diaria incoerente com a pasta mensal: "
                    f"{day_dir.relative_to(ROOT)} "
                    f"(mes esperado {expected_month:02d}, observado {observed_month:02d}; "
                    f"ano {month_match.group('year')})"
                )

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
            session_date = date.fromisoformat(date_key)
        except ValueError:
            errors.append(f"Data invalida: {readme.parent.relative_to(ROOT)}")
        else:
            if not ROADMAP_START <= session_date <= ROADMAP_END:
                errors.append(
                    "Data fora do limite de um ano: "
                    f"{readme.parent.relative_to(ROOT)} "
                    f"({ROADMAP_START.isoformat()} a {ROADMAP_END.isoformat()})"
                )
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

        if readme.parent.name.startswith("OK - "):
            completion = LEGACY_COMPLETION_RE.search(text)
            completion_count = (
                len(CHECKBOX_RE.findall(completion.group("body")))
                if completion
                else 0
            )
            if completion_count != 3:
                errors.append(
                    "Criterio legado de conclusao deve ter tres provas: "
                    f"{readme.relative_to(ROOT)} ({completion_count})"
                )
        if date_key in LINKEDIN_POST_DATES:
            heading = "## Publicação da semana no LinkedIn"
            if text.count(heading) != 1:
                errors.append(
                    "Publicacao semanal do LinkedIn ausente ou duplicada: "
                    f"{readme.relative_to(ROOT)}"
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
    validate_internal_activity_ids(errors)
    validate_project_markdown_checkboxes(errors)
    validate_ai_project(errors)
    validate_future_readmes_and_video_challenges(errors)
    validate_activity_manifest(errors)
    validate_portfolio_projects_and_credentials(errors)
    validate_generated_indices(errors)

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
