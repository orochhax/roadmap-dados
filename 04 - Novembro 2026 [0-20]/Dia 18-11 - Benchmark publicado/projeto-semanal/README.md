# Projeto — Benchmark publicado

## Manifesto de entradas

- **Obrigatórias:** `dados/clientes_telecom.csv`, `dados/pedidos.csv`, split fixo, pipeline, calibração, limiar, matriz de custos e XGBoost instalado.
- **Saídas:** `benchmark.csv`, `parametros.json` e README com regra de seleção.
- **Fallback local:** use os CSVs versionados e reduza a amostra mantendo a proporção do alvo; serviço externo não é requisito.

## Núcleo essencial

1. [ ] Compare Dummy, regressão logística, Random Forest e XGBoost no mesmo protocolo.
2. [ ] Registre biblioteca, versão, seed, métricas e tempos de treino e inferência.
3. [ ] Salve as métricas em `benchmark.csv` e os parâmetros em `parametros.json`.
4. [ ] Recomende champion e challenger com qualidade, custo, latência, explicabilidade e três trade-offs.

## Prática obrigatória

- [ ] Simule três valores de Top-N com orçamento, custo de contato e valor de retenção declarados.
- [ ] Analise segmentos e estabilidade em uma segunda seed.

## Concluído quando

- [ ] A tabela contém os quatro modelos obrigatórios no mesmo split, pré-processamento e métricas.
- [ ] CSV, JSON e README permitem reproduzir a seleção.
- [ ] A recomendação cita uma evidência de negócio e uma limitação.
