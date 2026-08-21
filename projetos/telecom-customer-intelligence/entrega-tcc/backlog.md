# Backlog obrigatório — entrega do TCC

Execute os itens na ordem. Um gate incompleto impede avançar para o benchmark
final.

## Gate 0 — protocolo antes dos resultados

- [ ] Congelar pergunta, hipótese principal e hipótese nula.
- [ ] Definir unidade, data de decisão, horizonte e população elegível.
- [ ] Definir capacidade, custo por contato e valor de uma retenção.
- [ ] Escolher métrica primária, segmentos e regra de decisão.
- [ ] Registrar o que seria um resultado negativo ou inconclusivo.

## Gate 1 — dados

- [ ] Validar hashes, chaves, datas, nulos e duplicatas das fontes herdadas.
- [ ] Criar tabela cliente-data sem usar informação futura.
- [ ] Congelar splits temporais, incluindo janela intocada de monitoramento.
- [ ] Implementar gerador determinístico do piloto sintético.
- [ ] Marcar tratamento, resposta e desfecho como sintéticos em dados e metadados.
- [ ] Testar randomização, positividade e reprodução pela seed.
- [ ] Completar o data card e o manifesto de derivados.

## Gate 2 — modelos

- [ ] Implementar e testar a regra de negócio.
- [ ] Treinar regressão logística dentro de uma pipeline.
- [ ] Treinar XGBoost sem ajustar no teste final.
- [ ] Calibrar e comparar probabilidades de churn.
- [ ] Implementar um único estimador simples de efeito incremental.
- [ ] Registrar parâmetros, versão dos dados e artefatos no MLflow.

## Gate 3 — políticas sob capacidade

- [ ] Implementar política aleatória com seed.
- [ ] Implementar política pela regra de negócio.
- [ ] Implementar política pelo risco de churn.
- [ ] Implementar política pelo efeito incremental esperado.
- [ ] Garantir a mesma elegibilidade, período e capacidade em todas as políticas.
- [ ] Testar empates, capacidade zero, capacidade máxima e dados ausentes.

## Gate 4 — avaliação

- [ ] Calcular PR-AUC, recall no Top-K e calibração.
- [ ] Estimar efeito principal com intervalo de confiança.
- [ ] Calcular ganho incremental e valor líquido das políticas.
- [ ] Avaliar pelo menos dois segmentos pré-declarados.
- [ ] Fazer análise manual dos erros mais caros.
- [ ] Executar análise de sensibilidade sem escolher retrospectivamente o cenário vencedor.
- [ ] Registrar resultados negativos e violações de premissas.

## Gate 5 — monitoramento e ciclo de vida

- [ ] Definir métricas e limites antes de abrir a janela de monitoramento.
- [ ] Medir qualidade, drift de dados, calibração e valor da política.
- [ ] Definir critérios de champion/challenger.
- [ ] Simular um gatilho de retreinamento.
- [ ] Simular promoção e rollback com logs e versões recuperáveis.
- [ ] Confirmar que rollback não altera dados ou resultados históricos.

## Gate 6 — entrega e defesa

- [ ] Reconciliar código, testes, MLflow, tabelas, gráficos e relatório.
- [ ] Preencher README.md e README.en.md apenas com resultados executados.
- [ ] Declarar dados sintéticos em resumo, método, resultados e limitações.
- [ ] Completar e ensaiar a apresentação em inglês.
- [ ] Preparar respostas sobre risco versus efeito, causalidade e validade externa.
- [ ] Executar tudo em ambiente limpo e registrar o comando final.

