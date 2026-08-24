# Publicacao e apresentacao

**Data de estudo:** 12/11/2026  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Publicacao e apresentacao

#### O que pesquisar
- `Publicacao e apresentacao Python explicado passo a passo`
- `Publicacao e apresentacao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-publicacao-e-apresentacao`](<atividades/01-publicacao-e-apresentacao/>)

#### Conquista para o LinkedIn

- **Projetos ou Destaques:** depois de testar a release em ambiente limpo, publique o projeto de churn com repositório, demonstração, resultado e limitação.
- **Sobre:** revise o texto apenas para mencionar a entrega completa e reproduzível; não transforme o resultado educacional em impacto empresarial.
- O README e a apresentação em inglês são evidências de prática, mas ainda não comprovam inglês avançado. Siga o [Guia de LinkedIn e evidências](<../../00 - Recursos Compartilhados/linkedin-e-evidencias.md>).

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-publicacao-e-apresentacao/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** entrega reproduzível fixa dependências, comando e versão; ambiente limpo prova independência da máquina original.
- **Exemplo mínimo:** crie o ambiente de teste em `$env:TEMP`, fora do OneDrive; ative-o, rode `python -m pip install -r requirements.txt` e execute o comando do README.
- **Erro comum:** publicar notebook sem versões, dados permitidos, comando e teste limpo.

#### O que fazer

- [ ] Limpe o repositório, fixe dependências e rode tudo em ambiente novo.
- [ ] Crie README com instalação, estrutura, resultados e decisões.
- [ ] Publique release e grave demo de 8–10 minutos.
- [ ] Responda por escrito a cinco perguntas de banca sobre leakage, métrica, custo, viés e implantação.
- [ ] Escreva `atividades/01-publicacao-e-apresentacao/projeto-semanal/README.en.md` em inglês, com 150–250 palavras, cobrindo problema, dados, método, resultados, limitações e reprodução.
- [ ] Prepare `atividades/01-publicacao-e-apresentacao/projeto-semanal/docs/presentation-en.md` como roteiro em inglês para uma apresentação falada de 2–3 minutos.

- [ ] Faça retrospectiva: três acertos, três falhas e três melhorias.


- [ ] **Em `atividades/01-publicacao-e-apresentacao/roteiro_atividades.md`:** Responda por escrito: 'Como você provou que status_atual não entrou no treino?' citando a etapa exata da pipeline.
- [ ] **Em `atividades/01-publicacao-e-apresentacao/roteiro_atividades.md`:** Clone em uma pasta nova, execute a instrução principal e registre qualquer etapa manual que ainda impeça reprodução.

#### Como validar

- O projeto foi executado, incluindo `README.en.md` e `docs/presentation-en.md`, e o roteiro contém todas as saídas obrigatórias.
- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Entrega real de portfólio

**Telecom Customer Intelligence — decisão de churn**

Siga o [brief do projeto](<../../projetos/telecom-customer-intelligence/README.md>). A entrega precisa ter problema e usuário definidos, data card, dados reproduzíveis, baseline, métricas escolhidas antes do resultado, análise de erros, testes, README em português e inglês e apresentação de 2–3 minutos em inglês. Documente também resultados negativos.

## Publicação da semana no LinkedIn

- **Tema específico:** release reproduzível do Telecom Customer Intelligence e a política de retenção derivada do projeto de churn.
- **Tipo:** entrega.
- **Formato:** carrossel de até seis páginas, acompanhado do link do repositório e de uma demonstração curta.
- **Artefato/evidência exigida:** release executada em ambiente limpo, dashboard ou relatório, métrica realmente observada, política de limiar/capacidade, análise de um erro e uma limitação registrada em `atividades/01-publicacao-e-apresentacao/projeto-semanal/`.

### Roteiro para preencher

- **Problema e usuário:** [qual decisão de retenção foi investigada e para quem?]
- **Dados e recorte:** [quais dados, período, alvo e divisão foram usados?]
- **Baseline e abordagem final:** [o que foi comparado no mesmo conjunto de avaliação?]
- **Resultado verificável:** [métrica, valor e caminho do artefato que comprova o número]
- **Decisão:** [qual política foi recomendada e qual restrição de capacidade foi considerada?]
- **Erro analisado:** [qual falso positivo, falso negativo ou segmento alterou sua interpretação?]
- **Link:** [repositório, relatório, dashboard ou demonstração conferidos]

### Limitação obrigatória

Explique por que o resultado educacional não comprova redução real de churn em uma operadora e qual validação ainda seria necessária.

### Cuidado contra afirmações falsas

Não diga que o modelo foi implantado em produção, gerou receita ou reduziu churn. Use os verbos `construí`, `avaliei` e `simulei` de acordo com o que a release realmente demonstra. Esta publicação não libera, por si só, novas Competências nem mudança de headline.

### Checklist de publicação

- [ ] Reexecutei a release em ambiente limpo usando apenas o README.
- [ ] Conferi cada número e imagem contra o relatório, dashboard ou arquivo de métricas.
- [ ] Mostrei uma comparação com baseline, um erro e uma limitação.
- [ ] Removi dados pessoais, segredos, caminhos locais e alegações de impacto empresarial.
- [ ] Testei todos os links em janela anônima.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
