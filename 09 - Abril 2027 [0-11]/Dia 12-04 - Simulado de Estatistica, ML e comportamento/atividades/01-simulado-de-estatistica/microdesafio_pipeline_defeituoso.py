"""Microdesafio executavel: audite um pipeline com resultado suspeito.

O trecho foi entregue como codigo legado e contem pelo menos dois problemas de
desenho experimental. Execute-o, nao confie automaticamente na metrica e anote
suas hipoteses antes de modificar qualquer linha. O arquivo nao traz o gabarito.

Dependencias esperadas nesta etapa do roadmap: pandas e scikit-learn.
"""

from __future__ import annotations

from pathlib import Path


def encontrar_raiz(inicio: Path | None = None) -> Path:
    atual = (inicio or Path(__file__)).resolve()
    for candidato in (atual, *atual.parents):
        if (candidato / "dados" / "clientes_telecom.csv").is_file():
            return candidato
    raise FileNotFoundError("Nao encontrei dados/clientes_telecom.csv.")


def executar_pipeline_legado() -> tuple[float, float, int, int]:
    """Executa exatamente o fluxo recebido; a auditoria e parte do desafio."""
    try:
        import pandas as pd
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score, f1_score
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
    except ModuleNotFoundError as erro:
        raise RuntimeError(
            "Instale pandas e scikit-learn no ambiente desta etapa antes de executar."
        ) from erro

    caminho = encontrar_raiz() / "dados" / "clientes_telecom.csv"
    dados = pd.read_csv(caminho)
    colunas = [
        "mensalidade",
        "nps",
        "chamados_90d",
        "atraso_dias",
        "tempo_cliente_meses",
        "status_atual",
    ]

    x = pd.get_dummies(dados[colunas], drop_first=False)
    y = dados["churn"].astype(int)

    escalador = StandardScaler()
    x_escalado = escalador.fit_transform(x)
    x_treino, x_validacao, y_treino, y_validacao = train_test_split(
        x_escalado,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    # Trecho legado recebido: audite o fluxo inteiro antes de confiar nele.
    x_ajuste = pd.concat(
        [pd.DataFrame(x_treino), pd.DataFrame(x_validacao)], ignore_index=True
    )
    y_ajuste = pd.concat(
        [y_treino.reset_index(drop=True), y_validacao.reset_index(drop=True)],
        ignore_index=True,
    )
    modelo = LogisticRegression(max_iter=1000, random_state=42)
    modelo.fit(x_ajuste, y_ajuste)

    predicoes = modelo.predict(x_validacao)
    return (
        float(accuracy_score(y_validacao, predicoes)),
        float(f1_score(y_validacao, predicoes, zero_division=0)),
        len(x_treino),
        len(x_validacao),
    )


def main() -> None:
    try:
        accuracy, f1, n_treino, n_validacao = executar_pipeline_legado()
    except RuntimeError as erro:
        print(erro)
        print("O starter esta integro; execute novamente no ambiente de ML da etapa.")
        return
    print("Resultado do pipeline legado (ainda nao aprovado):")
    print(f"Treino: {n_treino}; validacao: {n_validacao}")
    print(f"Accuracy: {accuracy:.4f}; F1: {f1:.4f}")
    print("TODO 1: identifique pelo menos dois motivos para desconfiar do resultado.")
    print("TODO 2: corrija features, split e pipeline e meça novamente sem olhar o teste.")
    print("TODO 3: explique por que a metrica corrigida pode piorar e ainda ser mais honesta.")


if __name__ == "__main__":
    main()
