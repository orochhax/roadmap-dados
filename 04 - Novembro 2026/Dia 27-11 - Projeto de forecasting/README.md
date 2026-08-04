<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 80 — Projeto de forecasting — 20/11/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Projeto de forecasting.
- **Competência sugerida:** Forecasting.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Forecasting** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Projeto de forecasting** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 4–5 horas; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Projeto de forecasting.
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/energia.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Organize o projeto com dados, notebook ou script, resultados e README.
2. [ ] Compare o baseline oficial com um único modelo em backtesting walk-forward.
3. [ ] Salve métricas em CSV e crie um gráfico de previsão com intervalo ou faixa de incerteza.
4. [ ] Produza resumo executivo de uma página com decisão, horizonte, risco e limitação.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Inclua modelos adicionais apenas se todos usarem exatamente os mesmos cortes temporais.
- [ ] Apresentação gravada e análises por muitos horizontes são desafios.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Execute o backtesting removendo o mês de maior consumo e registre como ranking de modelos e erro mudam.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Aumente em 25% o custo de subestimação no resumo executivo e confira se a decisão operacional permanece.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Por que um baseline simples é importante em **Projeto de forecasting**?

- [ ] A) Porque sempre será o modelo usado em produção.
- [ ] B) Porque garante que não existam valores ausentes.
- [ ] C) Porque substitui a definição do horizonte de previsão.
- [ ] D) Porque mostra se o modelo supera regras como repetir o último valor ou a sazonalidade anterior.
- [ ] E) Porque elimina a necessidade de avaliar modelos mais complexos.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual cuidado evita informação do futuro em variáveis de **Projeto de forecasting**?

- [ ] A) Ordenar por valor em vez de ordenar por data.
- [ ] B) Calcular defasagens e médias móveis usando somente observações disponíveis antes de cada previsão.
- [ ] C) Centralizar médias móveis com dados anteriores e posteriores.
- [ ] D) Preencher períodos passados com valores observados no futuro.
- [ ] E) Usar a série completa para ajustar cada transformação.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de previsão para **Projeto de forecasting**.

- A) Ordenar a série e verificar falhas, datas e mudanças de regime.
- B) Criar baselines e variáveis usando apenas o passado.
- C) Validar com divisões temporais sucessivas.
- D) Comparar erros, comunicar incerteza e definir o uso da previsão.
- E) Definir frequência, horizonte e decisão atendida.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`


> [!todo] PUBLICAR NO LINKEDIN — projeto prioritário do portfólio
> - [ ] Publique somente após README, resultados e limitações estarem revisados.
> - [ ] Inclua problema, abordagem, principal evidência, decisão e link do GitHub.
> - [ ] **Ângulo sugerido:** mostrar validação temporal, comparação com baseline sazonal e decisão de capacidade ou escala.


---
