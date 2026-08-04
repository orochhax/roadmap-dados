<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 88 — Orquestração conceitual — 02/12/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Orquestração conceitual.
- **Competência sugerida:** Orquestração de pipelines.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Orquestração de pipelines** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Orquestração conceitual** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Orquestração conceitual.
- **Pasta/arquivo principal:** `01-exercicios/dia-088-orquestracao-conceitual.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Modele o pipeline como tarefas com dependências: extrair → validar → transformar → carregar → testar.
2. [ ] Crie um DAG conceitual em Mermaid ou use Prefect/Airflow local se desejar.
3. [ ] Defina política de retry, timeout, alerta e backfill.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Simule falha na transformação e confirme que carregamento não ocorre.
- [ ] Escreva um runbook com diagnóstico e recuperação.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-088-orquestracao-conceitual.py`:** Defina retry máximo 3, timeout 10 minutos e alerta após a última falha para a tarefa transformar.
- [ ] **Em `01-exercicios/dia-088-orquestracao-conceitual.py`:** Simule transformar com status falha e confirme no fluxo que carregar e testar ficam bloqueadas.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual controle de qualidade é mais útil em **Orquestração conceitual**?

- [ ] A) Validar esquema, chaves, nulidade, faixas, duplicidades e volume em pontos definidos do fluxo.
- [ ] B) Conferir apenas se o processo terminou sem erro.
- [ ] C) Aceitar qualquer alteração de esquema automaticamente.
- [ ] D) Verificar somente o tamanho do arquivo final.
- [ ] E) Remover registros problemáticos sem contabilizá-los.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** O que melhora a observabilidade de uma solução de **Orquestração conceitual**?

- [ ] A) Ocultar falhas e repetir o processo indefinidamente.
- [ ] B) Registrar somente o horário de início.
- [ ] C) Depender da observação manual da pasta de saída.
- [ ] D) Logs estruturados, métricas, alertas e identificação clara de cada execução e etapa.
- [ ] E) Mensagens genéricas como 'deu erro'.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de dados para **Orquestração conceitual**.

- A) Validar e transformar preservando rastreabilidade.
- B) Extrair os dados com identificação da execução.
- C) Definir fontes, destino, frequência e contrato dos dados.
- D) Carregar de forma idempotente no destino.
- E) Monitorar qualidade, volume, duração e falhas.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`
