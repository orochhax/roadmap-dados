"""Exercício: cliente REST com modo HTTP e modo local simulado.

Leia ENUNCIADO.md antes de começar. Os TODOs indicam responsabilidades, não
uma solução. Não coloque tokens reais neste arquivo.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
ARQUIVO_FAKE = BASE_DIR / "api_fake_paginas.json"
PASTA_SAIDA = BASE_DIR / "entrega"


def carregar_cenario_fake(caminho: Path) -> dict[str, Any]:
    """Carregue o contrato local usado nos testes offline."""
    # TODO: validar existência, JSON e estrutura mínima esperada.
    raise NotImplementedError


def obter_configuracao() -> dict[str, str]:
    """Leia configuração externa sem revelar credenciais em logs."""
    # TODO: separar configuração do modo HTTP e do modo local.
    raise NotImplementedError


def buscar_pagina(
    cursor: str | None,
    atualizado_depois_de: str | None,
    modo: str,
    contexto: dict[str, Any],
) -> dict[str, Any]:
    """Busque uma página e aplique a política limitada de falhas."""
    # TODO: parâmetros, headers, timeout, status, retry/backoff e Retry-After.
    raise NotImplementedError


def coletar_todas_as_paginas(
    atualizado_depois_de: str | None,
    modo: str,
    contexto: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    """Percorra os cursores, detecte ciclos e reúna métricas."""
    # TODO: paginação, cursor repetido, página vazia e deduplicação.
    raise NotImplementedError


def carregar_estado_incremental(caminho: Path) -> dict[str, Any]:
    """Leia a última marca confirmada de uma execução anterior."""
    # TODO: diferenciar ausência de estado, estado válido e estado corrompido.
    raise NotImplementedError


def salvar_resultados(
    chamados: list[dict[str, Any]],
    metricas: dict[str, Any],
    pasta_saida: Path,
) -> None:
    """Grave dados, cache, métricas e estado somente no momento correto."""
    # TODO: CSV determinístico, JSON bruto, cache e atualização atômica do estado.
    raise NotImplementedError


def main() -> None:
    """Orquestre uma execução sem misturar as responsabilidades acima."""
    # TODO: permitir escolher modo local ou HTTP e registrar falhas sem segredos.
    raise NotImplementedError


if __name__ == "__main__":
    main()
