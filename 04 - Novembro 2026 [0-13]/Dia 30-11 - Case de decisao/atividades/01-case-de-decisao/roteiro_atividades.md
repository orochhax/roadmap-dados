# Roteiro de atividades — Case de decisão

## Entradas

Use id do cliente, probabilidade de churn, alvo real e custos de ação, falso positivo e falso negativo. Se não houver probabilidades salvas, ajuste a regressão logística no próprio notebook e use `predict_proba(X_validacao)[:, 1]`.

## Requisitos principais

1. Monte uma tabela com cliente, probabilidade, limiar, decisão e custo esperado.
2. Crie políticas conservadora, equilibrada e agressiva; calcule volume de ações e custo.
3. Analise os resultados por cidade, plano e faixa de mensalidade.
4. Defina revisão humana para casos próximos ao limiar.
5. Registre a decisão em uma página, incluindo quem não deve receber ação automatizada.

## Comparação das políticas

| Política | Limiar | Ações | Custo total | Observação |
|---|---:|---:|---:|---|
| Conservadora |  |  |  |  |
| Equilibrada |  |  |  |  |
| Agressiva |  |  |  |  |

## Adaptação e verificação

- Use limiares 0,70, 0,50 e 0,30 nas três políticas e compare volume e custo no mesmo conjunto.
- Defina revisão humana entre 0,45 e 0,55 e conte os clientes nessa faixa.

## Decisão

- Política escolhida:
- Evidência:
- Regra de revisão humana:
- Grupo sem ação automatizada:
- Limitação:
