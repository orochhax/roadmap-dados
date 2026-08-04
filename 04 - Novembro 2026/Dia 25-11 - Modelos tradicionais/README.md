<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 78 — Modelos tradicionais — 18/11/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Modelos tradicionais.
- **Competência sugerida:** Modelos de séries temporais.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Modelos de séries temporais** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Modelos tradicionais** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Modelos tradicionais.
- **Pasta/arquivo principal:** `01-exercicios/dia-078-modelos-tradicionais.ipynb`.
- **Dados:** `dados/energia.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Treine regressão linear com lags, árvore/Random Forest e modelo estatístico simples como Holt-Winters ou ARIMA, se disponível.
2. [ ] Garanta que features sejam criadas respeitando tempo.
3. [ ] Faça backtesting com múltiplos cortes.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Compare erro e estabilidade por horizonte.
- [ ] Analise resíduos e autocorrelação remanescente.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-078-modelos-tradicionais.ipynb`:** Adicione um quarto corte ao backtesting e compare a estabilidade de Random Forest e Holt-Winters.
- [ ] **Em `01-exercicios/dia-078-modelos-tradicionais.ipynb`:** Meça autocorrelação dos resíduos nos lags 1 e 7 e registre qual padrão ainda não foi capturado.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Por que um baseline simples é importante em **Modelos tradicionais**?

- [ ] A) Porque mostra se o modelo supera regras como repetir o último valor ou a sazonalidade anterior.
- [ ] B) Porque elimina a necessidade de avaliar modelos mais complexos.
- [ ] C) Porque sempre será o modelo usado em produção.
- [ ] D) Porque garante que não existam valores ausentes.
- [ ] E) Porque substitui a definição do horizonte de previsão.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual cuidado evita informação do futuro em variáveis de **Modelos tradicionais**?

- [ ] A) Preencher períodos passados com valores observados no futuro.
- [ ] B) Usar a série completa para ajustar cada transformação.
- [ ] C) Ordenar por valor em vez de ordenar por data.
- [ ] D) Calcular defasagens e médias móveis usando somente observações disponíveis antes de cada previsão.
- [ ] E) Centralizar médias móveis com dados anteriores e posteriores.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de previsão para **Modelos tradicionais**.

- A) Definir frequência, horizonte e decisão atendida.
- B) Criar baselines e variáveis usando apenas o passado.
- C) Ordenar a série e verificar falhas, datas e mudanças de regime.
- D) Validar com divisões temporais sucessivas.
- E) Comparar erros, comunicar incerteza e definir o uso da previsão.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`
