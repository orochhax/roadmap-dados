<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 65 — Auditoria do pipeline — 30/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Auditoria do pipeline** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Auditoria do pipeline.
- **Pasta/arquivo principal:** `projeto-mensal/src/train.py`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Execute checklist de auditoria: definição do alvo, split, leakage, pipeline, métricas, tuning, calibração, segmentos e reprodutibilidade.
2. [ ] Rode notebook do zero em kernel limpo e corrija células fora de ordem.
3. [ ] Converta partes estáveis em scripts `train.py`, `evaluate.py` e `features.py`.
4. [ ] Use linter ou revisão manual para encontrar código duplicado, variáveis globais e caminhos fixos.
5. [ ] Crie `auditoria_modelo.md` com problemas encontrados, severidade, correção e evidência.

### Exercícios extras
> Os enunciados também estão preparados em `projeto-mensal/src/train.py`. Faça exatamente estes dois itens.

- [ ] **Em `projeto-mensal/src/train.py`:** Acrescente à auditoria uma checagem que procure caminhos absolutos contendo C:\Users e classifique a severidade.
- [ ] **Em `projeto-mensal/src/train.py`:** Rode train.py duas vezes com seed 42 e compare as métricas salvas para verificar reprodutibilidade.

### Perguntas de checagem
1. Quais pontos do pipeline você verificaria para detectar leakage, inconsistência e baixa reprodutibilidade?

**Resposta:**

2. Em qual exercício de **Auditoria do pipeline** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Auditoria do pipeline** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

5. Que vazamento ou escolha de validação poderia produzir um resultado artificialmente bom neste dia?

**Resposta:**

6. Qual troca entre métricas mudaria a decisão de negócio e por quê?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

> [!important] Projeto mensal robusto — Motor de Decisão de Churn
> **Desafio:** Entregar um sistema completo que classifique risco, explique fatores e recomende uma ação de retenção.
>
> **Deve reutilizar:** Tudo das semanas 1–13.
>
> **Entregáveis obrigatórios:**
> - [ ] SQL ou pipeline de base;
> - [ ] EDA e features;
> - [ ] validação e tuning;
> - [ ] limiar orientado a custo;
> - [ ] explicabilidade;
> - [ ] dashboard/API e defesa;
>
> **Defesa:** apresentação de 8–15 minutos, seguida de cinco perguntas críticas respondidas sem ler o README.
>
> **Nota mínima recomendada:** `7/10`. Abaixo disso, reserve um bloco de correção na segunda-feira seguinte.

> [!check] Critério para avançar
> Seu pipeline pode ser executado novamente sem intervenção manual e suas conclusões continuam defensáveis?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Auditoria do pipeline.
- **Competência sugerida:** Auditoria e pipelines de Machine Learning.
- **Ação recomendada:** Após concluir todas as atividades do dia, atualize o título profissional e adicione ou reforce **Auditoria e pipelines de Machine Learning** na seção Competências. Se a entrega estiver revisada e apresentável, inclua-a também em Projetos ou Destaques.
- **Novo título sugerido:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
