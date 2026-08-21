"""Arquivo inicial — diferenças em diferenças do rollout regional."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


SEED = 42
CIDADES = (
    "Salvador",
    "Feira de Santana",
    "Vitória da Conquista",
    "Aracaju",
)
SEMANA_TRATAMENTO = 9
EFEITO_INJETADO_MIN = -12.0


def gerar_painel(tendencia_paralela: bool) -> pd.DataFrame:
    """Gere um painel válido ou uma violação controlada da hipótese."""
    raise NotImplementedError


def calcular_did_manual(painel: pd.DataFrame) -> float:
    """Calcule o contraste 2x2 respeitando os pesos declarados."""
    raise NotImplementedError


def estimar_regressao_e_event_study(painel: pd.DataFrame) -> dict[str, object]:
    """Estime interação, leads/lags e incerteza agrupada."""
    raise NotImplementedError


def executar_sensibilidades(painel: pd.DataFrame) -> pd.DataFrame:
    """Execute placebo e leave-one-city-out."""
    raise NotImplementedError


def main() -> None:
    diretorio = Path(__file__).resolve().parent
    # TODO: gere as duas bases, estime, valide e grave todas as saídas.
    _ = diretorio
    raise NotImplementedError("Complete o enunciado antes de executar.")


if __name__ == "__main__":
    main()

