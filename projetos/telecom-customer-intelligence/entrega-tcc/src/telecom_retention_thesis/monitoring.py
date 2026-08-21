"""Fase de monitoramento: rastreio, drift, retreinamento e rollback.

As decisões de ciclo de vida devem usar limites declarados antes de abrir a
janela de monitoramento. Toda promoção ou reversão precisa ser auditável.
"""

from pathlib import Path
from typing import Any, Mapping


def registrar_experimento(
    parametros: Mapping[str, Any],
    metricas: Mapping[str, float],
    artefatos: Mapping[str, Path],
) -> str:
    """Registre no MLflow dados, código, parâmetros, métricas e artefatos."""
    raise NotImplementedError(
        "Exercício: implemente tracking e devolva um identificador reproduzível."
    )


def avaliar_janela_monitoramento(
    referencia: Any,
    atual: Any,
    *,
    limites: Mapping[str, float],
) -> Mapping[str, Any]:
    """Meça qualidade, drift, calibração e valor sem retreinar silenciosamente."""
    raise NotImplementedError(
        "Exercício: implemente o relatório e compare com limites pré-definidos."
    )


def decidir_ciclo_de_vida(
    champion: Mapping[str, Any],
    challenger: Mapping[str, Any],
    monitoramento: Mapping[str, Any],
    *,
    regra: Mapping[str, Any],
) -> str:
    """Retorne manter, promover, retreinar ou reverter com justificativa."""
    raise NotImplementedError(
        "Exercício: implemente uma decisão determinística e auditável."
    )


def simular_rollback(registro_modelos: Any, versao_anterior: str) -> Any:
    """Restaure a versão anterior sem apagar histórico ou artefatos."""
    raise NotImplementedError(
        "Exercício: simule rollback e prove a versão ativa por teste."
    )

