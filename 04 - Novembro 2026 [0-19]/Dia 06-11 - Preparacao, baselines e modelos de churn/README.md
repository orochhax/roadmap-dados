# Preparacao para modelagem + Baselines e modelos

**Data de estudo:** 06/11/2026  
**Carga planejada:** 4 a 5 horas

## Como estudar

Você pode escolher vídeo, documentação, site ou IA. Pesquise os nomes abaixo, faça uma primeira tentativa sem solução pronta e guarde evidência executável.

## Assuntos para pesquisar

### Bloco 1 — Preparacao para modelagem

Pesquise exatamente:

- `Preparacao para modelagem Python explicado passo a passo`
- `Preparacao para modelagem Python exercícios práticos`

Depois siga o [guia e os enunciados deste bloco](<modulos/01-e76/README.md>). Tente os exercícios antes de procurar uma implementação completa.

### Bloco 2 — Baselines e modelos

Pesquise exatamente:

- `Baselines e modelos machine learning com Python explicado passo a passo`
- `Baselines e modelos machine learning com Python exercícios práticos`

Depois siga o [guia e os enunciados deste bloco](<modulos/02-e77/README.md>). Tente os exercícios antes de procurar uma implementação completa.

## Integração

Explique com suas palavras como os blocos se conectam em um fluxo de dados ou decisão. Execute um caso comum e um caso de borda de cada bloco e registre comandos, saídas e dúvidas nas evidências.

## Publicação da semana no LinkedIn

- **Tema específico:** da auditoria ao primeiro baseline confiável de churn — alvo temporal, qualidade, SQL/EDA e pipeline sem vazamento.
- **Tipo:** progresso.
- **Formato:** carrossel problema → achado da auditoria → correção → baseline → próximo teste.
- **Artefato/evidência exigida:** `auditoria_modelo.md`, definição temporal do alvo, checks de qualidade, consulta/EDA do churn, split congelado, baseline e modelo inicial executados durante 03–06/11.

### Roteiro para preencher

- **Problema e alvo:** [quem é previsto, em qual data e em qual horizonte?]
- **Achado da auditoria:** [qual risco de leakage, caminho fixo ou estado oculto foi encontrado?]
- **Correção e prova:** [qual alteração foi feita e qual teste comprova a correção?]
- **Dados/EDA:** [qual problema de qualidade ou padrão relevante apareceu?]
- **Baseline:** [qual referência simples foi executada e qual resultado observou?]
- **Estado atual:** [o que falta para política, segmentos, dashboard e release de 12/11?]
- **Evidência:** [relatório, script ou saída conferidos]

### Limitação obrigatória

Explique que o projeto de churn ainda está em construção e que um baseline offline não define sozinho uma política de retenção.

### Cuidado contra afirmações falsas

Não publique resultado como release final, não afirme previsão em produção nem impacto sobre clientes. Chame o trabalho de auditoria e baseline em progresso. O post não antecipa Competências ou headline.

### Checklist de publicação

- [ ] Reexecutei o pipeline duas vezes com a seed registrada.
- [ ] Confirmei alvo, datas, split e ausência dos sinais pós-evento.
- [ ] Mostrei um achado, a correção e a evidência do teste.
- [ ] Mantive baseline e limitações visíveis.
- [ ] Removi dados sensíveis, caminhos locais e links privados.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Concluído quando

- [ ] Estudei todos os assuntos e concluí os enunciados dos blocos sem copiar uma solução completa.
- [ ] Executei os artefatos, testei casos de borda e registrei resultados verificáveis.
- [ ] Expliquei a conexão entre os blocos, a decisão tomada e pelo menos uma limitação concreta.
