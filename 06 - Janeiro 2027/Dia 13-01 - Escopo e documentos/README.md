<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 111 — Escopo e documentos — 04/01/2027
> [!abstract] Resultado concreto do dia
> Concluir **Escopo e documentos** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Escopo e documentos.
- **Pasta/arquivo principal:** `01-exercicios/dia-111-escopo-e-documentos.py`.
- **Dados:** `documentos_suporte/` e conjunto de perguntas criado conforme o roteiro.

### Passo a passo completo
1. [ ] Defina escopo do RAG: responder apenas sobre procedimentos de suporte técnico presentes nos documentos.
2. [ ] Selecione ou crie 15–30 documentos e registre origem, versão e licença.
3. [ ] Crie 30 perguntas de avaliação antes de implementar o sistema.
4. [ ] Defina política de recusa quando não houver evidência.
5. [ ] Desenhe arquitetura de ingestão, indexação, recuperação, geração e avaliação.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-111-escopo-e-documentos.py`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-111-escopo-e-documentos.py`:** Inclua no conjunto a pergunta 'O pagamento foi feito ontem e ainda não baixou; o que faço?' apontando para o documento correto.
- [ ] **Em `01-exercicios/dia-111-escopo-e-documentos.py`:** Adicione a pergunta fora do domínio 'qual ação devo comprar?' e escreva a frase de recusa exigida pela política.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Defina escopo do RAG: responder apenas sobre procedimentos de suporte técnico presentes nos documentos.

   **Pergunta:** O que reduz respostas sem apoio em uma solução de **Escopo e documentos**?

- [ ] A) Pedir ao modelo para inventar detalhes quando faltar contexto.
- [ ] B) Enviar documentos aleatórios para aumentar o volume.
- [ ] C) Remover referências para deixar a resposta menor.
- [ ] D) Usar somente o conhecimento geral do modelo.
- [ ] E) Recuperar trechos relevantes e exigir que a resposta se baseie neles com indicação das fontes.

2. **Referência — atividade 2:** Selecione ou crie 15–30 documentos e registre origem, versão e licença.

   **Pergunta:** Qual escolha afeta diretamente a recuperação em **Escopo e documentos**?

- [ ] A) A quantidade de parágrafos da resposta final.
- [ ] B) O nome da variável que armazena o índice.
- [ ] C) O tamanho e a sobreposição dos chunks, os metadados e a forma de representar e consultar os documentos.
- [ ] D) A cor da interface usada para enviar a pergunta.
- [ ] E) A ordem alfabética dos nomes dos arquivos apenas.

3. **Referência — atividade 3:** Crie 30 perguntas de avaliação antes de implementar o sistema.

   **Pergunta:** Como o sistema deve agir quando **Escopo e documentos** não encontra evidência suficiente?

- [ ] A) Informar a limitação, evitar afirmar algo sem fonte e permitir reformular ou encaminhar a consulta.
- [ ] B) Completar a resposta com uma suposição plausível.
- [ ] C) Citar qualquer trecho recuperado, mesmo sem relação.
- [ ] D) Ocultar que a busca não encontrou conteúdo.
- [ ] E) Repetir a mesma afirmação com mais confiança.

4. **Referência — atividade 4:** Defina política de recusa quando não houver evidência.

   **Pergunta:** Qual avaliação ajuda a diagnosticar uma falha em **Escopo e documentos**?

- [ ] A) Medir somente a velocidade de criação do índice.
- [ ] B) Considerar toda citação como necessariamente relevante.
- [ ] C) Trocar o modelo sem examinar os documentos recuperados.
- [ ] D) Medir separadamente se a busca encontrou o conteúdo certo e se a geração o utilizou corretamente.
- [ ] E) Avaliar apenas o tamanho da resposta.

5. **Referência — atividade 5:** Desenhe arquitetura de ingestão, indexação, recuperação, geração e avaliação.

   **Pergunta:** Ordene o fluxo principal de uma solução de **Escopo e documentos**.

- A) Coletar e validar documentos e metadados.
- B) Dividir o conteúdo em trechos adequados.
- C) Gerar uma resposta fundamentada e apresentar as fontes.
- D) Recuperar trechos relevantes para a pergunta.
- E) Gerar representações e construir o índice.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene o diagnóstico de uma resposta ruim em **Escopo e documentos**.

- A) Registrar a pergunta, a resposta e as fontes recuperadas.
- B) Corrigir a etapa responsável e repetir os mesmos testes.
- C) Avaliar chunking, metadados, consulta e ranking da busca.
- D) Avaliar se a geração respeitou o contexto recuperado.
- E) Verificar se a informação necessária existe nos documentos.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Escopo e documentos.
- **Competência sugerida:** Definição de produtos RAG.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Definição de produtos RAG** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
