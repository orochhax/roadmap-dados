"""Arquivo inicial do validador de eventos do autoatendimento.

Amplie a fixture e implemente os contratos descritos em ENUNCIADO.md.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from pathlib import Path


EVENTOS_EXEMPLO: tuple[dict[str, object], ...] = (
    {
        "event_id": "evt-001",
        "event_name": "account_created",
        "occurred_at": "2026-08-21T12:00:00-03:00",
        "user_id": "cli-001",
        "anonymous_id": None,
        "session_id": "ses-001",
        "schema_version": 1,
        "properties": {"channel": "app"},
    },
    {
        "event_id": "evt-002",
        "event_name": "diagnostic_started",
        "occurred_at": "2026-08-21T12:05:00-03:00",
        "user_id": "cli-001",
        "anonymous_id": None,
        "session_id": "ses-001",
        "schema_version": 1,
        "properties": {"diagnostic_id": "diag-001"},
    },
    # TODO: acrescente eventos válidos e todos os casos de borda do enunciado.
)


def validar_evento(evento: Mapping[str, object]) -> tuple[bool, list[str]]:
    """Retorne validade e todos os motivos encontrados, sem corrigir silenciosamente."""
    raise NotImplementedError


def processar_eventos(
    eventos: Iterable[Mapping[str, object]],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    """Valide, deduplique e separe aceitos de rejeitados."""
    raise NotImplementedError


def gravar_saidas(diretorio: Path) -> None:
    """Gere tracking plan, JSONL e relatório de qualidade."""
    raise NotImplementedError


def main() -> None:
    gravar_saidas(Path(__file__).resolve().parent)


if __name__ == "__main__":
    main()

