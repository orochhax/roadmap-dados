"""Starter executavel para comparar politicas de decisao.

As probabilidades de demonstracao sao sinteticas e existem apenas para permitir
que a politica seja programada antes de haver um modelo salvo. Elas nao podem ser
apresentadas como previsoes reais nem usadas para concluir desempenho do modelo.
"""

from __future__ import annotations

import csv
import random
from pathlib import Path
from typing import Any


SEED = 42
LIMIARES = {
    "conservadora": 0.70,
    "equilibrada": 0.50,
    "agressiva": 0.30,
}
CUSTOS = {
    "acao": 35.0,
    "falso_positivo": 20.0,
    "falso_negativo": 500.0,
}


def encontrar_raiz(inicio: Path | None = None) -> Path:
    atual = (inicio or Path(__file__)).resolve()
    for candidato in (atual, *atual.parents):
        if (candidato / "dados" / "clientes_telecom.csv").is_file():
            return candidato
    raise FileNotFoundError("Nao encontrei dados/clientes_telecom.csv.")


def carregar_clientes(caminho: Path) -> list[dict[str, Any]]:
    # `utf-8-sig` aceita tanto CSV comum quanto o BOM presente nas fixtures.
    with caminho.open(encoding="utf-8-sig", newline="") as arquivo:
        linhas = list(csv.DictReader(arquivo))

    obrigatorias = {"cliente_id", "cidade", "plano", "mensalidade", "churn"}
    ausentes = obrigatorias.difference(linhas[0] if linhas else {})
    if ausentes:
        raise ValueError(f"Colunas obrigatorias ausentes: {sorted(ausentes)}")

    for linha in linhas:
        linha["mensalidade"] = float(linha["mensalidade"])
        linha["churn"] = int(linha["churn"])
    return linhas


def criar_amostra_demo(
    clientes: list[dict[str, Any]], quantidade: int = 60, seed: int = SEED
) -> list[dict[str, Any]]:
    """Anexa probabilidades aleatorias; substitua-as por predict_proba depois."""
    gerador = random.Random(seed)
    amostra: list[dict[str, Any]] = []
    for cliente in clientes[:quantidade]:
        registro = dict(cliente)
        registro["probabilidade_churn"] = round(gerador.random(), 4)
        amostra.append(registro)
    return amostra


def decidir_acao(probabilidade: float, limiar: float) -> bool:
    """TODO: aplique o contrato do limiar e documente o caso de igualdade."""
    raise NotImplementedError("Implemente decidir_acao.")


def custo_por_cliente(
    alvo_real: int, recebeu_acao: bool, custos: dict[str, float]
) -> float:
    """TODO: traduza TP, FP, FN e TN para o custo definido no enunciado."""
    raise NotImplementedError("Implemente custo_por_cliente.")


def avaliar_politica(
    registros: list[dict[str, Any]], nome: str, limiar: float
) -> dict[str, Any]:
    """TODO: retorne volume, matriz de confusao e custo total comparaveis."""
    raise NotImplementedError("Implemente avaliar_politica.")


def resumir_por_segmento(
    registros: list[dict[str, Any]], coluna: str, limiar: float
) -> list[dict[str, Any]]:
    """TODO: compare taxa de acao e custo sem perder grupos pequenos."""
    raise NotImplementedError("Implemente resumir_por_segmento.")


def selecionar_revisao_humana(
    registros: list[dict[str, Any]], minimo: float = 0.45, maximo: float = 0.55
) -> list[dict[str, Any]]:
    """TODO: selecione a faixa e declare como tratou os dois limites."""
    raise NotImplementedError("Implemente selecionar_revisao_humana.")


def main() -> None:
    raiz = encontrar_raiz()
    clientes = carregar_clientes(raiz / "dados" / "clientes_telecom.csv")
    amostra = criar_amostra_demo(clientes)

    print("Starter do case de decisao carregado.")
    print(f"Clientes na base: {len(clientes)}")
    print(f"Registros demo com probabilidade sintetica: {len(amostra)}")
    print(f"Politicas a comparar: {', '.join(LIMIARES)}")
    print("Proximo passo: implemente os TODOs e substitua a entrada demo quando houver predict_proba.")


if __name__ == "__main__":
    main()
