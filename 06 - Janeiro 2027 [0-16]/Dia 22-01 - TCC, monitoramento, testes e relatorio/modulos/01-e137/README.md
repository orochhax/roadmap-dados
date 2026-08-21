# TCC — testes, observabilidade e ciclo de vida

## Objetivo

Provar que os resultados do TCC são reproduzíveis e que existe uma resposta segura quando dados ou desempenho mudam. A sessão fecha o ciclo de vida mínimo sem construir uma aplicação grande.

## Preparação

- **Enunciado local:** `01-exercicios/roteiro_tcc.md`.
- **Projeto canônico:** `projetos/telecom-customer-intelligence/`.
- **Entradas:** datasets/versionamento, runs MLflow, champion/challenger, análise do piloto e métricas de custo.
- **Saídas esperadas:** testes em `tests/`, monitoramento em `outputs/`, relatório/model card em `docs/` e execução reproduzível.

## Pesquise exatamente

- `pytest data validation schema tests pandas`
- `temporal leakage unit test machine learning`
- `metric implementation unit test precision recall calibration`
- `MLflow model registry champion challenger rollback`
- `model monitoring data drift performance drift calibration`
- `retraining trigger model rollback runbook`

## Núcleo essencial

1. [ ] Implemente testes de schema, chave, datas, leakage temporal e campos pós-tratamento.
2. [ ] Implemente casos pequenos com oráculo conhecido para PR-AUC/recall@K ou métricas auxiliares e efeito/ganho por 100.
3. [ ] Faça uma auditoria dos runs no MLflow e reconcilie champion/challenger com o relatório.
4. [ ] Crie uma janela temporal posterior sintética para monitorar qualidade, distribuição, PR-AUC, recall@K e calibração quando houver rótulo.
5. [ ] Defina gatilhos de alerta sem tratar drift isolado como ordem automática de retreino.
6. [ ] Simule retreino, compare challenger no protocolo congelado e promova somente se os critérios forem cumpridos.
7. [ ] Simule rollback para o champion anterior e registre versão, motivo e verificação.
8. [ ] Produza relatório de 4–6 páginas, resumo executivo e visual estático/compacto.

## Visual mínimo

- funil dos dados e capacidade;
- comparação dos três modelos;
- curva/tabela de calibração e recall@K;
- efeito do piloto com intervalo;
- ganho por 100 e custo por retenção;
- slices e evolução temporal.

## Regras

- Teste precisa possuir entrada, resultado esperado e resultado observado.
- Janela de monitoramento, retreino e rollback devem ser rotulados como simulação.
- O challenger não vence apenas por uma métrica; considere calibração, slices, latência e custo.
- Nenhum painel deve sugerir impacto real ou esconder incerteza.
- Não construa API, frontend ou infraestrutura de nuvem para este TCC.

## Concluído quando

- [ ] Testes falham nos casos inválidos e passam no caminho válido.
- [ ] Monitoramento temporal e runs MLflow são reproduzíveis.
- [ ] Promoção, retreino e rollback simulados possuem critérios e evidências.
- [ ] Relatório e visual reconciliam métricas preditivas, causais e de custo.
