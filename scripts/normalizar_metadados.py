"""Remove números e datas antigas dos cabeçalhos de artefatos do roadmap."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MONTH_RE = re.compile(r"^(?:OK - )?\d{2} - .+ \d{4}(?: \[\d+-\d+\])?$")
DAY_DIR_RE = re.compile(r"^(?:OK - )?Dia \d{2}-\d{2} - .+$")
TEXT_SUFFIXES = {".py", ".sql", ".md", ".txt", ".ipynb"}
DATE = r"\d{2}/\d{2}/20\d{2}"

HEADER_DAY_FIRST = re.compile(
    rf"(?m)^(?P<prefix>[ \t]*(?:#{{1,6}}|--)\s*)"
    rf"(?P<project>Projeto\s+—\s+)?Dia\s+#?0*\d+\s*(?:—|:|-)\s*"
    rf"(?P<topic>.*?)(?:\s+—\s+{DATE})?[ \t]*$"
)
HEADER_DAY_LAST = re.compile(
    r"(?m)^(?P<prefix>[ \t]*(?:#{1,6}|--)\s*)"
    r"(?P<label>.*?)\s+—\s+Dia\s+#?0*\d+"
    r"(?:(?:\s+—\s+|:\s*)(?P<topic>.*?))?[ \t]*$"
)
NOTEBOOK_DAY_FIRST = re.compile(
    rf'(?m)^(?P<lead>[ \t]*")#\s+(?P<project>Projeto\s+—\s+)?'
    rf'Dia\s+#?0*\d+\s*(?:—|:|-)\s*(?P<topic>.*?)'
    rf'(?:\s+—\s+{DATE})?\\n",(?P<trail>[ \t]*)\r?$'
)
NOTEBOOK_DAY_LAST = re.compile(
    r'(?m)^(?P<lead>[ \t]*")#\s+(?P<label>.*?)\s+—\s+Dia\s+#?0*\d+'
    r'(?:(?:\s+—\s+|:\s*)(?P<topic>.*?))?\\n",(?P<trail>[ \t]*)\r?$'
)
NOTEBOOK_DATE_LINE = re.compile(
    rf'(?m)^[ \t]*"\\n\*\*Data:\*\*\s*{DATE}\\n",[ \t]*\r?\n?'
)
PLAIN_DATE_LINE = re.compile(rf"(?m)^\*\*Data:\*\*\s*{DATE}[ \t]*\r?\n?")
OBSOLETE_PROJECT_NAVIGATION = re.compile(
    r"(?m)^O momento de execução deste projeto segue o "
    r"\[README do Dia \d+\]\(<\.\./README\.md>\), não a data da pasta\."
    r"\r?\n(?:\r?\n)?"
)


def decode(path: Path) -> tuple[str, bool]:
    raw = path.read_bytes()
    has_bom = raw.startswith(b"\xef\xbb\xbf")
    return raw.decode("utf-8-sig" if has_bom else "utf-8"), has_bom


def encode(path: Path, text: str, has_bom: bool) -> None:
    path.write_bytes(text.encode("utf-8-sig" if has_bom else "utf-8"))


def clean_heading_match(match: re.Match[str]) -> str:
    project = match.groupdict().get("project") or ""
    topic = match.group("topic").strip()
    return f"{match.group('prefix')}{project}{topic}"


def clean_trailing_match(match: re.Match[str]) -> str:
    topic = (match.groupdict().get("topic") or "").strip()
    if match.group("label").strip().lower().endswith("tcc") and topic.lower().startswith("tcc:"):
        topic = topic[4:].strip()
    suffix = f" — {topic}" if topic else ""
    return f"{match.group('prefix')}{match.group('label').strip()}{suffix}"


def clean_notebook_first(match: re.Match[str]) -> str:
    project = match.groupdict().get("project") or ""
    topic = match.group("topic").strip()
    return f'{match.group("lead")}# {project}{topic}\\n",{match.group("trail")}'


def clean_notebook_last(match: re.Match[str]) -> str:
    topic = (match.groupdict().get("topic") or "").strip()
    suffix = f" — {topic}" if topic else ""
    return (
        f'{match.group("lead")}# {match.group("label").strip()}{suffix}'
        f'\\n",{match.group("trail")}'
    )


def strip_header_date_suffixes(text: str) -> str:
    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines[:12]):
        ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
        body = line[: -len(ending)] if ending else line
        if re.match(r"^[ \t]*(?:#|--)", body):
            body = re.sub(rf"\s+—\s+{DATE}[ \t]*$", "", body)
            lines[index] = body + ending
    return "".join(lines)


def normalize(text: str) -> str:
    uses_crlf = "\r\n" in text
    text = NOTEBOOK_DAY_FIRST.sub(clean_notebook_first, text)
    text = NOTEBOOK_DAY_LAST.sub(clean_notebook_last, text)
    text = NOTEBOOK_DATE_LINE.sub("", text)
    text = HEADER_DAY_FIRST.sub(clean_heading_match, text)
    text = HEADER_DAY_LAST.sub(clean_trailing_match, text)
    text = PLAIN_DATE_LINE.sub("", text)
    text = OBSOLETE_PROJECT_NAVIGATION.sub("", text)
    text = strip_header_date_suffixes(text)
    if uses_crlf:
        text = text.replace("\r\n", "\n").replace("\n", "\r\n")
    return text


def targets() -> list[Path]:
    roots: list[Path] = []
    for month in ROOT.iterdir():
        if not month.is_dir() or not MONTH_RE.match(month.name):
            continue
        roots.extend(day for day in month.iterdir() if day.is_dir() and DAY_DIR_RE.match(day.name))
    projects = ROOT / "projetos"
    if projects.is_dir():
        roots.extend(path for path in projects.iterdir() if path.is_dir())
    return sorted(
        path
        for base in roots
        for path in base.rglob("*")
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="grava as normalizações")
    args = parser.parse_args()

    changed: list[tuple[Path, str, bool]] = []
    for path in targets():
        original, has_bom = decode(path)
        updated = normalize(original)
        if updated != original:
            changed.append((path, updated, has_bom))

    if args.write:
        for path, updated, _ in changed:
            if path.suffix.lower() == ".ipynb":
                json.loads(updated)
        for path, updated, has_bom in changed:
            encode(path, updated, has_bom)

    action = "normalizados" if args.write else "pendentes"
    print(f"Arquivos {action}: {len(changed)}")
    for path, _, _ in changed:
        print(f"- {path.relative_to(ROOT)}")
    return 0 if args.write or not changed else 1


if __name__ == "__main__":
    raise SystemExit(main())
