# Visão computacional II: detecção, segmentação, IoU, mAP e Dice

**Data de estudo:** 18/11/2026  
**Carga planejada:** 2 a 4 horas

## Como estudar

Você pode escolher vídeo, documentação, site ou IA. Pesquise os nomes abaixo, faça uma primeira tentativa sem solução pronta e guarde evidência executável.

## Assuntos para pesquisar

### Bloco 1 — Visão computacional II: detecção, segmentação, IoU, mAP e Dice

Pesquise exatamente:

- `object detection vs segmentation`
- `IoU`
- `mAP`
- `Dice coefficient`

Depois siga o [guia e os enunciados deste bloco](<modulos/01-n22/README.md>). Tente os exercícios antes de procurar uma implementação completa.

## Integração

Explique com suas palavras como os blocos se conectam em um fluxo de dados ou decisão. Execute um caso comum e um caso de borda de cada bloco e registre comandos, saídas e dúvidas nas evidências.


## Entrega real de portfólio

**Intelligent Support Operations — triagem visual**

Siga o [brief do projeto](<../../projetos/assistente-suporte-ia/extensao-visao-computacional/README.md>). A entrega precisa ter problema e usuário definidos, data card, dados reproduzíveis, baseline, métricas escolhidas antes do resultado, análise de erros, testes, README em português e inglês e apresentação de 2–3 minutos em inglês. Documente também resultados negativos.

## Publicação da semana no LinkedIn

- **Tema específico:** avaliação de uma triagem visual que localiza defeitos em ativos, comparando baseline, detecção e segmentação sem esconder erros.
- **Tipo:** entrega.
- **Formato:** carrossel visual com sobreposições de verdade e previsão, acompanhado de uma tabela curta de métricas.
- **Artefato/evidência exigida:** `modulos/01-n22/01-exercicios/avaliar_segmentacao.py` executado, evidências preenchidas, teste manual de IoU/Dice, resultados por classe/tamanho, latência em CPU e imagens cuja licença permita publicação.

### Roteiro para preencher

- **Problema operacional:** [qual defeito precisa ser localizado e qual erro é mais caro?]
- **Dataset e licença:** [qual fonte foi usada e por que as imagens podem ser mostradas?]
- **Baseline e modelos avaliados:** [quais abordagens foram comparadas no mesmo split?]
- **Resultado verificável:** [mAP, AP50, IoU, Dice, recall crítico ou latência, com caminho da evidência]
- **Erro visual:** [qual imagem representa o erro mais importante e o que ele ensina?]
- **Decisão:** [protótipo aceito, rejeitado ou encaminhado para revisão humana, e por quê?]
- **Link:** [repositório, relatório ou demonstração conferidos]

### Limitação obrigatória

Declare a diferença entre o conjunto de imagens usado e ativos reais de telecom, incluindo o risco de mudança de domínio.

### Cuidado contra afirmações falsas

Não chame um experimento com dados públicos ou proxy de sistema implantado em campo. Não publique imagens, anotações ou pesos sem licença. Esta publicação não antecipa Competências nem alteração de headline.

### Checklist de publicação

- [ ] Validei o split por ativo/grupo e os testes manuais de IoU e Dice.
- [ ] Recalculei as métricas exibidas e mantive o baseline visível.
- [ ] Selecionei exemplos de erro representativos, sem escolher apenas acertos.
- [ ] Confirmei licença e ausência de dados sensíveis em todas as imagens.
- [ ] Registrei latência, decisão operacional e limitação de domínio.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Concluído quando

- [ ] Estudei todos os assuntos e concluí os enunciados dos blocos sem copiar uma solução completa.
- [ ] Executei os artefatos, testei casos de borda e registrei resultados verificáveis.
- [ ] Expliquei a conexão entre os blocos, a decisão tomada e pelo menos uma limitação concreta.
