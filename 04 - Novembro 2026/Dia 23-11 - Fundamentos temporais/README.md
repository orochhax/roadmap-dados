<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 76 — Fundamentos temporais — 16/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **Fundamentos temporais** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Fundamentos temporais.
- **Pasta/arquivo principal:** `01-exercicios/dia-076-fundamentos-temporais.ipynb`.
- **Dados:** `dados/energia.csv`.

### Passo a passo completo
1. [ ] Carregue `energia.csv`, converta índice temporal e verifique frequência, lacunas e duplicidades.
2. [ ] Separe tendência, sazonalidade e ruído por gráficos e médias móveis.
3. [ ] Calcule autocorrelação em atrasos 1, 7 e 30.
4. [ ] Crie features de calendário e lags sem olhar o futuro.
5. [ ] Defina horizonte de previsão e decisão operacional associada.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-076-fundamentos-temporais.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-076-fundamentos-temporais.ipynb`:** Remova sete dias consecutivos de uma cópia da série e mostre como a verificação de frequência identifica a lacuna.
- [ ] **Em `01-exercicios/dia-076-fundamentos-temporais.ipynb`:** Crie lags 1, 7 e 30 e confirme que cada linha usa somente datas anteriores à própria data.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Carregue `energia.csv`, converta índice temporal e verifique frequência, lacunas e duplicidades.

   **Pergunta:** Qual separação de dados é adequada em **Fundamentos temporais**?

- [ ] A) Embaralhar todas as datas antes da divisão.
- [ ] B) Usar os períodos futuros no cálculo das variáveis de treino.
- [ ] C) Escolher aleatoriamente linhas do mesmo período para teste.
- [ ] D) Treinar e avaliar com toda a série ao mesmo tempo.
- [ ] E) Treinar no passado e validar em períodos posteriores, preservando a ordem temporal.

2. **Referência — atividade 2:** Separe tendência, sazonalidade e ruído por gráficos e médias móveis.

   **Pergunta:** Por que um baseline simples é importante em **Fundamentos temporais**?

- [ ] A) Porque garante que não existam valores ausentes.
- [ ] B) Porque substitui a definição do horizonte de previsão.
- [ ] C) Porque mostra se o modelo supera regras como repetir o último valor ou a sazonalidade anterior.
- [ ] D) Porque elimina a necessidade de avaliar modelos mais complexos.
- [ ] E) Porque sempre será o modelo usado em produção.

3. **Referência — atividade 3:** Calcule autocorrelação em atrasos 1, 7 e 30.

   **Pergunta:** Qual cuidado evita informação do futuro em variáveis de **Fundamentos temporais**?

- [ ] A) Calcular defasagens e médias móveis usando somente observações disponíveis antes de cada previsão.
- [ ] B) Centralizar médias móveis com dados anteriores e posteriores.
- [ ] C) Preencher períodos passados com valores observados no futuro.
- [ ] D) Usar a série completa para ajustar cada transformação.
- [ ] E) Ordenar por valor em vez de ordenar por data.

4. **Referência — atividade 4:** Crie features de calendário e lags sem olhar o futuro.

   **Pergunta:** Como escolher uma solução de **Fundamentos temporais** para apoiar uma decisão?

- [ ] A) Ignorar mudanças de regime quando a métrica global é boa.
- [ ] B) Usar o mesmo horizonte para qualquer decisão.
- [ ] C) Comparar modelos em períodos de teste diferentes.
- [ ] D) Avaliar por horizonte e período, traduzindo os erros em impacto operacional ou financeiro.
- [ ] E) Escolher apenas pela menor falha média de treinamento.

5. **Referência — atividade 5:** Defina horizonte de previsão e decisão operacional associada.

   **Pergunta:** Ordene um fluxo de previsão para **Fundamentos temporais**.

- A) Comparar erros, comunicar incerteza e definir o uso da previsão.
- B) Criar baselines e variáveis usando apenas o passado.
- C) Ordenar a série e verificar falhas, datas e mudanças de regime.
- D) Validar com divisões temporais sucessivas.
- E) Definir frequência, horizonte e decisão atendida.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a atualização de uma previsão ligada a **Fundamentos temporais**.

- A) Receber e validar os dados do período mais recente.
- B) Gerar previsões para o horizonte definido.
- C) Executar o pipeline com a versão aprovada.
- D) Monitorar erros quando os valores reais se tornarem disponíveis.
- E) Reavaliar o modelo diante de degradação ou mudança de regime.

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

- **Conhecimento praticado hoje:** Fundamentos temporais.
- **Competência sugerida:** Séries temporais.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Séries temporais** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
