<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 86 — ETL/ELT e arquitetura básica — 30/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **ETL/ELT e arquitetura básica** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** ETL/ELT e arquitetura básica.
- **Pasta/arquivo principal:** `01-exercicios/dia-086-etl-elt-e-arquitetura-basica.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Passo a passo completo
1. [ ] Desenhe arquitetura simples: fontes CSV/API → camada raw → transformação → camada curated → consumo por BI/modelo.
2. [ ] Explique ETL versus ELT com o mesmo exemplo e escolha uma abordagem.
3. [ ] Defina contratos de dados para incidentes e clientes: campos, tipos, chave e frequência.
4. [ ] Crie estrutura de pastas `raw`, `processed`, `curated` e regras de nomenclatura.
5. [ ] Liste cinco falhas possíveis e como detectar cada uma.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-086-etl-elt-e-arquitetura-basica.py`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-086-etl-elt-e-arquitetura-basica.py`:** Adicione à arquitetura uma área quarantine entre raw e processed para linhas sem id ou com tipo inválido.
- [ ] **Em `01-exercicios/dia-086-etl-elt-e-arquitetura-basica.py`:** Simule ausência da coluna id e uma execução repetida; descreva em qual etapa cada problema deve ser detectado.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Desenhe arquitetura simples: fontes CSV/API → camada raw → transformação → camada curated → consumo por BI/modelo.

   **Pergunta:** Qual característica torna um pipeline de **ETL/ELT e arquitetura básica** seguro para ser executado novamente?

- [ ] A) Gerar um arquivo diferente a cada tentativa.
- [ ] B) Apagar toda a origem antes de iniciar.
- [ ] C) Depender de correções manuais após cada execução.
- [ ] D) Ignorar registros já processados sem usar uma chave.
- [ ] E) Ser idempotente, produzindo estado consistente sem duplicar ou corromper dados.

2. **Referência — atividade 2:** Explique ETL versus ELT com o mesmo exemplo e escolha uma abordagem.

   **Pergunta:** Qual controle de qualidade é mais útil em **ETL/ELT e arquitetura básica**?

- [ ] A) Verificar somente o tamanho do arquivo final.
- [ ] B) Remover registros problemáticos sem contabilizá-los.
- [ ] C) Validar esquema, chaves, nulidade, faixas, duplicidades e volume em pontos definidos do fluxo.
- [ ] D) Conferir apenas se o processo terminou sem erro.
- [ ] E) Aceitar qualquer alteração de esquema automaticamente.

3. **Referência — atividade 3:** Defina contratos de dados para incidentes e clientes: campos, tipos, chave e frequência.

   **Pergunta:** O que melhora a observabilidade de uma solução de **ETL/ELT e arquitetura básica**?

- [ ] A) Logs estruturados, métricas, alertas e identificação clara de cada execução e etapa.
- [ ] B) Mensagens genéricas como 'deu erro'.
- [ ] C) Ocultar falhas e repetir o processo indefinidamente.
- [ ] D) Registrar somente o horário de início.
- [ ] E) Depender da observação manual da pasta de saída.

4. **Referência — atividade 4:** Crie estrutura de pastas `raw`, `processed`, `curated` e regras de nomenclatura.

   **Pergunta:** Como relacionar **ETL/ELT e arquitetura básica** a uma necessidade de negócio?

- [ ] A) Processar tudo em tempo real, mesmo sem necessidade.
- [ ] B) Manter dados sem informar origem ou atualização.
- [ ] C) Priorizar volume acima de confiabilidade e custo.
- [ ] D) Definir prazo, frequência, qualidade e consumidores dos dados antes de escolher a arquitetura.
- [ ] E) Escolher a ferramenta mais complexa disponível.

5. **Referência — atividade 5:** Liste cinco falhas possíveis e como detectar cada uma.

   **Pergunta:** Ordene um fluxo de dados para **ETL/ELT e arquitetura básica**.

- A) Monitorar qualidade, volume, duração e falhas.
- B) Extrair os dados com identificação da execução.
- C) Validar e transformar preservando rastreabilidade.
- D) Carregar de forma idempotente no destino.
- E) Definir fontes, destino, frequência e contrato dos dados.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a resposta a uma falha em **ETL/ELT e arquitetura básica**.

- A) Detectar a falha por alerta ou verificação automática.
- B) Identificar execução, etapa e dados afetados.
- C) Confirmar a recuperação e registrar prevenção.
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

- **Conhecimento praticado hoje:** ETL/ELT e arquitetura básica.
- **Competência sugerida:** ETL, ELT e arquitetura de dados.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **ETL, ELT e arquitetura de dados** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
