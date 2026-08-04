<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 49 — Feature engineering para regressão — 08/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Feature engineering para regressão** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Feature engineering para regressão.
- **Pasta/arquivo principal:** `semana-10/dia-049-feature-engineering-para-regressao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Crie features de data: mês, dia da semana, fim de semana e dias desde primeira compra.
2. [ ] Crie transformações `log1p` para variável assimétrica e interações entre desconto e canal.
3. [ ] Agrupe categorias raras com limiar explícito e documente impacto.
4. [ ] Construa cada feature dentro da pipeline para evitar diferenças entre treino e inferência.
5. [ ] Faça ablação: remova grupos de features e registre quanto cada grupo muda a métrica.

### Verificação prática sem consulta
- [ ] Treine ou avalie novamente o componente central de **Feature engineering para regressão** em um notebook limpo.
- [ ] Mude seed, limiar ou uma feature e registre se a conclusão permanece estável.
- [ ] Explique qual erro técnico produziria uma métrica artificialmente boa.

### Perguntas de checagem
1. Como criar atributos úteis sem inserir informação futura ou relação artificial?

**Resposta:**

2. Em qual exercício de **Feature engineering para regressão** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Feature engineering para regressão** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Commit realizado com mensagem no formato `dia-049: feature-engineering-para-regressao`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

---

## Anotações pessoais

### Resultado esperado antes de executar


### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação
