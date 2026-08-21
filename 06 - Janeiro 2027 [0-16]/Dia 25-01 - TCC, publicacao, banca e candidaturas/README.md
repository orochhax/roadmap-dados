# TCC — publicação, banca e candidaturas

**Data de estudo:** 25/01/2027  
**Carga planejada:** 4 a 5 horas

## Entrega final

**Do risco de churn ao efeito incremental: priorização de campanhas de retenção em telecom sob restrição de capacidade**

Reproduza a release do [Telecom Customer Intelligence](<../../projetos/telecom-customer-intelligence/README.md>) em ambiente limpo. A entrega final precisa mostrar o que foi executado, o que falhou e o que dados sintéticos não permitem concluir.

## Assuntos para pesquisar

Pesquise exatamente:

- `reproducible machine learning project release checklist`
- `data science thesis defense machine learning questions`
- `model card synthetic data intended use limitations`
- `technical presentation churn causal experiment`
- `data science portfolio honest project claims`

Depois siga o [guia e o roteiro](<modulos/01-e138/README.md>) sem copiar respostas de banca.

## Escopo da release

- contrato de decisão, horizonte e capacidade;
- dados sintéticos versionados e piloto randomizado explicitamente simulado;
- regra de negócio, regressão logística e XGBoost;
- métricas preditivas, causais, de custo e slices;
- MLflow, testes, monitoramento temporal, champion/challenger, retreino e rollback simulados;
- relatório, README em português/inglês e apresentação curta em inglês.

## Publicação da semana no LinkedIn

- **Tema específico:** release final do TCC — do ranking de risco ao efeito incremental de uma campanha de retenção simulada sob capacidade limitada.
- **Tipo:** entrega.
- **Formato:** post principal com carrossel do relatório, link do GitHub e demonstração curta.
- **Artefato/evidência exigida:** release reproduzida em ambiente limpo, dados sintéticos manifestados, regra/logística/XGBoost no mesmo protocolo, piloto randomizado simulado, PR-AUC, recall@K, calibração, efeito/IC, ganho por 100, custo por retenção, slices, testes, MLflow, monitoramento e rollback.

### Roteiro para preencher

- **Pergunta e usuário:** [qual decisão o TCC apoia e para quem?]
- **Contrato:** [data de decisão, horizonte, capacidade e custos]
- **Dados:** [versão, seed, período e declaração sintética]
- **Baseline e modelos:** [regra, logística e XGBoost sob o mesmo protocolo]
- **Piloto simulado:** [randomização, estimando, efeito e intervalo]
- **Resultado verificável:** [métricas preditivas, ganho por 100 e custo presentes nos artefatos]
- **Resultado negativo/limite:** [onde o método não venceu ou ficou inconclusivo]
- **Ciclo de vida:** [MLflow, teste, monitoramento, retreino e rollback]
- **Links:** [GitHub, relatório e demonstração conferidos]

### Limitação obrigatória

Declare que dados e piloto são sintéticos, que o projeto demonstra método e que não mede redução real de churn, economia real nem efeito causal em clientes de uma operadora.

### Cuidado contra afirmações falsas

Não apresente retenções simuladas como impacto profissional. Não esconda intervalo inconclusivo, slice fraco ou modelo que perdeu para a regra. Use somente números reconciliados. A publicação não autoriza inventar cargo, experiência, Competências ou nível de inglês.

### Checklist de publicação

- [ ] Reproduzi a release em clone ou pasta limpa usando somente o README.
- [ ] Reconciliei outputs, MLflow, relatório e texto da publicação.
- [ ] Diferenciei risco previsto de efeito incremental.
- [ ] Mantive dados/piloto/retreino/rollback identificados como simulações.
- [ ] Mostrei baseline, incerteza, resultado negativo e limitação.
- [ ] Conferi ausência de dados pessoais, segredos e links quebrados.
- [ ] Testei GitHub, relatório e demonstração em janela anônima.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Concluído quando

- [ ] A release foi reproduzida e todos os testes obrigatórios passaram.
- [ ] A defesa liga cada afirmação a um artefato real e declara os limites sintéticos.
- [ ] README PT/EN, relatório e apresentações reconciliam os mesmos resultados, e candidaturas e LinkedIn descrevem projeto educacional sem inventar experiência.
