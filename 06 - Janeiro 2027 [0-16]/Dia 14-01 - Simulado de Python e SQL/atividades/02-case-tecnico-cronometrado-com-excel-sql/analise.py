"""Case NexoVarejo: complete sem procurar uma solução pronta."""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DADOS_DIR = BASE_DIR / "dados"
SAIDA_DIR = BASE_DIR / "saida"


def main() -> None:
    """Orquestre validação, tratamento, análise e exportação."""
    # TODO: leia as quatro entradas por caminhos relativos.
    # TODO: valide schema, chaves, domínios e qualidade.
    # TODO: construa métricas e uma análise complementar ao SQL.
    # TODO: gere gráficos e exporte a tabela analítica.
    pass


if __name__ == "__main__":
    main()
