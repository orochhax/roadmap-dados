# Calendário de entregas reais

As sessões ensinam conceitos; estas entregas provam que você consegue conectá-los. Um mesmo produto evolui em várias versões para evitar muitos projetos pequenos e rasos.

| Data | Produto e versão | Decisão que precisa ficar demonstrável |
|---|---|---|
| 31/08/2026 | Telecom Customer Intelligence — fundação | Ingerir arquivos, validar entradas e produzir resumo operacional reproduzível. |
| 30/09/2026 | Telecom Customer Intelligence — Product Analytics | Explicar funil, cohorts, churn, receita e reclamações com SQL, Python e dashboard reconciliados. |
| 08/10/2026 | Telecom Customer Intelligence — impacto causal | Separar associação de causalidade e decidir se as premissas sustentam o efeito estimado. |
| 28/10/2026 | Telecom Customer Intelligence — benchmark de retenção | Escolher regra ou modelo com base em PR-AUC, recall no Top-K, calibração, custo e slices. |
| 12/11/2026 | Telecom Customer Intelligence — operação de churn | Transformar score, segmentos e explicabilidade em política de retenção com capacidade limitada. |
| 18/11/2026 | Intelligent Support Operations — triagem visual | Comparar baseline e PyTorch e encaminhar baixa confiança para revisão humana. |
| 25/11/2026 | Energy ForecastOps | Escolher previsão por horizonte com backtest e custo de subprevisão. |
| 18/12/2026 | Telecom Customer Intelligence — Data Engineering e MLOps | Reproduzir pipeline, serviço, monitoramento, retreino, champion/challenger e rollback. |
| 30/12/2026 | Entity Matching Lab | Comparar regras, fuzzy, TF-IDF, embeddings e ranking por qualidade, latência e custo. |
| 06/01/2027 | Intelligent Support Operations — RAG | Responder com fontes, recusar sem evidência e demonstrar resultado no conjunto fixo de avaliação. |
| 12/01/2027 | Produto integrador | Demonstrar dados, baseline, modelo, interface, testes, decisão e retrospectiva em um fluxo único. |
| 25/01/2027 | Telecom Customer Intelligence — TCC | Defender uma política de retenção sob capacidade limitada, distinguindo risco de churn de efeito incremental simulado e demonstrando custo, estabilidade, monitoramento e limitações. |

## Contrato de cada entrega

Toda entrega precisa conter:

1. problema, usuário e decisão;
2. data card com origem, licença, período, campos, limitações e hash;
3. dados brutos preservados e processamento reproduzível;
4. baseline implementado antes do método avançado;
5. métricas e regra de decisão definidas antes de observar o resultado;
6. análise de erros e segmentos relevantes;
7. testes automatizados e caso de borda;
8. comando único ou sequência curta para reprodução;
9. README em português e inglês;
10. apresentação de 2–3 minutos em inglês;
11. conclusão honesta quando o método avançado perder para o baseline.

No portfólio público, destaque somente os quatro produtos mais fortes. Todas as entregas continuam obrigatórias para aprendizado.
