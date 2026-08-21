# TCC — release, banca e comunicação profissional

## Objetivo

Congelar e publicar uma release reproduzível do TCC, defender escolhas técnicas e traduzir o trabalho para candidaturas sem transformar simulação em experiência profissional.

## Conquista para o LinkedIn

- Revise Sobre, Competências, Projetos e Destaques somente com links e evidências verificadas.
- Adapte `[cargo ou área atual verdadeira] | Em formação em Ciência de Dados | [duas ou três competências comprovadas]` ao contexto registrado em [LinkedIn — perfil atual](<../../../../00 - Recursos Compartilhados/linkedin-perfil-atual.md>).
- Adicione competências apenas se os artefatos correspondentes estiverem executados e você conseguir defendê-los.
- **Comunicação técnica em inglês** exige apresentação e respostas próprias, não apenas um template preenchido.
- Use o [Guia de LinkedIn e evidências](<../../../../00 - Recursos Compartilhados/linkedin-e-evidencias.md>).

## Preparação

- **Enunciado local:** `01-exercicios/roteiro_tcc.md`.
- **Projeto canônico:** `projetos/telecom-customer-intelligence/`.
- **Entradas:** release candidata, dados sintéticos manifestados, relatório, runs MLflow, testes, materiais de banca e instruções.
- **Fallback:** vídeo ou capturas substituem hospedagem; execução em ambiente limpo continua obrigatória.

## Pesquise exatamente

- `machine learning reproducibility clean environment release`
- `data science thesis defense model limitations`
- `portfolio project synthetic data disclosure`
- `technical presentation English machine learning project`
- `STAR method data science project interview`

## Núcleo essencial

1. [ ] Execute o projeto em clone/pasta limpa usando somente o README.
2. [ ] Reproduza dados, benchmark, piloto, testes, monitoramento e relatório sem etapa manual oculta.
3. [ ] Crie release com versão, dependências, data card, model card, resultados e limitações.
4. [ ] Faça defesa de 8–10 minutos e responda usando artefatos do escopo congelado.
5. [ ] Atualize `README.en.md` com 150–250 palavras e resultados reais da própria execução.
6. [ ] Prepare `docs/presentation-en.md` e grave apresentação em inglês de 2–3 minutos.
7. [ ] Publique apenas depois de conferir links, ausência de dados pessoais/segredos e declaração sintética.
8. [ ] Envie três candidaturas compatíveis, adaptando palavras-chave sem inventar experiência.

## Fora do escopo

Não adicione controle sintético, nuvem nova, LLM, entity matching, forecasting ou aplicação grande para “valorizar” a entrega final.

## Banco de perguntas de banca

1. Qual decisão, data de corte, horizonte e capacidade foram congelados?
2. Por que risco de churn não equivale a resposta à campanha?
3. Como você provou que não houve leakage temporal ou pós-tratamento?
4. Qual baseline foi mais difícil de superar e por quê?
5. Por que PR-AUC e recall@K são adequados à capacidade?
6. Como avaliou e usou calibração?
7. Como os dados sintéticos foram gerados e quais vieses isso introduz?
8. Como a randomização simulada sustenta o efeito por intenção de tratar?
9. O que significa um intervalo de confiança que cruza zero?
10. Como calculou ganho por 100 contatos e custo por retenção quando o efeito é incerto?
11. Quais slices não permitem conclusão por falta de amostra?
12. Como MLflow sustenta champion/challenger e reprodução?
13. Quais gatilhos iniciam retreino e rollback simulados?
14. Qual é a maior limitação e qual evidência permitiria contestar seu resultado?

## Concluído quando

- [ ] Uma pessoa externa reproduz a release apenas com as instruções.
- [ ] A banca usa evidências e reconhece resultados negativos/inconclusivos.
- [ ] README PT/EN, relatório, MLflow e apresentação estão reconciliados.
- [ ] Publicação e candidaturas deixam claro o caráter educacional e sintético.
