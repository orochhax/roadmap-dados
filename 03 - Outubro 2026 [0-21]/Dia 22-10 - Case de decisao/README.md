# Case de decisao

**Data de estudo:** 22/10/2026  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Case de decisao

#### O que pesquisar
- `Case de decisao Python explicado passo a passo`
- `Case de decisao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-case-de-decisao`](<atividades/01-case-de-decisao/>)

#### O que você precisa entender

Uma política converte probabilidade, custo e capacidade operacional em ação. Casos próximos ao limiar podem ser encaminhados à revisão humana.

```python
decisao = np.select(
    [probabilidade >= 0.70, probabilidade >= 0.45],
    ["agir", "revisar"],
    default="não agir",
)
```

**Erro comum:** escolher uma única política global sem conferir custo e taxa de ação por segmento.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-case-de-decisao/roteiro_atividades.md`.
- **Starter executável:** `atividades/01-case-de-decisao/case_decisao.py`. A primeira execução usa probabilidades sintéticas somente para desenvolver a política; substitua-as por `predict_proba` antes de avaliar um modelo.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.
- **Entradas concretas:** id do cliente, probabilidade de churn, alvo real e custos de ação, falso positivo e falso negativo.
- **Fallback local:** se não houver probabilidades salvas, ajuste no próprio notebook a pipeline de regressão logística mostrada acima e use `predict_proba(X_validacao)[:, 1]`.

#### O que fazer

- [ ] Monte tabela com cliente, probabilidade, limiar, decisão e custo esperado.
- [ ] Crie três políticas: conservadora, equilibrada e agressiva; calcule volume de ações e custo.
- [ ] Analise desempenho por cidade, plano e faixa de mensalidade.
- [ ] Defina regra de revisão humana para casos próximos ao limiar.

- [ ] Apresente decisão em uma página, incluindo quem não deve receber ação automatizada.


- [ ] **Em `atividades/01-case-de-decisao/case_decisao.py`:** defina política conservadora com limiar 0,70, equilibrada com 0,50 e agressiva com 0,30; calcule volume e custo no mesmo conjunto e registre a tabela no roteiro.
- [ ] **Em `atividades/01-case-de-decisao/case_decisao.py`:** crie revisão humana para probabilidades entre 0,45 e 0,55, conte quantos clientes entram nessa faixa e registre a regra no roteiro.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
