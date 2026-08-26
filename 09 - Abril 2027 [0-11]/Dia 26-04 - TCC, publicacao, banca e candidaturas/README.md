# TCC — publicação, banca e candidaturas

**Data de estudo:** 26/04/2027
**Carga planejada:** 4 a 5 horas

## Entrega final

**Do risco de churn ao efeito incremental: priorização de campanhas de retenção em telecom sob restrição de capacidade**

Reproduza a release do [Telecom Customer Intelligence](<../../projetos/telecom-customer-intelligence/README.md>) em ambiente limpo. A entrega final precisa mostrar o que foi executado, o que falhou e o que dados sintéticos não permitem concluir.

## Atividades do dia

Pesquise exatamente:

- `reproducible machine learning project release checklist`
- `data science thesis defense machine learning questions`
- `model card synthetic data intended use limitations`
- `technical presentation churn causal experiment`
- `data science portfolio honest project claims`

Depois siga o guia e o roteiro disponíveis abaixo sem copiar respostas de banca.

### Conteúdo e atividades — TCC — release, banca e comunicação profissional

**Arquivos da atividade:** [abrir a pasta `01-tcc-release-banca-e-comunicacao`](<atividades/01-tcc-release-banca-e-comunicacao/>)

#### Objetivo

Congelar e publicar uma release reproduzível do TCC, defender escolhas técnicas e traduzir o trabalho para candidaturas sem transformar simulação em experiência profissional.

#### Conquista para o LinkedIn

- Revise Sobre, Competências, Projetos e Destaques somente com links e evidências verificadas.
- Adapte `[cargo ou área atual verdadeira] | Em formação em Ciência de Dados | [duas ou três competências comprovadas]` ao contexto registrado em [LinkedIn — perfil atual](<../../00 - Recursos Compartilhados/linkedin-perfil-atual.md>).
- Adicione competências apenas se os artefatos correspondentes estiverem executados e você conseguir defendê-los.
- **Comunicação técnica em inglês** exige apresentação e respostas próprias, não apenas um template preenchido.
- Use o [Guia de LinkedIn e evidências](<../../00 - Recursos Compartilhados/linkedin-e-evidencias.md>).

#### Arquivos e dados

- **Enunciado local:** `atividades/01-tcc-release-banca-e-comunicacao/roteiro_tcc.md`.
- **Projeto canônico:** `projetos/telecom-customer-intelligence/`.
- **Entradas:** release candidata, dados sintéticos manifestados, relatório, runs MLflow, testes, materiais de banca e instruções.
- **Fallback:** vídeo ou capturas substituem hospedagem; execução em ambiente limpo continua obrigatória.

#### Pesquise exatamente

- `machine learning reproducibility clean environment release`
- `data science thesis defense model limitations`
- `portfolio project synthetic data disclosure`
- `technical presentation English machine learning project`
- `STAR method data science project interview`

#### O que fazer

- [ ] Execute o projeto em clone/pasta limpa usando somente o README.
- [ ] Reproduza dados, benchmark, piloto, testes, monitoramento e relatório sem etapa manual oculta.
- [ ] Crie release com versão, dependências, data card, model card, resultados e limitações.
- [ ] Faça defesa de 8–10 minutos e responda usando artefatos do escopo congelado.
- [ ] Atualize `README.en.md` com 150–250 palavras e resultados reais da própria execução.
- [ ] Prepare `docs/presentation-en.md` e grave apresentação em inglês de 2–3 minutos.
- [ ] Publique apenas depois de conferir links, ausência de dados pessoais/segredos e declaração sintética.
- [ ] Envie três candidaturas compatíveis, adaptando palavras-chave sem inventar experiência.

#### Fora do escopo

Não adicione controle sintético, nuvem nova, LLM, entity matching, forecasting ou aplicação grande para “valorizar” a entrega final.

#### Banco de perguntas de banca

1. Qual decisão, data de corte, horizonte e capacidade foram congelados?
2. Por que risco de churn não equivale a resposta à campanha?
3. Como você provou que não houve leakage temporal ou pós-tratamento?
4. Qual baseline foi mais difícil de superar e por quê?
5. Por que PR-AUC e recall@K são adequados à capacidade?
6. Como avaliou e usou calibração?
7. Como os dados sintéticos foram gerados e quais vieses isso introduz?
8. Como a randomização simulada sustenta o efeito por intenção de tratar?
9. O que significa um intervalo de confiança que cruza zero?
10. Como calculou ganho por 100 contatos e custo por retenção quando o efeito é incerto?
11. Quais slices não permitem conclusão por falta de amostra?
12. Como MLflow sustenta champion/challenger e reprodução?
13. Quais gatilhos iniciam retreino e rollback simulados?
14. Qual é a maior limitação e qual evidência permitiria contestar seu resultado?

#### Como validar

- Uma pessoa externa reproduz a release apenas com as instruções.
- A banca usa evidências e reconhece resultados negativos/inconclusivos.
- README PT/EN, relatório, MLflow e apresentação estão reconciliados.
- Publicação e candidaturas deixam claro o caráter educacional e sintético.

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

## Finalização

Antes de concluir, confirme:

- A release foi reproduzida e todos os testes obrigatórios passaram.
- A defesa liga cada afirmação a um artefato real e declara os limites sintéticos.
- README PT/EN, relatório e apresentações reconciliam os mesmos resultados, e candidaturas e LinkedIn descrevem projeto educacional sem inventar experiência.

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
