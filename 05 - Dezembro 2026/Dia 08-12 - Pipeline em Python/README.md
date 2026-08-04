<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 87 — Pipeline em Python — 01/12/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Pipeline em Python.
- **Competência sugerida:** Pipelines de dados com Python.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Pipelines de dados com Python** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Pipeline em Python** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Pipeline em Python.
- **Pasta/arquivo principal:** `01-exercicios/transform.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Implemente `extract.py` para ler CSV/JSON, `transform.py` para limpar e criar features, e `load.py` para gravar Parquet ou DuckDB.
2. [ ] Use arquivo de configuração para caminhos, sem valores fixos no código.
3. [ ] Adicione logs com quantidade lida, rejeitada e gravada.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Garanta idempotência: executar duas vezes não deve duplicar dados.
- [ ] Teste arquivo ausente, coluna faltante, linha inválida e execução repetida.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/transform.py`:** Adicione validação obrigatória das colunas cliente_id e data_ativacao antes da transformação.
- [ ] **Em `01-exercicios/transform.py`:** Execute duas vezes com o mesmo arquivo e depois com uma linha nova; compare contagens para provar idempotência e incremento.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual controle de qualidade é mais útil em **Pipeline em Python**?

- [ ] A) Remover registros problemáticos sem contabilizá-los.
- [ ] B) Validar esquema, chaves, nulidade, faixas, duplicidades e volume em pontos definidos do fluxo.
- [ ] C) Conferir apenas se o processo terminou sem erro.
- [ ] D) Aceitar qualquer alteração de esquema automaticamente.
- [ ] E) Verificar somente o tamanho do arquivo final.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** O que melhora a observabilidade de uma solução de **Pipeline em Python**?

- [ ] A) Mensagens genéricas como 'deu erro'.
- [ ] B) Ocultar falhas e repetir o processo indefinidamente.
- [ ] C) Registrar somente o horário de início.
- [ ] D) Depender da observação manual da pasta de saída.
- [ ] E) Logs estruturados, métricas, alertas e identificação clara de cada execução e etapa.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de dados para **Pipeline em Python**.

- A) Monitorar qualidade, volume, duração e falhas.
- B) Validar e transformar preservando rastreabilidade.
- C) Extrair os dados com identificação da execução.
- D) Carregar de forma idempotente no destino.
- E) Definir fontes, destino, frequência e contrato dos dados.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`
