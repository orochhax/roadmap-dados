<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 77 — Baselines temporais — 17/11/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Baselines temporais.
- **Competência sugerida:** Baselines de forecasting.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Baselines de forecasting** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Baselines temporais** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Baselines temporais.
- **Pasta/arquivo principal:** `01-exercicios/dia-077-baselines-temporais.ipynb`.
- **Dados:** `dados/energia.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Implemente baselines: último valor, média móvel de 7 dias, média do mesmo dia da semana e média sazonal.
2. [ ] Use validação walk-forward em pelo menos três janelas.
3. [ ] Calcule MAE, RMSE e MAPE/SMAPE quando adequado.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Compare desempenho por períodos de alta e baixa demanda.
- [ ] Escolha baseline oficial que qualquer modelo deve superar.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-077-baselines-temporais.ipynb`:** Compare horizonte de 7 e 14 dias nas mesmas três janelas walk-forward e registre MAE por horizonte.
- [ ] **Em `01-exercicios/dia-077-baselines-temporais.ipynb`:** Avalie o baseline oficial separadamente em dias úteis e fins de semana.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Por que um baseline simples é importante em **Baselines temporais**?

- [ ] A) Porque substitui a definição do horizonte de previsão.
- [ ] B) Porque mostra se o modelo supera regras como repetir o último valor ou a sazonalidade anterior.
- [ ] C) Porque elimina a necessidade de avaliar modelos mais complexos.
- [ ] D) Porque sempre será o modelo usado em produção.
- [ ] E) Porque garante que não existam valores ausentes.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual cuidado evita informação do futuro em variáveis de **Baselines temporais**?

- [ ] A) Centralizar médias móveis com dados anteriores e posteriores.
- [ ] B) Preencher períodos passados com valores observados no futuro.
- [ ] C) Usar a série completa para ajustar cada transformação.
- [ ] D) Ordenar por valor em vez de ordenar por data.
- [ ] E) Calcular defasagens e médias móveis usando somente observações disponíveis antes de cada previsão.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de previsão para **Baselines temporais**.

- A) Criar baselines e variáveis usando apenas o passado.
- B) Ordenar a série e verificar falhas, datas e mudanças de regime.
- C) Comparar erros, comunicar incerteza e definir o uso da previsão.
- D) Validar com divisões temporais sucessivas.
- E) Definir frequência, horizonte e decisão atendida.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`
