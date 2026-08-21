"""Arquivo inicial — propensity score da oferta de retenção.

As funções abaixo são contratos de trabalho; implemente-as conforme ENUNCIADO.md.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


SEED = 42
COVARIAVEIS_PRE_TRATAMENTO = (
    "nps",
    "chamados_90d",
    "atraso_dias",
    "tempo_cliente_meses",
    "mensalidade",
)


def gerar_amostra_observacional(clientes: pd.DataFrame, baixo_overlap: bool) -> pd.DataFrame:
    """Gere oferta e desfecho de forma reproduzível, sem executar a análise."""
    raise NotImplementedError


def estimar_propensity(dados: pd.DataFrame) -> pd.Series:
    """Estime probabilidades usando somente covariáveis pré-tratamento."""
    raise NotImplementedError


def calcular_smd(dados: pd.DataFrame, pesos: pd.Series | None = None) -> pd.DataFrame:
    """Calcule diferenças padronizadas por covariável."""
    raise NotImplementedError


def executar_matching_e_ipw(dados: pd.DataFrame) -> dict[str, object]:
    """Implemente diagnósticos, estimativas e sensibilidades obrigatórias."""
    raise NotImplementedError


def main() -> None:
    raiz_repo = Path(__file__).resolve().parents[5]
    caminho_clientes = raiz_repo / "dados" / "clientes_telecom.csv"
    # TODO: carregue, gere as duas bases, analise e grave as saídas.
    _ = caminho_clientes
    raise NotImplementedError("Complete o fluxo descrito no enunciado.")


if __name__ == "__main__":
    main()

