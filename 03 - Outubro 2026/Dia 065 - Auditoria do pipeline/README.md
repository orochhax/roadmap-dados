<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 65 — Auditoria do pipeline — 30/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Auditoria do pipeline** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Auditoria do pipeline.
- **Pasta/arquivo principal:** `semana-13/dia-065-auditoria-do-pipeline/` (pasta do projeto).
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Execute checklist de auditoria: definição do alvo, split, leakage, pipeline, métricas, tuning, calibração, segmentos e reprodutibilidade.
2. [ ] Rode notebook do zero em kernel limpo e corrija células fora de ordem.
3. [ ] Converta partes estáveis em scripts `train.py`, `evaluate.py` e `features.py`.
4. [ ] Use linter ou revisão manual para encontrar código duplicado, variáveis globais e caminhos fixos.
5. [ ] Crie `auditoria_modelo.md` com problemas encontrados, severidade, correção e evidência.

### Verificação prática sem consulta
- [ ] Treine ou avalie novamente o componente central de **Auditoria do pipeline** em um notebook limpo.
- [ ] Mude seed, limiar ou uma feature e registre se a conclusão permanece estável.
- [ ] Explique qual erro técnico produziria uma métrica artificialmente boa.

### Perguntas de checagem
1. Quais pontos do pipeline você verificaria para detectar leakage, inconsistência e baixa reprodutibilidade?

**Resposta:**

2. Em qual exercício de **Auditoria do pipeline** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Auditoria do pipeline** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Commit realizado com mensagem no formato `dia-065: auditoria-do-pipeline`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

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

## Anotações pessoais

### Resultado esperado antes de executar


### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação
