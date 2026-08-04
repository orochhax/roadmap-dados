<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 65 — Auditoria do pipeline — 30/10/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Auditoria do pipeline.
- **Competência sugerida:** Auditoria e pipelines de Machine Learning.
- **Ação recomendada:** Após concluir todas as atividades do dia, atualize o título profissional e adicione ou reforce **Auditoria e pipelines de Machine Learning** na seção Competências. Se a entrega estiver revisada e apresentável, inclua-a também em Projetos ou Destaques.
- **Novo título sugerido:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Auditoria do pipeline** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 4–5 horas; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Auditoria do pipeline.
- **Pasta/arquivo principal:** `projeto-mensal/src/train.py`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Execute checklist de auditoria: definição do alvo, split, leakage, pipeline, métricas, tuning, calibração, segmentos e reprodutibilidade.
2. [ ] Rode notebook do zero em kernel limpo e corrija células fora de ordem.
3. [ ] Converta partes estáveis em scripts `train.py`, `evaluate.py` e `features.py`.
4. [ ] Use linter ou revisão manual para encontrar código duplicado, variáveis globais e caminhos fixos.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Crie `auditoria_modelo.md` com problemas encontrados, severidade, correção e evidência.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `projeto-mensal/src/train.py`:** Acrescente à auditoria uma checagem que procure caminhos absolutos contendo C:\Users e classifique a severidade.
- [ ] **Em `projeto-mensal/src/train.py`:** Rode train.py duas vezes com seed 42 e compare as métricas salvas para verificar reprodutibilidade.

### Perguntas de checagem
1. Quais pontos do pipeline você verificaria para detectar leakage, inconsistência e baixa reprodutibilidade?
2. Em qual exercício de **Auditoria do pipeline** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.
3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?
4. Como o conhecimento de **Auditoria do pipeline** seria usado para apoiar uma decisão real em dados ou IA?
5. Que vazamento ou escolha de validação poderia produzir um resultado artificialmente bom neste dia?
6. Qual troca entre métricas mudaria a decisão de negócio e por quê?

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Respondi pelo menos três das seis perguntas de checagem com justificativa própria.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`



---
