"""Fase de avaliação: predição, causalidade e valor da política.

Congele métricas antes do teste final. Compare políticas na mesma população,
período, capacidade e função de custo; reporte incerteza e resultados negativos.
"""

from typing import Any, Mapping


def avaliar_risco(
    observado: Any,
    probabilidades: Any,
    *,
    capacidade: int,
) -> Mapping[str, float]:
    """Calcule PR-AUC, recall no Top-K, Brier e medidas de calibração."""
    raise NotImplementedError("Exercício: implemente e teste as métricas de risco.")


def avaliar_efeito(
    dados_piloto: Any,
    efeito_estimado: Any,
    *,
    configuracao: Mapping[str, Any],
) -> Mapping[str, float]:
    """Estime efeito, incerteza e qualidade do ordenamento incremental."""
    raise NotImplementedError(
        "Exercício: implemente ITT/efeito escolhido, intervalo e AUUC/Qini."
    )


def comparar_politicas(
    dados_piloto: Any,
    selecoes: Mapping[str, Any],
    *,
    capacidade: int,
    custo_contato: float,
    valor_retencao: float,
) -> Any:
    """Compare ganho incremental e valor líquido sob contratos idênticos."""
    raise NotImplementedError(
        "Exercício: compare políticas sem escolher custos após ver resultados."
    )


def avaliar_segmentos(
    dados: Any,
    resultados: Any,
    *,
    segmentos: tuple[str, ...],
) -> Any:
    """Reporte tamanho, métrica e incerteza dos segmentos pré-declarados."""
    raise NotImplementedError(
        "Exercício: implemente slices e sinalize amostras insuficientes."
    )

