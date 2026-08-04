<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 86 — ETL/ELT e arquitetura básica — 30/11/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** ETL/ELT e arquitetura básica.
- **Competência sugerida:** ETL, ELT e arquitetura de dados.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **ETL, ELT e arquitetura de dados** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **ETL/ELT e arquitetura básica** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** ETL/ELT e arquitetura básica.
- **Pasta/arquivo principal:** `01-exercicios/dia-086-etl-elt-e-arquitetura-basica.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Desenhe arquitetura simples: fontes CSV/API → camada raw → transformação → camada curated → consumo por BI/modelo.
2. [ ] Explique ETL versus ELT com o mesmo exemplo e escolha uma abordagem.
3. [ ] Defina contratos de dados para incidentes e clientes: campos, tipos, chave e frequência.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Crie estrutura de pastas `raw`, `processed`, `curated` e regras de nomenclatura.
- [ ] Liste cinco falhas possíveis e como detectar cada uma.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-086-etl-elt-e-arquitetura-basica.py`:** Adicione à arquitetura uma área quarantine entre raw e processed para linhas sem id ou com tipo inválido.
- [ ] **Em `01-exercicios/dia-086-etl-elt-e-arquitetura-basica.py`:** Simule ausência da coluna id e uma execução repetida; descreva em qual etapa cada problema deve ser detectado.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual controle de qualidade é mais útil em **ETL/ELT e arquitetura básica**?

- [ ] A) Verificar somente o tamanho do arquivo final.
- [ ] B) Remover registros problemáticos sem contabilizá-los.
- [ ] C) Validar esquema, chaves, nulidade, faixas, duplicidades e volume em pontos definidos do fluxo.
- [ ] D) Conferir apenas se o processo terminou sem erro.
- [ ] E) Aceitar qualquer alteração de esquema automaticamente.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** O que melhora a observabilidade de uma solução de **ETL/ELT e arquitetura básica**?

- [ ] A) Logs estruturados, métricas, alertas e identificação clara de cada execução e etapa.
- [ ] B) Mensagens genéricas como 'deu erro'.
- [ ] C) Ocultar falhas e repetir o processo indefinidamente.
- [ ] D) Registrar somente o horário de início.
- [ ] E) Depender da observação manual da pasta de saída.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de dados para **ETL/ELT e arquitetura básica**.

- A) Monitorar qualidade, volume, duração e falhas.
- B) Extrair os dados com identificação da execução.
- C) Validar e transformar preservando rastreabilidade.
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
