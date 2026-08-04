<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 8 — Exceções e validação — 12/08/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Exceções e validação.
- **Competência sugerida:** Tratamento de exceções e validação.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Tratamento de exceções e validação** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software`.
- **Próximo marco do perfil:** Dia 10 — Engenharia de Software | Python.

> [!abstract] Resultado concreto do dia
> Concluir **Exceções e validação** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Exceções e validação.
- **Pasta/arquivo principal:** `01-exercicios/dia-008-excecoes-e-validacao.py`.
- **Dados:** Dados pequenos definidos nos próprios exercícios e arquivos criados por você.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Use uma cópia pequena do CSV com quatro erros diferentes e implemente `validar_linha()` para retornar os problemas encontrados.
2. [ ] Aplique `try/except` somente nas conversões que podem falhar, sem envolver o programa inteiro.
3. [ ] Separe linhas válidas e rejeitadas sem interromper o processamento no primeiro erro.
4. [ ] Volte a `metricas_atendimento.py` do Dia 2 e trate divisão por zero e texto no lugar de número em um único programa integrado.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Grave os dois CSVs de saída apenas depois de validar corretamente a lista em memória.
- [ ] Amplie a tabela para oito casos se ainda houver dúvida sobre qual exceção ocorre em cada conversão.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-008-excecoes-e-validacao.py`:** Adicione uma linha com duracao_min=-10 ao arquivo de teste e faça validar_linha() registrar 'duração negativa' sem interromper as demais linhas.
- [ ] **Em `01-exercicios/dia-008-excecoes-e-validacao.py`:** Repita um mesmo id em duas linhas válidas e acrescente uma validação que envie a segunda ocorrência para dados_rejeitados.csv.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual prática reduz mais o risco de erro em um programa relacionado a **Exceções e validação**?

- [ ] A) Verificar os tipos e os limites das entradas antes de realizar os cálculos.
- [ ] B) Transformar todas as entradas em texto e calcular diretamente.
- [ ] C) Aceitar qualquer entrada e corrigir somente se o programa fechar.
- [ ] D) Remover mensagens de erro para deixar o terminal mais limpo.
- [ ] E) Repetir o mesmo cálculo em vários lugares do arquivo.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual teste fornece a verificação mais completa para um exercício de **Exceções e validação**?

- [ ] A) Conferir somente se o arquivo foi salvo com a extensão `.py`.
- [ ] B) Ler o código sem executá-lo porque a sintaxe parece correta.
- [ ] C) Trocar somente o nome das variáveis e comparar o tamanho do arquivo.
- [ ] D) Executar exemplos comuns, valores-limite e entradas inadequadas para observar comportamentos diferentes.
- [ ] E) Executar apenas o exemplo numérico apresentado no enunciado.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo seguro para resolver uma atividade de **Exceções e validação**.

- A) Ler o enunciado e identificar o objetivo.
- B) Definir as entradas, as regras e a saída necessária.
- C) Revisar o código e registrar o aprendizado.
- D) Executar testes com valores diferentes.
- E) Implementar a solução em pequenas etapas.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`
