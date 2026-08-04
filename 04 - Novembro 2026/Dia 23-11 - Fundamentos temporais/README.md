<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 76 — Fundamentos temporais — 16/11/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Fundamentos temporais.
- **Competência sugerida:** Séries temporais.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Séries temporais** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Fundamentos temporais** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Fundamentos temporais.
- **Pasta/arquivo principal:** `01-exercicios/dia-076-fundamentos-temporais.ipynb`.
- **Dados:** `dados/energia.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Carregue `energia.csv`, converta índice temporal e verifique frequência, lacunas e duplicidades.
2. [ ] Separe tendência, sazonalidade e ruído por gráficos e médias móveis.
3. [ ] Calcule autocorrelação em atrasos 1, 7 e 30.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Crie features de calendário e lags sem olhar o futuro.
- [ ] Defina horizonte de previsão e decisão operacional associada.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-076-fundamentos-temporais.ipynb`:** Remova sete dias consecutivos de uma cópia da série e mostre como a verificação de frequência identifica a lacuna.
- [ ] **Em `01-exercicios/dia-076-fundamentos-temporais.ipynb`:** Crie lags 1, 7 e 30 e confirme que cada linha usa somente datas anteriores à própria data.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Por que um baseline simples é importante em **Fundamentos temporais**?

- [ ] A) Porque garante que não existam valores ausentes.
- [ ] B) Porque substitui a definição do horizonte de previsão.
- [ ] C) Porque mostra se o modelo supera regras como repetir o último valor ou a sazonalidade anterior.
- [ ] D) Porque elimina a necessidade de avaliar modelos mais complexos.
- [ ] E) Porque sempre será o modelo usado em produção.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual cuidado evita informação do futuro em variáveis de **Fundamentos temporais**?

- [ ] A) Calcular defasagens e médias móveis usando somente observações disponíveis antes de cada previsão.
- [ ] B) Centralizar médias móveis com dados anteriores e posteriores.
- [ ] C) Preencher períodos passados com valores observados no futuro.
- [ ] D) Usar a série completa para ajustar cada transformação.
- [ ] E) Ordenar por valor em vez de ordenar por data.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de previsão para **Fundamentos temporais**.

- A) Comparar erros, comunicar incerteza e definir o uso da previsão.
- B) Criar baselines e variáveis usando apenas o passado.
- C) Ordenar a série e verificar falhas, datas e mudanças de regime.
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
