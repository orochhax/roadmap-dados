"""Microdesafio executavel: limiar, metricas, capacidade e custo.

Nao ha gabarito neste arquivo. A primeira execucao apresenta o contrato e as
entradas. Implemente os TODOs e use o mesmo conjunto em todos os limiares.
"""

from __future__ import annotations

from typing import Any


ALVOS = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1]
PROBABILIDADES = [
    0.92,
    0.81,
    0.76,
    0.71,
    0.68,
    0.63,
    0.57,
    0.54,
    0.49,
    0.46,
    0.41,
    0.37,
    0.34,
    0.29,
    0.26,
    0.22,
    0.18,
    0.14,
    0.09,
    0.04,
]
LIMIARES = [0.30, 0.50, 0.70]
CUSTO_FP = 20.0
CUSTO_FN = 500.0
CAPACIDADE_MAXIMA = 8


def gerar_predicoes(probabilidades: list[float], limiar: float) -> list[int]:
    """TODO: documente se uma probabilidade igual ao limiar recebe acao."""
    raise NotImplementedError("Implemente gerar_predicoes.")


def matriz_confusao(alvos: list[int], predicoes: list[int]) -> dict[str, int]:
    """TODO: conte TP, FP, FN e TN sem usar o conjunto duas vezes."""
    raise NotImplementedError("Implemente matriz_confusao.")


def calcular_metricas(contagens: dict[str, int]) -> dict[str, float]:
    """TODO: calcule precision, recall e F1 tratando divisao por zero."""
    raise NotImplementedError("Implemente calcular_metricas.")


def calcular_custo(contagens: dict[str, int]) -> float:
    """TODO: use os custos de FP e FN declarados no inicio do arquivo."""
    raise NotImplementedError("Implemente calcular_custo.")


def avaliar_limiares() -> list[dict[str, Any]]:
    """TODO: produza uma linha comparavel por limiar e sinalize a capacidade."""
    raise NotImplementedError("Implemente avaliar_limiares.")


def main() -> None:
    if len(ALVOS) != len(PROBABILIDADES):
        raise ValueError("Alvos e probabilidades precisam ter o mesmo tamanho.")

    print("Microdesafio de limiares preparado.")
    print(f"Observacoes: {len(ALVOS)}")
    print(f"Limiares: {LIMIARES}")
    print(f"Custos: FP=R${CUSTO_FP:.2f}; FN=R${CUSTO_FN:.2f}")
    print(f"Capacidade maxima de acoes: {CAPACIDADE_MAXIMA}")
    print("TODO: compare metricas e custo e defenda uma politica viavel.")


if __name__ == "__main__":
    main()
