"""Regenera a agenda principal e o mapa de arquivos a partir das pastas datadas."""

from __future__ import annotations

import os
import re
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROOT_README = ROOT / "README.md"
FILE_MAP = ROOT / "00 - Recursos Compartilhados" / "mapa-de-arquivos.md"
MONTH_RE = re.compile(
    r"^(?:OK - )?(?P<order>\d{2}) - (?P<label>.+?) (?P<year>\d{4})(?: \[\d+-\d+\])?$"
)
DAY_RE = re.compile(r"^(?:OK - )?Dia (?P<day>\d{2})-(?P<month>\d{2}) - (?P<topic>.+)$")
MONTH_LABELS = {"Marco": "Março"}


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def map_relative(path: Path) -> str:
    return f"../{relative(path)}"


def title_for(readme: Path, fallback: str) -> str:
    if readme.is_file():
        match = re.search(r"(?m)^# ([^#].+)$", readme.read_text(encoding="utf-8"))
        if match:
            return match.group(1).strip()
    return fallback


def sessions() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for month_dir in sorted(ROOT.iterdir()):
        month_match = MONTH_RE.match(month_dir.name) if month_dir.is_dir() else None
        if not month_match or month_match.group("order") == "00":
            continue
        for day_dir in month_dir.iterdir():
            day_match = DAY_RE.match(day_dir.name) if day_dir.is_dir() else None
            if not day_match:
                continue
            readme = day_dir / "README.md"
            result.append(
                {
                    "month_order": int(month_match.group("order")),
                    "month_label": (
                        f"{MONTH_LABELS.get(month_match.group('label'), month_match.group('label'))} "
                        f"{month_match.group('year')}"
                    ),
                    "year": int(month_match.group("year")),
                    "month": int(day_match.group("month")),
                    "day": int(day_match.group("day")),
                    "dir": day_dir,
                    "readme": readme,
                    "title": title_for(readme, day_match.group("topic")),
                }
            )
    return sorted(result, key=lambda item: (item["year"], item["month"], item["day"]))


def generate_root(items: list[dict[str, object]]) -> str:
    lines = [
        "# Roadmap Data Science",
        "",
        f"Trilha prática com **{len(items)} sessões**, conteúdo gratuito, exercícios e projetos. "
        "Cada pasta datada traz as instruções e os caminhos necessários: conclua a sessão, marque aqui e siga o "
        "primeiro item ainda aberto.",
        "",
        "- [Plano e método de estudo](PLANO-DE-ESTUDOS.md)",
        "- [Curso em Vídeo — cobertura de Python](<00 - Recursos Compartilhados/trilha-curso-em-video-python.md>)",
        "- [Cursos gratuitos e lacunas](<00 - Recursos Compartilhados/cursos-complementares-selecionados.md>)",
        "- [Dados e recursos compartilhados](<00 - Recursos Compartilhados/README.md>)",
        "- [LinkedIn e evidências](<00 - Recursos Compartilhados/linkedin-e-evidencias.md>)",
        "- [LinkedIn — perfil atual](<00 - Recursos Compartilhados/linkedin-perfil-atual.md>)",
        "- [Vagas para análise do roadmap](<00 - Recursos Compartilhados/VAGAS.md>)",
        "- [Análise das vagas e decisões do currículo](<00 - Recursos Compartilhados/analise-vagas-e-decisoes.md>)",
        "- [Projetos compartilhados](projetos/README.md)",
        "- [Decisões de Carlos](<00 - Recursos Compartilhados/PERGUNTAS-PARA-CARLOS.md>)",
        "- [Mapa de arquivos](<00 - Recursos Compartilhados/mapa-de-arquivos.md>)",
        "",
        "## Como usar",
        "",
        "1. Abra o primeiro item não marcado na agenda abaixo.",
        "2. Faça somente o conteúdo daquela pasta e tente exercícios antes de ver a resolução.",
        "3. Marque a sessão quando o artefato executar, você conseguir alterá-lo e explicar a lógica.",
        "4. Não reabra dias concluídos; qualquer revisão necessária aparece em uma nova atividade.",
        "",
        "Para conferir a integridade do projeto:",
        "",
        "```powershell",
        "python scripts/validar_roadmap.py",
        "```",
        "",
        "## Agenda e progresso",
        "",
    ]

    current_month: int | None = None
    for item in items:
        month_order = int(item["month_order"])
        if month_order != current_month:
            if current_month is not None:
                lines.append("")
            lines.extend([f"### {item['month_label']}", ""])
            current_month = month_order
        link = relative(item["readme"])
        mark = "x" if item["dir"].name.startswith("OK - ") else " "
        date = f"{item['day']:02d}/{item['month']:02d}/{item['year']}"
        lines.append(f"- [{mark}] **{date}** — [{item['title']}](<{link}>)")
    lines.append("")
    return "\n".join(lines)


def generate_map(items: list[dict[str, object]]) -> str:
    lines = [
        "# Mapa de arquivos",
        "",
        "> Gerado por `python scripts/gerar_indices.py`. Edite os arquivos de origem, não esta lista.",
        "",
        "## Sessões",
        "",
    ]
    current_month: int | None = None
    for item in items:
        month_order = int(item["month_order"])
        if month_order != current_month:
            lines.extend([f"### {item['month_label']}", ""])
            current_month = month_order
        date = f"{item['day']:02d}/{item['month']:02d}/{item['year']}"
        readme_link = map_relative(item["readme"])
        lines.append(f"#### {date} — [{item['title']}](<{readme_link}>)")
        lines.append("")
        day_dir = item["dir"]
        assets = sorted(
            path
            for path in day_dir.rglob("*")
            if path.is_file()
            and path.name != "README.md"
            and "__pycache__" not in path.parts
            and ".ipynb_checkpoints" not in path.parts
        )
        if assets:
            for asset in assets:
                lines.append(
                    f"- [{asset.relative_to(day_dir).as_posix()}](<{map_relative(asset)}>)"
                )
        else:
            lines.append("- Nenhum arquivo adicional.")
        lines.append("")

    lines.extend(["## Recursos compartilhados", ""])
    shared_roots = [ROOT / "dados", ROOT / "projetos"]
    for shared_root in shared_roots:
        lines.extend([f"### {shared_root.name}", ""])
        for path in sorted(shared_root.rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                lines.append(
                    f"- [{path.relative_to(shared_root).as_posix()}](<{map_relative(path)}>)"
                )
        lines.append("")
    return "\n".join(lines)


def atomic_write(path: Path, text: str) -> None:
    """Substitui um indice completo sem expor um arquivo parcialmente gravado."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as target:
            target.write(text)
            target.flush()
            os.fsync(target.fileno())
        os.replace(temporary, path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def main() -> None:
    items = sessions()
    root_text = generate_root(items)
    map_text = generate_map(items)
    atomic_write(ROOT_README, root_text)
    atomic_write(FILE_MAP, map_text)
    print(f"Indices gerados para {len(items)} sessoes.")


if __name__ == "__main__":
    main()
