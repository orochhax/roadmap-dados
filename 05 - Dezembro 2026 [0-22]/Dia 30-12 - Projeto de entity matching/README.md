# Entrega real: Entity Matching Lab

**Data de estudo:** 30/12/2026  
**Carga planejada:** 2 a 4 horas

## Como estudar

Você pode escolher vídeo, documentação, site ou IA. Pesquise os nomes abaixo, faça uma primeira tentativa sem solução pronta e guarde evidência executável.

## Assuntos para pesquisar

### Bloco 1 — Entrega real: Entity Matching Lab

Pesquise exatamente:

- `entity resolution benchmark`
- `model card`
- `error taxonomy`
- `human review threshold`

Depois siga o [guia e os enunciados deste bloco](<modulos/01-n18/README.md>). Tente os exercícios antes de procurar uma implementação completa.

## Integração

Explique com suas palavras como os blocos se conectam em um fluxo de dados ou decisão. Execute um caso comum e um caso de borda de cada bloco e registre comandos, saídas e dúvidas nas evidências.


## Entrega real de portfólio

**Entity Matching Lab — benchmark ponta a ponta**

Siga o [brief do projeto](<../../projetos/entity-matching-lab/README.md>). A entrega precisa ter problema e usuário definidos, data card, dados reproduzíveis, baseline, métricas escolhidas antes do resultado, análise de erros, testes, README em português e inglês e apresentação de 2–3 minutos em inglês. Documente também resultados negativos.

## Publicação da semana no LinkedIn

- **Tema específico:** Entity Matching Lab — comparação completa entre regras, fuzzy matching, TF-IDF, embeddings e ranking com revisão humana.
- **Tipo:** entrega.
- **Formato:** carrossel de benchmark acompanhado de uma demonstração de até 90 segundos e link do repositório.
- **Artefato/evidência exigida:** pipeline reproduzido por um comando, baseline e abordagem final no mesmo teste, Recall@5/MRR/precisão/taxa de revisão, latência/custo, taxonomia de erros, data card, model card e checklist N18 preenchido.

### Roteiro para preencher

- **Problema e usuário:** [qual vínculo precisa ser decidido e quem revisa ambiguidades?]
- **Evolução das abordagens:** [o que mudou de regras até embeddings/ranking?]
- **Benchmark:** [quais métricas e valores foram obtidos no teste congelado?]
- **Operação:** [latência, custo e faixa de revisão humana]
- **Erro mais perigoso:** [falso merge, falso split ou falha de recuperação e sua causa]
- **Decisão:** [qual abordagem foi escolhida ou rejeitada e por quê?]
- **Link:** [repositório, relatório e demonstração conferidos]

### Limitação obrigatória

Declare o limite do benchmark, a diferença entre métrica offline e impacto de negócio e o tipo de dado real que ainda exigiria validação.

### Cuidado contra afirmações falsas

Não afirme automação em produção, escala empresarial ou economia observada. Se a abordagem avançada perdeu para o baseline, publique essa conclusão sem selecionar exemplos favoráveis. A publicação não altera Competências ou headline por si só.

### Checklist de publicação

- [ ] Reproduzi o pipeline em instalação ou pasta limpa.
- [ ] Mantive o mesmo teste e conjunto de candidatos nas comparações.
- [ ] Reconciliei qualidade, latência, custo e imagens/tabelas publicadas.
- [ ] Incluí um erro, uma limitação e a política de revisão humana.
- [ ] Removi dados pessoais, segredos e artefatos sem licença.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Concluído quando

- [ ] Estudei todos os assuntos e concluí os enunciados dos blocos sem copiar uma solução completa.
- [ ] Executei os artefatos, testei casos de borda e registrei resultados verificáveis.
- [ ] Expliquei a conexão entre os blocos, a decisão tomada e pelo menos uma limitação concreta.
