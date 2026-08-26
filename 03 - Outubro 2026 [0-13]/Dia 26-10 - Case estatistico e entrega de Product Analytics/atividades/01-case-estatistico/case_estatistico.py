"""Starter executavel do case estatistico de antes e depois.

O arquivo prepara e valida as entradas, mas deixa os calculos e as decisoes
como TODO. Execute primeiro sem alterar nada para conhecer o conjunto de dados;
depois implemente uma funcao por vez sem procurar uma solucao completa.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


# Entrada congelada do case: nao altere a data depois de observar os resultados.
DATA_MUDANCA = "2026-05-01"
SEED = 42


def encontrar_raiz(inicio: Path | None = None) -> Path:
    """Encontra a raiz pelo diretorio `dados`, sem depender do terminal atual."""
    atual = (inicio or Path(__file__)).resolve()
    for candidato in (atual, *atual.parents):
        if (candidato / "dados" / "incidentes.csv").is_file():
            return candidato
    raise FileNotFoundError("Nao encontrei dados/incidentes.csv na arvore do projeto.")


def carregar_incidentes(caminho: Path) -> list[dict[str, Any]]:
    """Carrega somente tipos necessarios; ainda nao cria antes/depois."""
    # `utf-8-sig` aceita tanto CSV comum quanto o BOM presente nas fixtures.
    with caminho.open(encoding="utf-8-sig", newline="") as arquivo:
        linhas = list(csv.DictReader(arquivo))

    obrigatorias = {"id", "cidade", "duracao_min", "data_abertura"}
    ausentes = obrigatorias.difference(linhas[0] if linhas else {})
    if ausentes:
        raise ValueError(f"Colunas obrigatorias ausentes: {sorted(ausentes)}")

    for linha in linhas:
        linha["duracao_min"] = float(linha["duracao_min"])
    return linhas


def separar_periodos(
    incidentes: list[dict[str, Any]], data_mudanca: str
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """TODO: devolva amostras antes/depois sem sobrepor observacoes."""
    raise NotImplementedError("Implemente separar_periodos.")


def resumir_duracoes(valores: list[float]) -> dict[str, float]:
    """TODO: calcule pelo menos n, media, mediana e dispersao escolhida."""
    raise NotImplementedError("Implemente resumir_duracoes.")


def calcular_tamanho_efeito(antes: list[float], depois: list[float]) -> float:
    """TODO: implemente a definicao estudada e trate variancia nula."""
    raise NotImplementedError("Implemente calcular_tamanho_efeito.")


def comparar_cidade_mais_frequente(
    antes: list[dict[str, Any]], depois: list[dict[str, Any]]
) -> dict[str, Any]:
    """TODO: compare resultado geral e estratificado na mesma cidade."""
    raise NotImplementedError("Implemente comparar_cidade_mais_frequente.")


def simular_mudanca_de_composicao(seed: int = SEED) -> list[dict[str, Any]]:
    """TODO: crie dados em que composicao, e nao processo, muda o agregado."""
    raise NotImplementedError("Implemente simular_mudanca_de_composicao.")


def avaliar_outlier(depois: list[float], valor_extremo: float = 2000.0) -> dict[str, Any]:
    """TODO: compare media, mediana e efeito antes/depois do valor extremo."""
    raise NotImplementedError("Implemente avaliar_outlier.")


def main() -> None:
    raiz = encontrar_raiz()
    incidentes = carregar_incidentes(raiz / "dados" / "incidentes.csv")
    cidades = {str(linha["cidade"]) for linha in incidentes}

    print("Starter do case estatistico carregado.")
    print(f"Linhas disponiveis: {len(incidentes)}")
    print(f"Cidades distintas: {len(cidades)}")
    print(f"Data da mudanca: {DATA_MUDANCA}")
    print("Proximo passo: defina a data e implemente os TODOs do enunciado.")


if __name__ == "__main__":
    main()
