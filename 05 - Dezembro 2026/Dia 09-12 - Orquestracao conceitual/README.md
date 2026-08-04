<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 88 — Orquestração conceitual — 02/12/2026
> [!abstract] Resultado concreto do dia
> Concluir **Orquestração conceitual** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Orquestração conceitual.
- **Pasta/arquivo principal:** `01-exercicios/dia-088-orquestracao-conceitual.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Passo a passo completo
1. [ ] Modele o pipeline como tarefas com dependências: extrair → validar → transformar → carregar → testar.
2. [ ] Crie um DAG conceitual em Mermaid ou use Prefect/Airflow local se desejar.
3. [ ] Defina política de retry, timeout, alerta e backfill.
4. [ ] Simule falha na transformação e confirme que carregamento não ocorre.
5. [ ] Escreva um runbook com diagnóstico e recuperação.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-088-orquestracao-conceitual.py`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-088-orquestracao-conceitual.py`:** Defina retry máximo 3, timeout 10 minutos e alerta após a última falha para a tarefa transformar.
- [ ] **Em `01-exercicios/dia-088-orquestracao-conceitual.py`:** Simule transformar com status falha e confirme no fluxo que carregar e testar ficam bloqueadas.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Modele o pipeline como tarefas com dependências: extrair → validar → transformar → carregar → testar.

   **Pergunta:** Qual característica torna um pipeline de **Orquestração conceitual** seguro para ser executado novamente?

- [ ] A) Depender de correções manuais após cada execução.
- [ ] B) Ignorar registros já processados sem usar uma chave.
- [ ] C) Ser idempotente, produzindo estado consistente sem duplicar ou corromper dados.
- [ ] D) Gerar um arquivo diferente a cada tentativa.
- [ ] E) Apagar toda a origem antes de iniciar.

2. **Referência — atividade 2:** Crie um DAG conceitual em Mermaid ou use Prefect/Airflow local se desejar.

   **Pergunta:** Qual controle de qualidade é mais útil em **Orquestração conceitual**?

- [ ] A) Validar esquema, chaves, nulidade, faixas, duplicidades e volume em pontos definidos do fluxo.
- [ ] B) Conferir apenas se o processo terminou sem erro.
- [ ] C) Aceitar qualquer alteração de esquema automaticamente.
- [ ] D) Verificar somente o tamanho do arquivo final.
- [ ] E) Remover registros problemáticos sem contabilizá-los.

3. **Referência — atividade 3:** Defina política de retry, timeout, alerta e backfill.

   **Pergunta:** O que melhora a observabilidade de uma solução de **Orquestração conceitual**?

- [ ] A) Ocultar falhas e repetir o processo indefinidamente.
- [ ] B) Registrar somente o horário de início.
- [ ] C) Depender da observação manual da pasta de saída.
- [ ] D) Logs estruturados, métricas, alertas e identificação clara de cada execução e etapa.
- [ ] E) Mensagens genéricas como 'deu erro'.

4. **Referência — atividade 4:** Simule falha na transformação e confirme que carregamento não ocorre.

   **Pergunta:** Como relacionar **Orquestração conceitual** a uma necessidade de negócio?

- [ ] A) Priorizar volume acima de confiabilidade e custo.
- [ ] B) Definir prazo, frequência, qualidade e consumidores dos dados antes de escolher a arquitetura.
- [ ] C) Escolher a ferramenta mais complexa disponível.
- [ ] D) Processar tudo em tempo real, mesmo sem necessidade.
- [ ] E) Manter dados sem informar origem ou atualização.

5. **Referência — atividade 5:** Escreva um runbook com diagnóstico e recuperação.

   **Pergunta:** Ordene um fluxo de dados para **Orquestração conceitual**.

- A) Validar e transformar preservando rastreabilidade.
- B) Extrair os dados com identificação da execução.
- C) Definir fontes, destino, frequência e contrato dos dados.
- D) Carregar de forma idempotente no destino.
- E) Monitorar qualidade, volume, duração e falhas.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a resposta a uma falha em **Orquestração conceitual**.

- A) Corrigir a causa mantendo os dados íntegros.
- B) Identificar execução, etapa e dados afetados.
- C) Detectar a falha por alerta ou verificação automática.
- D) Reprocessar somente o escopo necessário.
- E) Confirmar a recuperação e registrar prevenção.

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

- **Conhecimento praticado hoje:** Orquestração conceitual.
- **Competência sugerida:** Orquestração de pipelines.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Orquestração de pipelines** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
