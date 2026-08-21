-- Schema local do ranking quantitativo e do backtest.

CREATE TABLE IF NOT EXISTS configuracao_projeto (
    configuracao_id INTEGER PRIMARY KEY CHECK (configuracao_id = 1),
    classe_escolhida VARCHAR NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    frequencia_rebalanceamento VARCHAR NOT NULL,
    custo_bps DOUBLE NOT NULL CHECK (custo_bps >= 0),
    top_k INTEGER NOT NULL CHECK (top_k > 0)
);

CREATE TABLE IF NOT EXISTS ativos (
    ticker VARCHAR PRIMARY KEY,
    data_inicio DATE NOT NULL,
    data_fim DATE,
    elegivel BOOLEAN NOT NULL,
    motivo_inelegibilidade VARCHAR
);

CREATE TABLE IF NOT EXISTS precos_ajustados (
    data DATE NOT NULL,
    ticker VARCHAR NOT NULL,
    preco_ajustado DOUBLE NOT NULL CHECK (preco_ajustado > 0),
    disponivel_em DATE NOT NULL,
    fonte VARCHAR NOT NULL,
    PRIMARY KEY (data, ticker),
    FOREIGN KEY (ticker) REFERENCES ativos(ticker)
);

CREATE TABLE IF NOT EXISTS fatores (
    data_rebalanceamento DATE NOT NULL,
    ticker VARCHAR NOT NULL,
    momentum DOUBLE,
    volatilidade DOUBLE,
    score DOUBLE NOT NULL,
    PRIMARY KEY (data_rebalanceamento, ticker)
);

CREATE TABLE IF NOT EXISTS ranking (
    data_rebalanceamento DATE NOT NULL,
    ticker VARCHAR NOT NULL,
    posicao INTEGER NOT NULL CHECK (posicao > 0),
    selecionado_top_k BOOLEAN NOT NULL,
    PRIMARY KEY (data_rebalanceamento, ticker)
);

CREATE TABLE IF NOT EXISTS resultados_carteira (
    data DATE NOT NULL,
    estrategia VARCHAR NOT NULL CHECK (estrategia IN ('pesos_iguais', 'top_k')),
    retorno_bruto DOUBLE NOT NULL,
    turnover DOUBLE NOT NULL CHECK (turnover >= 0),
    custo DOUBLE NOT NULL CHECK (custo >= 0),
    retorno_liquido DOUBLE NOT NULL,
    PRIMARY KEY (data, estrategia)
);
