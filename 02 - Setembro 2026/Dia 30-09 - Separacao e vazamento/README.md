<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 42 — Separação e vazamento — 29/09/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Separação e vazamento.
- **Competência sugerida:** Separação de dados e prevenção de vazamento.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Separação de dados e prevenção de vazamento** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

> [!abstract] Resultado concreto do dia
> Concluir **Separação e vazamento** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Separação e vazamento.
- **Pasta/arquivo principal:** `01-exercicios/dia-042-separacao-e-vazamento.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Separe treino, validação e teste com proporção definida e compare a distribuição do alvo com e sem estratificação.
2. [ ] Classifique colunas como disponíveis no momento da previsão ou como vazamento, justificando o momento em que surgem.
3. [ ] Desenhe um corte temporal simples e explique por que nenhum registro futuro pode participar do treino.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Crie as três features com leakage apenas como exemplo identificado, sem usá-las em um modelo ainda.
- [ ] A comparação de métricas com e sem leakage será feita após o primeiro baseline completo do Dia 45.
- [ ] Escreva um checklist curto de cinco perguntas, não dez.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] Após o Dia 45, treine uma versão com uma coluna vazada e outra sem ela para observar a inflação artificial da métrica.
- [ ] Compare split aleatório e temporal usando a mesma métrica e explique qual representa melhor o uso real.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma alternativa. Na questão 3, escreva a sequência correta usando A–E.

1. **Pergunta:** Qual coluna é um exemplo direto de vazamento ao prever churn futuro?

- [ ] A) Plano conhecido na data de previsão.
- [ ] B) Cidade cadastrada antes da previsão.
- [ ] C) Data de cancelamento registrada depois do evento.
- [ ] D) Mensalidade vigente na data de referência.
- [ ] E) Tempo de cliente calculado até a data de referência.

2. **Pergunta:** Em um problema temporal, qual conjunto deve conter as observações mais recentes?

- [ ] A) Treino.
- [ ] B) Dados descartados.
- [ ] C) Teste final.
- [ ] D) Todos ao mesmo tempo.
- [ ] E) Apenas dados sintéticos.

3. **Pergunta:** Ordene um fluxo seguro de separação.

- A) Congelar o conjunto de teste.
- B) Definir a data ou regra de corte.
- C) Treinar somente com o conjunto permitido.
- D) Identificar unidade, alvo e horizonte.
- E) Verificar proporções e datas dos conjuntos.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`
