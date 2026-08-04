<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 115 — Avaliação e publicação — 08/01/2027
> [!abstract] Resultado concreto do dia
> Concluir **Avaliação e publicação** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Avaliação e publicação.
- **Pasta/arquivo principal:** `semana-23/dia-115-avaliacao-e-publicacao/` (pasta do projeto).
- **Dados:** `documentos_suporte/` e conjunto de perguntas criado conforme o roteiro.

### Passo a passo completo
1. [ ] Execute avaliação completa das 30 perguntas e registre métricas de recuperação e geração.
2. [ ] Crie interface demonstrável com pergunta, resposta, fontes e feedback.
3. [ ] Adicione logs e tratamento de erro sem expor conteúdo sensível.
4. [ ] Empacote com Docker ou instrução reproduzível.
5. [ ] Publique relatório de limitações, riscos, custo e próximos passos.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Adicione um documento ou pergunta difícil ao conjunto de **Avaliação e publicação** e verifique recuperação, resposta e rastreabilidade da fonte.
- [ ] Altere uma configuração de chunking ou busca e compare as versões com o mesmo conjunto de perguntas.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. O que reduz respostas sem apoio em uma solução de **Avaliação e publicação**?

- [ ] A) Recuperar trechos relevantes e exigir que a resposta se baseie neles com indicação das fontes.
- [ ] B) Pedir ao modelo para inventar detalhes quando faltar contexto.
- [ ] C) Enviar documentos aleatórios para aumentar o volume.
- [ ] D) Remover referências para deixar a resposta menor.
- [ ] E) Usar somente o conhecimento geral do modelo.

2. Qual escolha afeta diretamente a recuperação em **Avaliação e publicação**?

- [ ] A) A ordem alfabética dos nomes dos arquivos apenas.
- [ ] B) A quantidade de parágrafos da resposta final.
- [ ] C) O nome da variável que armazena o índice.
- [ ] D) O tamanho e a sobreposição dos chunks, os metadados e a forma de representar e consultar os documentos.
- [ ] E) A cor da interface usada para enviar a pergunta.

3. Como o sistema deve agir quando **Avaliação e publicação** não encontra evidência suficiente?

- [ ] A) Repetir a mesma afirmação com mais confiança.
- [ ] B) Informar a limitação, evitar afirmar algo sem fonte e permitir reformular ou encaminhar a consulta.
- [ ] C) Completar a resposta com uma suposição plausível.
- [ ] D) Citar qualquer trecho recuperado, mesmo sem relação.
- [ ] E) Ocultar que a busca não encontrou conteúdo.

4. Qual avaliação ajuda a diagnosticar uma falha em **Avaliação e publicação**?

- [ ] A) Avaliar apenas o tamanho da resposta.
- [ ] B) Medir somente a velocidade de criação do índice.
- [ ] C) Considerar toda citação como necessariamente relevante.
- [ ] D) Trocar o modelo sem examinar os documentos recuperados.
- [ ] E) Medir separadamente se a busca encontrou o conteúdo certo e se a geração o utilizou corretamente.

5. Ordene o fluxo principal de uma solução de **Avaliação e publicação**.

- A) Gerar representações e construir o índice.
- B) Gerar uma resposta fundamentada e apresentar as fontes.
- C) Coletar e validar documentos e metadados.
- D) Recuperar trechos relevantes para a pergunta.
- E) Dividir o conteúdo em trechos adequados.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene o diagnóstico de uma resposta ruim em **Avaliação e publicação**.

- A) Registrar a pergunta, a resposta e as fontes recuperadas.
- B) Avaliar chunking, metadados, consulta e ranking da busca.
- C) Corrigir a etapa responsável e repetir os mesmos testes.
- D) Avaliar se a geração respeitou o contexto recuperado.
- E) Verificar se a informação necessária existe nos documentos.

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
> - [ ] **Ângulo sugerido:** mostrar recuperação de fontes, avaliação, política de recusa e exemplos de falhas corrigidas.

> [!project] Projeto semanal — Assistente RAG para suporte técnico
> **Desafio:** Criar uma aplicação que consulte documentos, recupere evidências e responda com fontes ou recusa segura.
>
> **Deve reutilizar:** Dados, software, LLMs, embeddings e avaliação.
>
> **Entregáveis obrigatórios:**
> - [ ] pipeline de ingestão;
> - [ ] índice e recuperação;
> - [ ] respostas com fontes;
> - [ ] avaliação de 30 perguntas;
> - [ ] API/interface e diagrama;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Seu RAG encontra evidências corretas e sabe recusar quando os documentos não sustentam a resposta?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Avaliação e publicação.
- **Competência sugerida:** IA Generativa e RAG.
- **Ação recomendada:** Após concluir todas as atividades do dia, atualize o título profissional e adicione ou reforce **IA Generativa e RAG** na seção Competências. Se a entrega estiver revisada e apresentável, inclua-a também em Projetos ou Destaques.
- **Novo título sugerido:** `Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa`.
- **Próximo marco do perfil:** Dia 130 — revisão final do título, Sobre, Competências, Projetos e Destaques.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação
