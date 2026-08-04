<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 113 — Recuperação — 06/01/2027

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Recuperação.
- **Competência sugerida:** Recuperação de informação e busca vetorial.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Recuperação de informação e busca vetorial** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Recuperação** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.
- **Gate da fase:** se Python, SQL, estatística ou ML estiver abaixo de 3/5, troque este dia por reforço da lacuna; LLM/RAG pode ser retomado depois.

### Preparação
- **Assunto central:** Recuperação.
- **Pasta/arquivo principal:** `01-exercicios/dia-113-recuperacao.py`.
- **Dados:** `documentos_suporte/` e conjunto de perguntas criado conforme o roteiro.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Crie índice vetorial e função `retrieve(query, k)`.
2. [ ] Teste valores de k=1,3,5,10 e diferentes limiares.
3. [ ] Implemente filtro por metadados e, se possível, busca híbrida.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Calcule métricas de recuperação nas 30 perguntas.
- [ ] Faça análise de 10 erros e ajuste chunking ou consulta.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-113-recuperacao.py`:** Execute retrieve('luz LOS vermelha', k=1,3,5) e registre posição do documento correto em cada execução.
- [ ] **Em `01-exercicios/dia-113-recuperacao.py`:** Aplique filtro de metadados para versão 1.0 e teste uma versão inexistente sem retornar documentos indevidos.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual escolha afeta diretamente a recuperação em **Recuperação**?

- [ ] A) O tamanho e a sobreposição dos chunks, os metadados e a forma de representar e consultar os documentos.
- [ ] B) A cor da interface usada para enviar a pergunta.
- [ ] C) A ordem alfabética dos nomes dos arquivos apenas.
- [ ] D) A quantidade de parágrafos da resposta final.
- [ ] E) O nome da variável que armazena o índice.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Como o sistema deve agir quando **Recuperação** não encontra evidência suficiente?

- [ ] A) Citar qualquer trecho recuperado, mesmo sem relação.
- [ ] B) Ocultar que a busca não encontrou conteúdo.
- [ ] C) Repetir a mesma afirmação com mais confiança.
- [ ] D) Informar a limitação, evitar afirmar algo sem fonte e permitir reformular ou encaminhar a consulta.
- [ ] E) Completar a resposta com uma suposição plausível.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene o fluxo principal de uma solução de **Recuperação**.

- A) Gerar representações e construir o índice.
- B) Gerar uma resposta fundamentada e apresentar as fontes.
- C) Coletar e validar documentos e metadados.
- D) Recuperar trechos relevantes para a pergunta.
- E) Dividir o conteúdo em trechos adequados.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`
