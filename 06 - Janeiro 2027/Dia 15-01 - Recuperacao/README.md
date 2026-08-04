<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 113 — Recuperação — 06/01/2027
> [!abstract] Resultado concreto do dia
> Concluir **Recuperação** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Recuperação.
- **Pasta/arquivo principal:** `01-exercicios/dia-113-recuperacao.py`.
- **Dados:** `documentos_suporte/` e conjunto de perguntas criado conforme o roteiro.

### Passo a passo completo
1. [ ] Crie índice vetorial e função `retrieve(query, k)`.
2. [ ] Teste valores de k=1,3,5,10 e diferentes limiares.
3. [ ] Implemente filtro por metadados e, se possível, busca híbrida.
4. [ ] Calcule métricas de recuperação nas 30 perguntas.
5. [ ] Faça análise de 10 erros e ajuste chunking ou consulta.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-113-recuperacao.py`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-113-recuperacao.py`:** Execute retrieve('luz LOS vermelha', k=1,3,5) e registre posição do documento correto em cada execução.
- [ ] **Em `01-exercicios/dia-113-recuperacao.py`:** Aplique filtro de metadados para versão 1.0 e teste uma versão inexistente sem retornar documentos indevidos.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Crie índice vetorial e função `retrieve(query, k)`.

   **Pergunta:** O que reduz respostas sem apoio em uma solução de **Recuperação**?

- [ ] A) Remover referências para deixar a resposta menor.
- [ ] B) Usar somente o conhecimento geral do modelo.
- [ ] C) Recuperar trechos relevantes e exigir que a resposta se baseie neles com indicação das fontes.
- [ ] D) Pedir ao modelo para inventar detalhes quando faltar contexto.
- [ ] E) Enviar documentos aleatórios para aumentar o volume.

2. **Referência — atividade 2:** Teste valores de k=1,3,5,10 e diferentes limiares.

   **Pergunta:** Qual escolha afeta diretamente a recuperação em **Recuperação**?

- [ ] A) O tamanho e a sobreposição dos chunks, os metadados e a forma de representar e consultar os documentos.
- [ ] B) A cor da interface usada para enviar a pergunta.
- [ ] C) A ordem alfabética dos nomes dos arquivos apenas.
- [ ] D) A quantidade de parágrafos da resposta final.
- [ ] E) O nome da variável que armazena o índice.

3. **Referência — atividade 3:** Implemente filtro por metadados e, se possível, busca híbrida.

   **Pergunta:** Como o sistema deve agir quando **Recuperação** não encontra evidência suficiente?

- [ ] A) Citar qualquer trecho recuperado, mesmo sem relação.
- [ ] B) Ocultar que a busca não encontrou conteúdo.
- [ ] C) Repetir a mesma afirmação com mais confiança.
- [ ] D) Informar a limitação, evitar afirmar algo sem fonte e permitir reformular ou encaminhar a consulta.
- [ ] E) Completar a resposta com uma suposição plausível.

4. **Referência — atividade 4:** Calcule métricas de recuperação nas 30 perguntas.

   **Pergunta:** Qual avaliação ajuda a diagnosticar uma falha em **Recuperação**?

- [ ] A) Trocar o modelo sem examinar os documentos recuperados.
- [ ] B) Medir separadamente se a busca encontrou o conteúdo certo e se a geração o utilizou corretamente.
- [ ] C) Avaliar apenas o tamanho da resposta.
- [ ] D) Medir somente a velocidade de criação do índice.
- [ ] E) Considerar toda citação como necessariamente relevante.

5. **Referência — atividade 5:** Faça análise de 10 erros e ajuste chunking ou consulta.

   **Pergunta:** Ordene o fluxo principal de uma solução de **Recuperação**.

- A) Gerar representações e construir o índice.
- B) Gerar uma resposta fundamentada e apresentar as fontes.
- C) Coletar e validar documentos e metadados.
- D) Recuperar trechos relevantes para a pergunta.
- E) Dividir o conteúdo em trechos adequados.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene o diagnóstico de uma resposta ruim em **Recuperação**.

- A) Avaliar chunking, metadados, consulta e ranking da busca.
- B) Corrigir a etapa responsável e repetir os mesmos testes.
- C) Registrar a pergunta, a resposta e as fontes recuperadas.
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

- **Conhecimento praticado hoje:** Recuperação.
- **Competência sugerida:** Recuperação de informação e busca vetorial.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Recuperação de informação e busca vetorial** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
