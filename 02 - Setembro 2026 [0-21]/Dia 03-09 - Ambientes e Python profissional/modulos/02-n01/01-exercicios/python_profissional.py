"""Arquivo inicial do núcleo tipado de incidentes.

Leia ENUNCIADO.md. As assinaturas indicam contratos, não a implementação.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence


@dataclass
class Incidente:
    """Defina os campos e as garantias de um incidente válido."""

    # TODO: declare os campos exigidos no enunciado.


def converter_incidente(linha: Mapping[str, str]) -> Incidente:
    """Converta uma linha bruta ou informe claramente por que ela é inválida."""
    raise NotImplementedError


def resumir_por_cidade(incidentes: Sequence[Incidente]) -> list[dict[str, object]]:
    """Produza o resumo determinístico pedido no enunciado."""
    raise NotImplementedError


def executar(caminho_entrada: Path, caminho_saida: Path) -> None:
    """Orquestre leitura, validação, resumo e escrita."""
    raise NotImplementedError


def main() -> None:
    raiz_repo = Path(__file__).resolve().parents[5]
    entrada = raiz_repo / "dados" / "incidentes.csv"
    saida = Path(__file__).with_name("resumo_incidentes.json")
    executar(entrada, saida)


if __name__ == "__main__":
    main()

