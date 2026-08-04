<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 78 — Modelos tradicionais — 18/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **Modelos tradicionais** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Modelos tradicionais.
- **Pasta/arquivo principal:** `semana-16/dia-078-modelos-tradicionais.ipynb`.
- **Dados:** `dados/energia.csv`.

### Passo a passo completo
1. [ ] Treine regressão linear com lags, árvore/Random Forest e modelo estatístico simples como Holt-Winters ou ARIMA, se disponível.
2. [ ] Garanta que features sejam criadas respeitando tempo.
3. [ ] Faça backtesting com múltiplos cortes.
4. [ ] Compare erro e estabilidade por horizonte.
5. [ ] Analise resíduos e autocorrelação remanescente.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Avalie **Modelos tradicionais** em uma janela temporal ou horizonte adicional, mantendo a ordem das datas.
- [ ] Crie um teste de estresse com mudança de regime, período ausente ou custo maior e registre se a conclusão permanece útil.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Qual separação de dados é adequada em **Modelos tradicionais**?

- [ ] A) Escolher aleatoriamente linhas do mesmo período para teste.
- [ ] B) Treinar e avaliar com toda a série ao mesmo tempo.
- [ ] C) Treinar no passado e validar em períodos posteriores, preservando a ordem temporal.
- [ ] D) Embaralhar todas as datas antes da divisão.
- [ ] E) Usar os períodos futuros no cálculo das variáveis de treino.

2. Por que um baseline simples é importante em **Modelos tradicionais**?

- [ ] A) Porque mostra se o modelo supera regras como repetir o último valor ou a sazonalidade anterior.
- [ ] B) Porque elimina a necessidade de avaliar modelos mais complexos.
- [ ] C) Porque sempre será o modelo usado em produção.
- [ ] D) Porque garante que não existam valores ausentes.
- [ ] E) Porque substitui a definição do horizonte de previsão.

3. Qual cuidado evita informação do futuro em variáveis de **Modelos tradicionais**?

- [ ] A) Preencher períodos passados com valores observados no futuro.
- [ ] B) Usar a série completa para ajustar cada transformação.
- [ ] C) Ordenar por valor em vez de ordenar por data.
- [ ] D) Calcular defasagens e médias móveis usando somente observações disponíveis antes de cada previsão.
- [ ] E) Centralizar médias móveis com dados anteriores e posteriores.

4. Como escolher uma solução de **Modelos tradicionais** para apoiar uma decisão?

- [ ] A) Comparar modelos em períodos de teste diferentes.
- [ ] B) Avaliar por horizonte e período, traduzindo os erros em impacto operacional ou financeiro.
- [ ] C) Escolher apenas pela menor falha média de treinamento.
- [ ] D) Ignorar mudanças de regime quando a métrica global é boa.
- [ ] E) Usar o mesmo horizonte para qualquer decisão.

5. Ordene um fluxo de previsão para **Modelos tradicionais**.

- A) Definir frequência, horizonte e decisão atendida.
- B) Criar baselines e variáveis usando apenas o passado.
- C) Ordenar a série e verificar falhas, datas e mudanças de regime.
- D) Validar com divisões temporais sucessivas.
- E) Comparar erros, comunicar incerteza e definir o uso da previsão.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene a atualização de uma previsão ligada a **Modelos tradicionais**.

- A) Executar o pipeline com a versão aprovada.
- B) Gerar previsões para o horizonte definido.
- C) Monitorar erros quando os valores reais se tornarem disponíveis.
- D) Reavaliar o modelo diante de degradação ou mudança de regime.
- E) Receber e validar os dados do período mais recente.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Modelos tradicionais.
- **Competência sugerida:** Modelos de séries temporais.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Modelos de séries temporais** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação
