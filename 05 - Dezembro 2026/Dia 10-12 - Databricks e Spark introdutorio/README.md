<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 89 — Databricks e Spark introdutório — 03/12/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Databricks e Spark introdutório.
- **Competência sugerida:** Databricks e Apache Spark.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Databricks e Apache Spark** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Databricks e Spark introdutório** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Databricks e Spark introdutório.
- **Pasta/arquivo principal:** `01-exercicios/dia-089-databricks-e-spark-introdutorio.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Crie conta/ambiente Databricks Free ou use PySpark local.
2. [ ] Carregue `clientes_telecom.csv` como DataFrame Spark e inspecione esquema.
3. [ ] Faça seleção, filtro, agregação, join e criação de coluna.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Compare sintaxe e execução com pandas em cinco operações.
- [ ] Salve resultado em Parquet e explique quando Spark é desnecessário.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-089-databricks-e-spark-introdutorio.py`:** Filtre clientes com chamados_90d>=3, agrupe por cidade e compare o resultado Spark com pandas.
- [ ] **Em `01-exercicios/dia-089-databricks-e-spark-introdutorio.py`:** Remova a coluna cliente_id da entrada e faça a checagem de esquema impedir o processamento.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual controle de qualidade é mais útil em **Databricks e Spark introdutório**?

- [ ] A) Conferir apenas se o processo terminou sem erro.
- [ ] B) Aceitar qualquer alteração de esquema automaticamente.
- [ ] C) Verificar somente o tamanho do arquivo final.
- [ ] D) Remover registros problemáticos sem contabilizá-los.
- [ ] E) Validar esquema, chaves, nulidade, faixas, duplicidades e volume em pontos definidos do fluxo.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** O que melhora a observabilidade de uma solução de **Databricks e Spark introdutório**?

- [ ] A) Registrar somente o horário de início.
- [ ] B) Depender da observação manual da pasta de saída.
- [ ] C) Logs estruturados, métricas, alertas e identificação clara de cada execução e etapa.
- [ ] D) Mensagens genéricas como 'deu erro'.
- [ ] E) Ocultar falhas e repetir o processo indefinidamente.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de dados para **Databricks e Spark introdutório**.

- A) Extrair os dados com identificação da execução.
- B) Validar e transformar preservando rastreabilidade.
- C) Carregar de forma idempotente no destino.
- D) Monitorar qualidade, volume, duração e falhas.
- E) Definir fontes, destino, frequência e contrato dos dados.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`
