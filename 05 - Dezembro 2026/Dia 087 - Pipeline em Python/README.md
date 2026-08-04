<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 87 — Pipeline em Python — 01/12/2026
> [!abstract] Resultado concreto do dia
> Concluir **Pipeline em Python** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Pipeline em Python.
- **Pasta/arquivo principal:** `semana-18/dia-087-pipeline-em-python.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Passo a passo completo
1. [ ] Implemente `extract.py` para ler CSV/JSON, `transform.py` para limpar e criar features, e `load.py` para gravar Parquet ou DuckDB.
2. [ ] Use arquivo de configuração para caminhos, sem valores fixos no código.
3. [ ] Adicione logs com quantidade lida, rejeitada e gravada.
4. [ ] Garanta idempotência: executar duas vezes não deve duplicar dados.
5. [ ] Teste arquivo ausente, coluna faltante, linha inválida e execução repetida.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Acrescente ao fluxo de **Pipeline em Python** uma checagem automática de qualidade ou uma condição clara de falha.
- [ ] Compare o comportamento de uma execução completa com uma execução parcial ou repetida e registre qualquer diferença inesperada.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Implemente `extract.py` para ler CSV/JSON, `transform.py` para limpar e criar features, e `load.py` para gravar Parquet ou DuckDB.

   **Pergunta:** Qual característica torna um pipeline de **Pipeline em Python** seguro para ser executado novamente?

- [ ] A) Apagar toda a origem antes de iniciar.
- [ ] B) Depender de correções manuais após cada execução.
- [ ] C) Ignorar registros já processados sem usar uma chave.
- [ ] D) Ser idempotente, produzindo estado consistente sem duplicar ou corromper dados.
- [ ] E) Gerar um arquivo diferente a cada tentativa.

2. **Referência — atividade 2:** Use arquivo de configuração para caminhos, sem valores fixos no código.

   **Pergunta:** Qual controle de qualidade é mais útil em **Pipeline em Python**?

- [ ] A) Remover registros problemáticos sem contabilizá-los.
- [ ] B) Validar esquema, chaves, nulidade, faixas, duplicidades e volume em pontos definidos do fluxo.
- [ ] C) Conferir apenas se o processo terminou sem erro.
- [ ] D) Aceitar qualquer alteração de esquema automaticamente.
- [ ] E) Verificar somente o tamanho do arquivo final.

3. **Referência — atividade 3:** Adicione logs com quantidade lida, rejeitada e gravada.

   **Pergunta:** O que melhora a observabilidade de uma solução de **Pipeline em Python**?

- [ ] A) Mensagens genéricas como 'deu erro'.
- [ ] B) Ocultar falhas e repetir o processo indefinidamente.
- [ ] C) Registrar somente o horário de início.
- [ ] D) Depender da observação manual da pasta de saída.
- [ ] E) Logs estruturados, métricas, alertas e identificação clara de cada execução e etapa.

4. **Referência — atividade 4:** Garanta idempotência: executar duas vezes não deve duplicar dados.

   **Pergunta:** Como relacionar **Pipeline em Python** a uma necessidade de negócio?

- [ ] A) Manter dados sem informar origem ou atualização.
- [ ] B) Priorizar volume acima de confiabilidade e custo.
- [ ] C) Definir prazo, frequência, qualidade e consumidores dos dados antes de escolher a arquitetura.
- [ ] D) Escolher a ferramenta mais complexa disponível.
- [ ] E) Processar tudo em tempo real, mesmo sem necessidade.

5. **Referência — atividade 5:** Teste arquivo ausente, coluna faltante, linha inválida e execução repetida.

   **Pergunta:** Ordene um fluxo de dados para **Pipeline em Python**.

- A) Monitorar qualidade, volume, duração e falhas.
- B) Validar e transformar preservando rastreabilidade.
- C) Extrair os dados com identificação da execução.
- D) Carregar de forma idempotente no destino.
- E) Definir fontes, destino, frequência e contrato dos dados.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a resposta a uma falha em **Pipeline em Python**.

- A) Detectar a falha por alerta ou verificação automática.
- B) Confirmar a recuperação e registrar prevenção.
- C) Identificar execução, etapa e dados afetados.
- D) Reprocessar somente o escopo necessário.
- E) Corrigir a causa mantendo os dados íntegros.

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

- **Conhecimento praticado hoje:** Pipeline em Python.
- **Competência sugerida:** Pipelines de dados com Python.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Pipelines de dados com Python** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
