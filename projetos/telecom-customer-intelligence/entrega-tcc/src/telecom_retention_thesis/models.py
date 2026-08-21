"""Fase de modelos: risco de churn e efeito incremental.

Comece pelos baselines. Use pipelines reproduzíveis e preserve o teste final e
a janela de monitoramento até o protocolo estar congelado.
"""

from typing import Any, Mapping


def treinar_modelos_de_risco(
    treino: Any,
    validacao: Any,
    *,
    configuracao: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Treine regressão logística e XGBoost sem acessar teste/monitoramento."""
    raise NotImplementedError(
        "Exercício: implemente, calibre e versione os modelos de risco."
    )


def treinar_estimador_incremental(
    treino: Any,
    validacao: Any,
    *,
    configuracao: Mapping[str, Any],
) -> Any:
    """Estime resposta heterogênea com um único método causal justificado."""
    raise NotImplementedError(
        "Exercício: implemente o estimador e documente suas premissas."
    )


def gerar_scores(modelo: Any, dados_decisao: Any) -> Any:
    """Produza scores auditáveis sem usar tratamento ou desfecho futuro."""
    raise NotImplementedError(
        "Exercício: gere probabilidades/efeitos e preserve as chaves da decisão."
    )

