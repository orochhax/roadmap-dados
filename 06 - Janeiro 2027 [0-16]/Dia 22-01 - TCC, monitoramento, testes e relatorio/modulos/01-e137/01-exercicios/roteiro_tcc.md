# TCC — roteiro de testes, monitoramento e relatório

> Preencha com artefatos executados. Todo cenário simulado deve continuar identificado como simulado.

## 1. Inventário reproduzível

- versão/hash dos dados:
- versão do código:
- ambiente/dependências:
- experimento e runs MLflow:
- champion/challenger antes da auditoria:
- comando único ou sequência curta de reprodução:

## 2. Matriz de testes

| Categoria | Caso | Resultado esperado | Resultado observado | Passou? | Arquivo do teste |
|---|---|---|---|---|---|
| schema |  |  |  |  |  |
| chave/data |  |  |  |  |  |
| leakage temporal |  |  |  |  |  |
| campo pós-tratamento |  |  |  |  |  |
| recall@K |  |  |  |  |  |
| efeito/ganho por 100 |  |  |  |  |  |
| custo indefinido |  |  |  |  |  |

## 3. Auditoria do MLflow

| Papel | Run/modelo | Dados | Métricas reconciliadas? | Artefato carregável? | Decisão |
|---|---|---|---|---|---|
| champion |  |  |  |  |  |
| challenger |  |  |  |  |  |

- inconsistência encontrada:
- correção aplicada:
- evidência após correção:

## 4. Monitoramento temporal simulado

| Janela | N | prevalência | qualidade de dados | PR-AUC | recall@K | calibração | alerta |
|---|---:|---:|---|---:|---:|---:|---|
| referência |  |  |  |  |  |  |  |
| atual simulada |  |  |  |  |  |  |  |

- slices monitorados:
- métricas sem rótulo imediato:
- métricas após chegada do rótulo:
- limiares de alerta:
- por que drift isolado não dispara retreino automático:

## 5. Retreino e promoção simulados

- gatilho simulado:
- nova janela de treino:
- dados que permaneceram intocados para comparação:
- run do challenger retreinado:

| Critério | Champion | Challenger | Limite | Passou? |
|---|---:|---:|---:|---|
| PR-AUC |  |  |  |  |
| recall@K |  |  |  |  |
| calibração |  |  |  |  |
| slice crítico |  |  |  |  |
| latência/custo |  |  |  |  |

- decisão de promoção ou rejeição:
- justificativa:

## 6. Rollback simulado

- versão promovida:
- falha controlada ou critério violado:
- versão de retorno:
- passos executados:
- verificação após rollback:
- evidência do MLflow/log:

## 7. Relatório e visual compacto

- caminho do relatório de 4–6 páginas:
- caminho do resumo executivo:
- gráficos/tabelas incluídos:
- números reconciliados com outputs:
- maior resultado negativo:
- limite de inferência mais importante:

## 8. Revisão de linguagem

- frase que declara dados/piloto sintéticos:
- frase que separa risco e efeito incremental:
- afirmação exagerada removida:
- motivo para não construir uma aplicação grande:

## Aceite

- [ ] Testes cobrem caminho válido e falhas controladas.
- [ ] Monitoramento, retreino e rollback estão marcados como simulações.
- [ ] Champion/challenger reconciliam com MLflow e relatório.
- [ ] Nenhuma conclusão extrapola os dados sintéticos.
