"""Fase de política: transformar scores em seleção sob capacidade.

Todas as políticas devem receber a mesma população elegível e o mesmo limite.
Empates e aleatoriedade precisam ter comportamento determinístico documentado.
"""

from typing import Any, Mapping


def aplicar_politica_aleatoria(
    elegiveis: Any,
    *,
    capacidade: int,
    seed: int,
) -> Any:
    """Selecione o baseline aleatório sem consultar o desfecho."""
    raise NotImplementedError("Exercício: implemente a política aleatória.")


def aplicar_regra_de_negocio(
    elegiveis: Any,
    *,
    capacidade: int,
    parametros: Mapping[str, Any],
) -> Any:
    """Aplique uma regra simples, pré-declarada e temporalmente válida."""
    raise NotImplementedError("Exercício: implemente a política por regra.")


def aplicar_politica_por_score(
    elegiveis_com_score: Any,
    *,
    coluna_score: str,
    capacidade: int,
) -> Any:
    """Priorize por risco ou efeito sem ultrapassar a capacidade."""
    raise NotImplementedError(
        "Exercício: ordene com desempate estável e valide a elegibilidade."
    )

