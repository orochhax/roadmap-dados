<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 77 — Baselines temporais — 17/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **Baselines temporais** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Baselines temporais.
- **Pasta/arquivo principal:** `semana-16/dia-077-baselines-temporais.ipynb`.
- **Dados:** `dados/energia.csv`.

### Passo a passo completo
1. [ ] Implemente baselines: último valor, média móvel de 7 dias, média do mesmo dia da semana e média sazonal.
2. [ ] Use validação walk-forward em pelo menos três janelas.
3. [ ] Calcule MAE, RMSE e MAPE/SMAPE quando adequado.
4. [ ] Compare desempenho por períodos de alta e baixa demanda.
5. [ ] Escolha baseline oficial que qualquer modelo deve superar.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Avalie **Baselines temporais** em uma janela temporal ou horizonte adicional, mantendo a ordem das datas.
- [ ] Crie um teste de estresse com mudança de regime, período ausente ou custo maior e registre se a conclusão permanece útil.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Qual separação de dados é adequada em **Baselines temporais**?

- [ ] A) Usar os períodos futuros no cálculo das variáveis de treino.
- [ ] B) Escolher aleatoriamente linhas do mesmo período para teste.
- [ ] C) Treinar e avaliar com toda a série ao mesmo tempo.
- [ ] D) Treinar no passado e validar em períodos posteriores, preservando a ordem temporal.
- [ ] E) Embaralhar todas as datas antes da divisão.

2. Por que um baseline simples é importante em **Baselines temporais**?

- [ ] A) Porque substitui a definição do horizonte de previsão.
- [ ] B) Porque mostra se o modelo supera regras como repetir o último valor ou a sazonalidade anterior.
- [ ] C) Porque elimina a necessidade de avaliar modelos mais complexos.
- [ ] D) Porque sempre será o modelo usado em produção.
- [ ] E) Porque garante que não existam valores ausentes.

3. Qual cuidado evita informação do futuro em variáveis de **Baselines temporais**?

- [ ] A) Centralizar médias móveis com dados anteriores e posteriores.
- [ ] B) Preencher períodos passados com valores observados no futuro.
- [ ] C) Usar a série completa para ajustar cada transformação.
- [ ] D) Ordenar por valor em vez de ordenar por data.
- [ ] E) Calcular defasagens e médias móveis usando somente observações disponíveis antes de cada previsão.

4. Como escolher uma solução de **Baselines temporais** para apoiar uma decisão?

- [ ] A) Usar o mesmo horizonte para qualquer decisão.
- [ ] B) Comparar modelos em períodos de teste diferentes.
- [ ] C) Avaliar por horizonte e período, traduzindo os erros em impacto operacional ou financeiro.
- [ ] D) Escolher apenas pela menor falha média de treinamento.
- [ ] E) Ignorar mudanças de regime quando a métrica global é boa.

5. Ordene um fluxo de previsão para **Baselines temporais**.

- A) Criar baselines e variáveis usando apenas o passado.
- B) Ordenar a série e verificar falhas, datas e mudanças de regime.
- C) Comparar erros, comunicar incerteza e definir o uso da previsão.
- D) Validar com divisões temporais sucessivas.
- E) Definir frequência, horizonte e decisão atendida.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene a atualização de uma previsão ligada a **Baselines temporais**.

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
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Baselines temporais.
- **Competência sugerida:** Baselines de forecasting.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Baselines de forecasting** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação
