<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 82 — Dados e cohorts — 24/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **Dados e cohorts** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Dados e cohorts.
- **Pasta/arquivo principal:** `semana-17/dia-082-dados-e-cohorts.ipynb`.
- **Dados:** `dados/credito.csv`.

### Passo a passo completo
1. [ ] Carregue `credito.csv`, faça qualidade e EDA da taxa de default.
2. [ ] Crie cohorts por mês de concessão e acompanhe default P1/P2/P3 quando possível.
3. [ ] Analise default por faixas de renda, dívida, atrasos e tempo de emprego.
4. [ ] Valide estabilidade temporal das variáveis.
5. [ ] Crie dicionário de features e regras de exclusão.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Avalie **Dados e cohorts** em uma janela temporal ou horizonte adicional, mantendo a ordem das datas.
- [ ] Crie um teste de estresse com mudança de regime, período ausente ou custo maior e registre se a conclusão permanece útil.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Qual definição é essencial antes de modelar **Dados e cohorts**?

- [ ] A) Usar dados posteriores ao evento para completar o cadastro.
- [ ] B) Remover todos os casos sem histórico longo.
- [ ] C) Definir risco apenas como uma pontuação alta do modelo.
- [ ] D) Estabelecer o evento de risco, o horizonte, a população e a data-limite das informações permitidas.
- [ ] E) Escolher o algoritmo antes de definir o evento.

2. Por que a calibração importa em uma aplicação de **Dados e cohorts**?

- [ ] A) Porque substitui a validação temporal.
- [ ] B) Porque a probabilidade estimada precisa representar uma frequência útil para políticas baseadas em custo e risco.
- [ ] C) Porque transforma qualquer modelo no mais preciso.
- [ ] D) Porque elimina diferenças entre grupos.
- [ ] E) Porque permite ignorar a taxa-base do evento.

3. Qual cuidado de governança é necessário em **Dados e cohorts**?

- [ ] A) Ocultar as variáveis para impedir questionamentos.
- [ ] B) Avaliar somente o grupo mais numeroso.
- [ ] C) Usar atributos sensíveis sem analisar consequências.
- [ ] D) Manter a política fixa mesmo quando os dados mudarem.
- [ ] E) Documentar dados, critérios, limitações e desempenho por segmento, com revisão de possíveis impactos injustos.

4. Como transformar uma pontuação de **Dados e cohorts** em política?

- [ ] A) Escolher o corte que aprova o menor número de pessoas.
- [ ] B) Ignorar o custo de erros porque a probabilidade já resume tudo.
- [ ] C) Definir faixas e ações segundo perdas, capacidade, restrições e acompanhamento posterior.
- [ ] D) Aplicar automaticamente a mesma decisão a toda pontuação positiva.
- [ ] E) Usar 50% como corte obrigatório.

5. Ordene o desenvolvimento de um modelo para **Dados e cohorts**.

- A) Separar períodos e treinar um baseline.
- B) Construir dados disponíveis até a data de decisão.
- C) Definir evento, horizonte, população e restrições.
- D) Avaliar discriminação, calibração e desempenho por segmento.
- E) Documentar limites e propor uma política de uso.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene a criação de uma política baseada em **Dados e cohorts**.

- A) Escolher regras compatíveis com risco e operação.
- B) Simular faixas de pontuação e decisões possíveis.
- C) Definir custos, benefícios, capacidade e restrições.
- D) Monitorar impacto, estabilidade e diferenças entre grupos.
- E) Aplicar a política com controles e rastreabilidade.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Dados e cohorts.
- **Competência sugerida:** Cohorts e análise de risco.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Cohorts e análise de risco** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação
