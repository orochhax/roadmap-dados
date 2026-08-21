"""Arquivo inicial — controle sintético do programa de fibra."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


SEED = 42
SEMANA_INTERVENCAO = 25
UNIDADE_TRATADA = "Salvador"


def gerar_painel(bom_ajuste_possivel: bool) -> pd.DataFrame:
    """Gere a base controlada descrita no enunciado."""
    raise NotImplementedError


def ajustar_pesos(
    tratada_pre: np.ndarray,
    doadores_pre: np.ndarray,
) -> np.ndarray:
    """Encontre pesos não negativos que somem um, sem consultar o pós."""
    raise NotImplementedError


def calcular_placebos(painel: pd.DataFrame) -> pd.DataFrame:
    """Trate cada doadora como placebo e registre RMSPE pré/pós."""
    raise NotImplementedError


def executar(diretorio: Path) -> None:
    """Gere, ajuste, valide, sensibilize e grave os artefatos."""
    raise NotImplementedError


if __name__ == "__main__":
    executar(Path(__file__).resolve().parent)

