"""Fase de dados: tabela de decisão e piloto sintético.

Implemente os contratos respeitando a data de decisão. O gerador deve ser
determinístico para a mesma seed e marcar tratamento e desfecho como sintéticos.
"""

from pathlib import Path
from typing import Any, Mapping


def construir_base_decisao(
    fontes: Mapping[str, Path],
    *,
    data_decisao: str,
    horizonte_dias: int,
) -> Any:
    """Crie uma linha por cliente usando somente fatos disponíveis na decisão."""
    raise NotImplementedError(
        "Exercício: implemente a base cliente-data e bloqueie vazamento temporal."
    )


def gerar_piloto_sintetico(
    base_decisao: Any,
    *,
    seed: int,
    taxa_tratamento: float,
    versao_gerador: str,
) -> Any:
    """Gere atribuição e desfecho sintéticos sem expor contrafactuais às features."""
    raise NotImplementedError(
        "Exercício: implemente o piloto e marque origem_sintetica=true."
    )


def validar_contrato_sintetico(dados: Any, metadados: Mapping[str, Any]) -> None:
    """Recuse artefatos causais que não declarem origem, versão e seed."""
    raise NotImplementedError(
        "Exercício: valide schema, marcação sintética, versão e seed."
    )


def criar_splits_temporais(dados: Any, limites: Mapping[str, str]) -> Any:
    """Separe treino, validação, teste e monitoramento sem embaralhar o tempo."""
    raise NotImplementedError(
        "Exercício: implemente splits temporais e teste horizontes sobrepostos."
    )

