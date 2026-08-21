# Armazenamento e processamento

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-102-armazenamento-e-processamento.py`.
- **Entradas:** `dados/pedidos.csv` e schema. **Fallback local:** Parquet particionado consultado com DuckDB.

## Aprenda agora

- **Definição:** objeto guarda arquivos, relacional serve transações, warehouse serve análise, lakehouse combina arquivos e tabelas; partição reduz leitura.
- **Exemplo mínimo:** grave Parquet particionado por `ano/mes` e leia somente uma partição; compare bytes e tempo.
- **Erro comum:** criar partição por coluna de alta cardinalidade ou usar CSV como contrato tipado.

## Núcleo essencial

1. [ ] Compare objeto, arquivo, banco relacional, warehouse e lakehouse para quatro tipos de dados.
2. [ ] Crie uma matriz decisão com volume, latência, custo, governança e acesso.
3. [ ] Converta CSV para Parquet e compare tamanho/tempo de leitura.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-102-armazenamento-e-processamento.py`:** compare CSV e Parquet ao projetar somente `data_pedido` e `valor_pedido`; explique quando Spark ou warehouse seria excesso.
- [ ] Particione por ano/mês, leia somente janeiro de 2026 e registre arquivos lidos e linhas retornadas.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-102-armazenamento-e-processamento.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.
