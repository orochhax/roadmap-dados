<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 36 — Intervalos de confiança — 21/09/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Intervalos de confiança.
- **Competência sugerida:** Intervalos de confiança.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Intervalos de confiança** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

> [!abstract] Resultado concreto do dia
> Concluir **Intervalos de confiança** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Intervalos de confiança.
- **Pasta/arquivo principal:** `01-exercicios/dia-036-intervalos-de-confianca.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Calcule um intervalo de confiança de 95% para a média manualmente e com biblioteca, declarando as suposições usadas.
2. [ ] Compare a largura do intervalo em amostras de tamanho 20 e 100.
3. [ ] Escreva a interpretação correta do intervalo sem atribuir probabilidade ao parâmetro fixo.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Compare 90%, 95% e 99% somente se a interpretação do intervalo de 95% estiver clara.
- [ ] Bootstrap para média e mediana é desafio; implemente-o depois de dominar o intervalo paramétrico.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-036-intervalos-de-confianca.ipynb`:** Calcule IC de 95% para as primeiras 50 durações por método paramétrico e bootstrap com seed 42; compare as larguras.
- [ ] **Em `01-exercicios/dia-036-intervalos-de-confianca.ipynb`:** Repita com uma amostra constante [60, 60, 60, 60, 60] e trate explicitamente a ausência de variabilidade.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual interpretação estatística é mais responsável em uma análise de **Intervalos de confiança**?

- [ ] A) Escolher a hipótese depois de observar os dados.
- [ ] B) Ignorar o tamanho da amostra quando a média parece convincente.
- [ ] C) Avaliar tamanho do efeito, incerteza, pressupostos e relevância prática em conjunto.
- [ ] D) Tratar qualquer valor-p pequeno como prova de grande impacto.
- [ ] E) Considerar correlação suficiente para afirmar causalidade.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual situação ameaça mais a validade de uma conclusão sobre **Intervalos de confiança**?

- [ ] A) Uma amostra enviesada que não representa adequadamente a população de interesse.
- [ ] B) Uma tabela com colunas em ordem diferente.
- [ ] C) Um gráfico com título curto.
- [ ] D) Uma média apresentada com duas casas decimais.
- [ ] E) Um arquivo salvo em uma pasta específica do projeto.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um estudo estatístico relacionado a **Intervalos de confiança**.

- A) Coletar e verificar a qualidade dos dados.
- B) Definir população, amostra, métrica e método.
- C) Formular a pergunta e a hipótese antes da análise.
- D) Interpretar a evidência com pressupostos e limitações.
- E) Estimar efeitos e quantificar a incerteza.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`
