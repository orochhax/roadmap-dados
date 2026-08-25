# Baseline completo

**Data de estudo:** 14/10/2026  
**Carga planejada:** 2 a 4 horas

## Aula selecionada no YouTube

- [ ] **Machine Learning 13: Prática no Python (Classificação)** (22:37), da trilha **Machine Learning — Téo Me Why** — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Machine+Learning+13+Pratica+no+Python+Classificacao+Teo+Me+Why).

Use a aula como demonstração. O baseline completo, o relatório e a comparação reproduzível do projeto semanal continuam sendo a prática obrigatória.

## Atividades do dia

### Atividade 1 — Baseline completo

#### O que pesquisar
- `Baseline completo Python explicado passo a passo`
- `Baseline completo Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-baseline-completo`](<atividades/01-baseline-completo/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-baseline-completo/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.
- **Experimento de leakage:** crie uma cópia com `status_vazado = churn`, treine a mesma pipeline com e sem essa coluna no mesmo split e compare a métrica.

#### O que fazer

- [ ] Treine `DummyClassifier`, uma regressão logística usada como baseline e uma regra de negócio no mesmo split.
- [ ] Avalie os três com a mesma função e registre as métricas em uma tabela.
- [ ] Analise seis erros representativos e escreva qual baseline qualquer candidato precisa superar.

- [ ] Execute o experimento de leakage descrito em Preparação e explique por que a versão vazada não representa uso real.
- [ ] Transforme a avaliação repetida em uma função reutilizável.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
