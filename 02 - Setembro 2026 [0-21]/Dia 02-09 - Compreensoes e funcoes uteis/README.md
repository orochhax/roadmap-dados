# Compreensões e funções úteis

## Aprenda agora

Uma *comprehension* cria uma coleção a partir de outra; `enumerate`, `zip`, `sorted`, `any` e `all` evitam laços auxiliares comuns.

```python
incidentes = [{"cidade": "Salvador", "duracao": 80}, {"cidade": "Feira", "duracao": 20}]
longos = [item for item in incidentes if item["duracao"] > 60]
ranking = sorted(incidentes, key=lambda item: item["duracao"], reverse=True)
tem_critico = any(item["duracao"] > 60 for item in incidentes)
duracoes_validas = all(item["duracao"] >= 0 for item in incidentes)
```

**Erro comum:** compactar filtro, transformação e várias condições em uma única expressão difícil de explicar.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/comprehensions.py`.
- **Dados:** cenários e valores já preenchidos no arquivo principal.

## Núcleo essencial

1. [ ] Crie uma lista de 20 incidentes e gere com list comprehension apenas os P1/P2 com duração superior a 60 minutos.
2. [ ] Crie um dicionário por comprehension no formato `{cidade: total_de_incidentes}` e compare com a solução usando laço tradicional.
3. [ ] Use `enumerate` para numerar um ranking, `zip` para combinar cidades e metas, `sorted` com `key` para ordenar por duração, `any` para detectar P1 e `all` para validar durações não negativas.

## Prática obrigatória

- [ ] Escreva três versões da mesma transformação: laço, comprehension legível e comprehension excessivamente compacta; explique qual manteria em produção.
- [ ] Crie cinco testes com lista vazia, cidade repetida, duração zero, valor negativo e prioridade inválida.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.
