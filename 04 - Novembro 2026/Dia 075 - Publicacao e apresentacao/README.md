<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 75 — Publicação e apresentação — 13/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **Publicação e apresentação** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Publicação e apresentação.
- **Pasta/arquivo principal:** `semana-15/dia-075-publicacao-e-apresentacao/` (pasta do projeto).
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Limpe o repositório, fixe dependências e rode tudo em ambiente novo.
2. [ ] Crie README com instalação, estrutura, resultados e decisões.
3. [ ] Publique release e grave demo de 8–10 minutos.
4. [ ] Responda por escrito a cinco perguntas de banca sobre leakage, métrica, custo, viés e implantação.
5. [ ] Faça retrospectiva: três acertos, três falhas e três melhorias.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Crie um recorte adicional por segmento de cliente e compare métricas, erros ou recomendações de **Publicação e apresentação**.
- [ ] Faça uma análise de sensibilidade alterando uma regra, custo ou limiar e registre se a ação recomendada muda.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Ao desenvolver **Publicação e apresentação**, qual definição evita um alvo ambíguo ou vazamento de dados?

- [ ] A) Fixar a população, a data de referência, a janela de observação e a regra objetiva de churn.
- [ ] B) Chamar de churn qualquer cliente com poucos registros.
- [ ] C) Usar informações posteriores ao cancelamento para prever o próprio cancelamento.
- [ ] D) Alterar a definição do alvo para melhorar a métrica do modelo.
- [ ] E) Remover clientes ativos sem registrar o critério usado.

2. Como avaliar um modelo ligado a **Publicação e apresentação** para uma estratégia de retenção?

- [ ] A) Priorizando somente a acurácia geral.
- [ ] B) Contatando todos os clientes classificados pelo modelo.
- [ ] C) Ignorando a capacidade operacional da equipe de retenção.
- [ ] D) Relacionando métricas e limiar ao custo do contato, ao valor do cliente e ao benefício provável da retenção.
- [ ] E) Escolhendo sempre o limiar de 50%.

3. Qual análise ajuda a encontrar riscos escondidos em **Publicação e apresentação**?

- [ ] A) Conferir somente o desempenho no conjunto de treino.
- [ ] B) Comparar qualidade dos dados, erros e desempenho entre períodos e segmentos de clientes.
- [ ] C) Avaliar apenas os clientes com maior probabilidade.
- [ ] D) Excluir segmentos pequenos antes de medir os erros.
- [ ] E) Usar a mesma explicação para todos os perfis.

4. Qual é a melhor ligação entre um modelo de **Publicação e apresentação** e uma ação de negócio?

- [ ] A) Enviar a probabilidade bruta sem orientar seu uso.
- [ ] B) Considerar todo cliente de alto risco automaticamente perdido.
- [ ] C) Escolher a ação apenas pela variável mais importante do modelo.
- [ ] D) Medir sucesso somente pelo número de contatos realizados.
- [ ] E) Criar uma política explícita que defina quem será priorizado, qual ação receberá e como o impacto será medido.

5. Ordene a construção de um projeto relacionado a **Publicação e apresentação**.

- A) Transformar previsões em estratégia e comunicar limitações.
- B) Construir e auditar dados disponíveis até a data de referência.
- C) Realizar EDA e preparar uma separação sem vazamento.
- D) Treinar baselines e modelos com métricas adequadas.
- E) Definir população, churn, datas e objetivo de negócio.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene a criação de uma política de retenção baseada em **Publicação e apresentação**.

- A) Medir retenção incremental e ajustar a política.
- B) Definir segmentos e ações possíveis para cada perfil.
- C) Escolher limiares com base em custo e benefício.
- D) Executar a ação em um grupo controlado.
- E) Estimar valor, risco, custo de contato e capacidade operacional.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

> [!todo] PUBLICAR NO LINKEDIN — projeto prioritário do portfólio
> - [ ] Publique somente após README, resultados e limitações estarem revisados.
> - [ ] Inclua problema, abordagem, principal evidência, decisão e link do GitHub.
> - [ ] **Ângulo sugerido:** publicar o case completo, do dado à API/dashboard, com impacto, limitações e vídeo curto.

> [!project] Projeto semanal — Churn: publicação e defesa técnica
> **Desafio:** Finalizar o projeto de churn como peça de portfólio e defendê-lo como em uma entrevista.
>
> **Deve reutilizar:** Todo o conteúdo acumulado até a semana 15.
>
> **Entregáveis obrigatórios:**
> - [ ] release no GitHub;
> - [ ] README executivo e técnico;
> - [ ] dashboard ou API;
> - [ ] vídeo de 8–10 minutos;
> - [ ] lista de perguntas críticas respondidas;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Seu projeto mostra impacto de negócio, domínio técnico e comunicação — ou parece apenas um notebook de curso?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Publicação e apresentação.
- **Competência sugerida:** Apresentação de projetos de Ciência de Dados.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Apresentação de projetos de Ciência de Dados** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação
