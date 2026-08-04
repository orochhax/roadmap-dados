<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 90 — Entrega do pipeline — 04/12/2026
> [!abstract] Resultado concreto do dia
> Concluir **Entrega do pipeline** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Entrega do pipeline.
- **Pasta/arquivo principal:** `semana-18/dia-090-entrega-do-pipeline/` (pasta do projeto).
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Passo a passo completo
1. [ ] Empacote pipeline da semana com script de execução única.
2. [ ] Adicione validações de esquema, unicidade, nulos e limites.
3. [ ] Produza tabela de auditoria com data, status, linhas de entrada, saída e erro.
4. [ ] Rode duas vezes e com dados novos para provar idempotência/incremento correto.
5. [ ] Publique README de arquitetura, execução, testes e limitações.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Acrescente ao fluxo de **Entrega do pipeline** uma checagem automática de qualidade ou uma condição clara de falha.
- [ ] Compare o comportamento de uma execução completa com uma execução parcial ou repetida e registre qualquer diferença inesperada.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Empacote pipeline da semana com script de execução única.

   **Pergunta:** Qual característica torna um pipeline de **Entrega do pipeline** seguro para ser executado novamente?

- [ ] A) Ser idempotente, produzindo estado consistente sem duplicar ou corromper dados.
- [ ] B) Gerar um arquivo diferente a cada tentativa.
- [ ] C) Apagar toda a origem antes de iniciar.
- [ ] D) Depender de correções manuais após cada execução.
- [ ] E) Ignorar registros já processados sem usar uma chave.

2. **Referência — atividade 2:** Adicione validações de esquema, unicidade, nulos e limites.

   **Pergunta:** Qual controle de qualidade é mais útil em **Entrega do pipeline**?

- [ ] A) Aceitar qualquer alteração de esquema automaticamente.
- [ ] B) Verificar somente o tamanho do arquivo final.
- [ ] C) Remover registros problemáticos sem contabilizá-los.
- [ ] D) Validar esquema, chaves, nulidade, faixas, duplicidades e volume em pontos definidos do fluxo.
- [ ] E) Conferir apenas se o processo terminou sem erro.

3. **Referência — atividade 3:** Produza tabela de auditoria com data, status, linhas de entrada, saída e erro.

   **Pergunta:** O que melhora a observabilidade de uma solução de **Entrega do pipeline**?

- [ ] A) Depender da observação manual da pasta de saída.
- [ ] B) Logs estruturados, métricas, alertas e identificação clara de cada execução e etapa.
- [ ] C) Mensagens genéricas como 'deu erro'.
- [ ] D) Ocultar falhas e repetir o processo indefinidamente.
- [ ] E) Registrar somente o horário de início.

4. **Referência — atividade 4:** Rode duas vezes e com dados novos para provar idempotência/incremento correto.

   **Pergunta:** Como relacionar **Entrega do pipeline** a uma necessidade de negócio?

- [ ] A) Escolher a ferramenta mais complexa disponível.
- [ ] B) Processar tudo em tempo real, mesmo sem necessidade.
- [ ] C) Manter dados sem informar origem ou atualização.
- [ ] D) Priorizar volume acima de confiabilidade e custo.
- [ ] E) Definir prazo, frequência, qualidade e consumidores dos dados antes de escolher a arquitetura.

5. **Referência — atividade 5:** Publique README de arquitetura, execução, testes e limitações.

   **Pergunta:** Ordene um fluxo de dados para **Entrega do pipeline**.

- A) Definir fontes, destino, frequência e contrato dos dados.
- B) Validar e transformar preservando rastreabilidade.
- C) Extrair os dados com identificação da execução.
- D) Carregar de forma idempotente no destino.
- E) Monitorar qualidade, volume, duração e falhas.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a resposta a uma falha em **Entrega do pipeline**.

- A) Detectar a falha por alerta ou verificação automática.
- B) Corrigir a causa mantendo os dados íntegros.
- C) Identificar execução, etapa e dados afetados.
- D) Reprocessar somente o escopo necessário.
- E) Confirmar a recuperação e registrar prevenção.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

> [!project] Projeto semanal — Pipeline ETL reprodutível
> **Desafio:** Criar um pipeline que ingere, valida, transforma e publica dados para análise e modelagem.
>
> **Deve reutilizar:** Python, SQL, testes de dados e arquitetura básica.
>
> **Entregáveis obrigatórios:**
> - [ ] camadas raw/clean/analytics;
> - [ ] execução idempotente;
> - [ ] logs e validações;
> - [ ] documentação de arquitetura;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Você consegue explicar de onde os dados vieram, como foram transformados e como reproduzir a tabela usada no modelo?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Entrega do pipeline.
- **Competência sugerida:** Engenharia de Dados.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Engenharia de Dados** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
