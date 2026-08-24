# Entrega real: Entity Matching Lab

**Data de estudo:** 30/12/2026  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Entrega real: Entity Matching Lab

#### O que pesquisar
- `entity resolution benchmark`
- `model card`
- `error taxonomy`
- `human review threshold`

**Arquivos da atividade:** [abrir a pasta `01-entrega-real-entity-matching-lab`](<atividades/01-entrega-real-entity-matching-lab/>)

#### Objetivo

Transformar os experimentos de normalização, baseline, geração de candidatos, embeddings e ranking em um produto de portfólio auditável. A entrega deve receber registros bagunçados, recuperar e ordenar candidatos, tomar decisões com abstenção e produzir um relatório que permita a uma pessoa técnica ou de negócio entender qualidade, custo, limites e riscos.

Esta sessão não serve para criar um quarto modelo. Ela serve para congelar contratos, reproduzir o melhor pipeline e demonstrar maturidade de avaliação.

#### Termos complementares para pesquisar

1. `entity resolution benchmark dataset train validation test`
2. `machine learning model card intended use limitations`
3. `data card dataset documentation schema provenance`
4. `entity resolution error taxonomy false merge false split`
5. `human in the loop confidence thresholds review queue`
6. `selective classification risk coverage curve`
7. `ML inference latency throughput cost benchmark`
8. `reproducible machine learning project README structure`

#### O que fazer

Use [o checklist e o enunciado](<atividades/01-entrega-real-entity-matching-lab/ENUNCIADO.md>) para integrar o que você construiu. Preencha `atividades/01-entrega-real-entity-matching-lab/checklist_entrega.md` sem apagar pendências e registre a auditoria final no próprio artefato.

O projeto precisa incluir também um README executivo curto em inglês; isso pratica comunicação profissional, não substitui seu estudo geral de inglês.

#### LinkedIn

Depois da publicação e somente se conseguir demonstrar cada etapa, adicione: **Entity Resolution**, **Machine Learning aplicado** e **Avaliação de modelos**. Use o projeto como evidência na seção “Projetos”.

## Entrega real de portfólio

**Entity Matching Lab — benchmark ponta a ponta**

Siga o [brief do projeto](<../../projetos/entity-matching-lab/README.md>). A entrega precisa ter problema e usuário definidos, data card, dados reproduzíveis, baseline, métricas escolhidas antes do resultado, análise de erros, testes, README em português e inglês e apresentação de 2–3 minutos em inglês. Documente também resultados negativos.

## Publicação da semana no LinkedIn

- **Tema específico:** Entity Matching Lab — comparação completa entre regras, fuzzy matching, TF-IDF, embeddings e ranking com revisão humana.
- **Tipo:** entrega.
- **Formato:** carrossel de benchmark acompanhado de uma demonstração de até 90 segundos e link do repositório.
- **Artefato/evidência exigida:** pipeline reproduzido por um comando, baseline e abordagem final no mesmo teste, Recall@5/MRR/precisão/taxa de revisão, latência/custo, taxonomia de erros, data card, model card e checklist final da entrega preenchido.

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

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
