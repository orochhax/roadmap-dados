# Exceções e validação

## Aprenda agora

Validação verifica regras do dado; exceção trata uma operação que pode falhar. Retorne todos os erros da linha para não interromper o arquivo no primeiro problema.

```python
def validar_linha(linha):
    erros = []
    try:
        duracao = int(linha["duracao_min"])
        if duracao < 0:
            erros.append("duração negativa")
    except (KeyError, TypeError, ValueError):
        erros.append("duração inválida")
    return erros
```

**Erro comum:** envolver o programa inteiro em um único `try/except` e esconder a operação que realmente falhou.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-008-excecoes-e-validacao.py`.
- **Dados:** cenários e valores já preenchidos no arquivo principal.

## Núcleo essencial

1. [ ] Use uma cópia pequena do CSV com quatro erros diferentes e implemente `validar_linha()` para retornar os problemas encontrados.
2. [ ] Aplique `try/except` somente nas conversões que podem falhar, sem envolver o programa inteiro.
3. [ ] Separe linhas válidas e rejeitadas sem interromper o processamento no primeiro erro.
4. [ ] No mesmo arquivo, implemente `calcular_taxa(resolvidos, total)` e trate `total == 0`, texto no lugar de número e valores negativos; teste com `(82, 100)`, `(0, 0)` e `("x", 10)`.

## Prática obrigatória

- [ ] Grave os dois CSVs de saída apenas depois de validar corretamente a lista em memória.
- [ ] Repita um mesmo id em duas linhas válidas e envie a segunda ocorrência para `dados_rejeitados.csv`.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.
