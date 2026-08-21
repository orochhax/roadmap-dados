# Condicionais e regras de negócio

## Objetivo

Usar uma única cadeia `if/elif/else` e entender por que a ordem das regras altera o resultado.

## Aprenda agora

Uma cadeia testa as condições em ordem e executa somente o primeiro bloco verdadeiro:

```python
pontuacao = 72

if pontuacao >= 90:
    faixa = "alta"
elif pontuacao >= 70:
    faixa = "média"
else:
    faixa = "baixa"
```

O `else` pertence à cadeia inteira. Com vários `if` independentes, mais de uma regra pode executar e o `else` pertence somente ao último `if`.

**Erro comum:** começar pela regra mais ampla; ela captura o caso antes que a regra específica seja testada.

## Prática

- [ ] Complete as regras em `01-exercicios/prioridade_chamados.py` com um `if`, os `elif` necessários e um `else` final.
- [ ] Execute os seis cenários obrigatórios e compare cada saída com o resultado indicado no arquivo.
- [ ] Explique por que 101 clientes em serviço crítico resultam em P1, enquanto exatamente 100 resultam em P3.

## Resultado esperado

Cada cenário produz somente uma prioridade e nenhuma regra posterior sobrescreve uma decisão anterior.

## Concluído quando

- [ ] Os seis cenários produzem a prioridade esperada.
- [ ] Você explica a diferença entre `> 100` e `>= 100`.
- [ ] Você explica o problema de usar vários `if` independentes nesse caso.

**Autoavaliação:** `__/5`
