<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 80 — Projeto de forecasting — 20/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **Projeto de forecasting** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Projeto de forecasting.
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/energia.csv`.

### Passo a passo completo
1. [ ] Organize projeto de forecasting com dados, notebook, scripts, resultados e relatório.
2. [ ] Reexecute backtesting do zero e salve métricas em CSV.
3. [ ] Crie gráfico de previsão com intervalo e comparação com baseline.
4. [ ] Produza resumo executivo com decisão e riscos.
5. [ ] Grave apresentação de seis minutos e responda perguntas sobre leakage temporal e validação.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/roteiro_atividades.md`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Execute o backtesting removendo o mês de maior consumo e registre como ranking de modelos e erro mudam.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Aumente em 25% o custo de subestimação no resumo executivo e confira se a decisão operacional permanece.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Organize projeto de forecasting com dados, notebook, scripts, resultados e relatório.

   **Pergunta:** Qual separação de dados é adequada em **Projeto de forecasting**?

- [ ] A) Treinar no passado e validar em períodos posteriores, preservando a ordem temporal.
- [ ] B) Embaralhar todas as datas antes da divisão.
- [ ] C) Usar os períodos futuros no cálculo das variáveis de treino.
- [ ] D) Escolher aleatoriamente linhas do mesmo período para teste.
- [ ] E) Treinar e avaliar com toda a série ao mesmo tempo.

2. **Referência — atividade 2:** Reexecute backtesting do zero e salve métricas em CSV.

   **Pergunta:** Por que um baseline simples é importante em **Projeto de forecasting**?

- [ ] A) Porque sempre será o modelo usado em produção.
- [ ] B) Porque garante que não existam valores ausentes.
- [ ] C) Porque substitui a definição do horizonte de previsão.
- [ ] D) Porque mostra se o modelo supera regras como repetir o último valor ou a sazonalidade anterior.
- [ ] E) Porque elimina a necessidade de avaliar modelos mais complexos.

3. **Referência — atividade 3:** Crie gráfico de previsão com intervalo e comparação com baseline.

   **Pergunta:** Qual cuidado evita informação do futuro em variáveis de **Projeto de forecasting**?

- [ ] A) Ordenar por valor em vez de ordenar por data.
- [ ] B) Calcular defasagens e médias móveis usando somente observações disponíveis antes de cada previsão.
- [ ] C) Centralizar médias móveis com dados anteriores e posteriores.
- [ ] D) Preencher períodos passados com valores observados no futuro.
- [ ] E) Usar a série completa para ajustar cada transformação.

4. **Referência — atividade 4:** Produza resumo executivo com decisão e riscos.

   **Pergunta:** Como escolher uma solução de **Projeto de forecasting** para apoiar uma decisão?

- [ ] A) Escolher apenas pela menor falha média de treinamento.
- [ ] B) Ignorar mudanças de regime quando a métrica global é boa.
- [ ] C) Usar o mesmo horizonte para qualquer decisão.
- [ ] D) Comparar modelos em períodos de teste diferentes.
- [ ] E) Avaliar por horizonte e período, traduzindo os erros em impacto operacional ou financeiro.

5. **Referência — atividade 5:** Grave apresentação de seis minutos e responda perguntas sobre leakage temporal e validação.

   **Pergunta:** Ordene um fluxo de previsão para **Projeto de forecasting**.

- A) Ordenar a série e verificar falhas, datas e mudanças de regime.
- B) Criar baselines e variáveis usando apenas o passado.
- C) Validar com divisões temporais sucessivas.
- D) Comparar erros, comunicar incerteza e definir o uso da previsão.
- E) Definir frequência, horizonte e decisão atendida.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a atualização de uma previsão ligada a **Projeto de forecasting**.

- A) Gerar previsões para o horizonte definido.
- B) Executar o pipeline com a versão aprovada.
- C) Receber e validar os dados do período mais recente.
- D) Monitorar erros quando os valores reais se tornarem disponíveis.
- E) Reavaliar o modelo diante de degradação ou mudança de regime.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

> [!todo] PUBLICAR NO LINKEDIN — projeto prioritário do portfólio
> - [ ] Publique somente após README, resultados e limitações estarem revisados.
> - [ ] Inclua problema, abordagem, principal evidência, decisão e link do GitHub.
> - [ ] **Ângulo sugerido:** mostrar validação temporal, comparação com baseline sazonal e decisão de capacidade ou escala.

> [!project] Projeto semanal — Forecasting de volume de chamados
> **Desafio:** Prever demanda futura e transformar intervalos de previsão em recomendação de escala ou capacidade.
>
> **Deve reutilizar:** Séries temporais e todo o repertório anterior.
>
> **Entregáveis obrigatórios:**
> - [ ] baseline sazonal;
> - [ ] validação temporal;
> - [ ] dois métodos;
> - [ ] intervalos e cenários;
> - [ ] decisão operacional;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Seu modelo supera um baseline simples em backtesting e a previsão leva a uma decisão concreta?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Projeto de forecasting.
- **Competência sugerida:** Forecasting.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Forecasting** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
