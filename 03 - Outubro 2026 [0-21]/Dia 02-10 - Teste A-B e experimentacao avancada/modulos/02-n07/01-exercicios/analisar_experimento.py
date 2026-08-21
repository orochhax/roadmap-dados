"""Arquivo inicial da análise avançada do experimento.

Implemente o protocolo descrito em ENUNCIADO.md sem mudar critérios após ver
o resultado.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class Protocolo:
    alpha: float = 0.05
    poder: float = 0.80
    mde_pontos_percentuais: float = 1.5
    seed: int = 42


def gerar_experimento(protocolo: Protocolo) -> pd.DataFrame:
    """Gere a entrada reproduzível especificada no enunciado."""
    raise NotImplementedError


def verificar_srm(dados: pd.DataFrame) -> dict[str, float | bool]:
    """Teste a proporção observada contra a alocação planejada."""
    raise NotImplementedError


def aplicar_cuped(dados: pd.DataFrame) -> pd.Series:
    """Retorne a métrica ajustada usando somente a covariável pré-período."""
    raise NotImplementedError


def simular_peeking(protocolo: Protocolo, repeticoes: int = 500) -> pd.DataFrame:
    """Compare regra ingênua e regra sequencial em experimentos sem efeito."""
    raise NotImplementedError


def executar(diretorio: Path) -> None:
    """Gere dados, valide, estime, simule e grave as saídas obrigatórias."""
    raise NotImplementedError


if __name__ == "__main__":
    executar(Path(__file__).resolve().parent)

