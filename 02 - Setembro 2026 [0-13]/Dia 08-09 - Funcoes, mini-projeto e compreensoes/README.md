# Funcoes e primeiro mini-projeto + Compreensoes e funcoes uteis

**Data de estudo:** 08/09/2026
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Funcoes e primeiro mini-projeto

#### O que pesquisar
- `Funcoes e primeiro mini-projeto Python explicado passo a passo`
- `Funcoes e primeiro mini-projeto Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-funcoes-e-primeiro-mini-projeto`](<atividades/01-funcoes-e-primeiro-mini-projeto/>)

#### Aulas gratuitas

- [ ] Curso em Vídeo — Aula #20: **Funções, parte 1**.
- [ ] Curso em Vídeo — Aula #21: **Funções, parte 2**.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-funcoes-e-primeiro-mini-projeto/projeto-semanal/src/noc_insights.py`.
- **Dados:** use os incidentes já preenchidos no projeto.
- **Regra de prioridade:** P1 para risco de segurança, cidade inteira afetada ou serviço crítico com mais de 100 clientes; P2 para mais de 500 clientes ou duração acima de 180 minutos; P3 para mais de 50 clientes; P4 nos demais casos. A primeira regra verdadeira vence.

#### O que fazer

- [ ] Implemente `classificar_prioridade()` com parâmetros e retorno usando a regra acima.
- [ ] Em `noc_insights.py`, gere um relatório com contagem por cidade, média de duração e prioridade mais frequente, sem menu interativo nesta primeira versão.
- [ ] Execute quatro testes manuais: lista comum, lista vazia, um único incidente e prioridade inválida.

- [ ] Crie funções separadas para calcular o resumo e formatar a saída da lista fixa de incidentes.
- [ ] Acrescente docstrings curtas às funções e confirme que cada uma pode ser chamada diretamente, sem depender de menu interativo.
- [ ] Preencha `atividades/01-funcoes-e-primeiro-mini-projeto/projeto-semanal/docs/apresentacao.md` e apresente o programa em até três minutos.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Compreensoes e funcoes uteis

#### O que pesquisar
- `Compreensoes e funcoes uteis Python explicado passo a passo`
- `Compreensoes e funcoes uteis Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-compreensoes-e-funcoes-uteis`](<atividades/02-compreensoes-e-funcoes-uteis/>)

#### O que você precisa entender

Uma *comprehension* cria uma coleção a partir de outra; `enumerate`, `zip`, `sorted`, `any` e `all` evitam laços auxiliares comuns.

```python
incidentes = [{"cidade": "Salvador", "duracao": 80}, {"cidade": "Feira", "duracao": 20}]
longos = [item for item in incidentes if item["duracao"] > 60]
ranking = sorted(incidentes, key=lambda item: item["duracao"], reverse=True)
tem_critico = any(item["duracao"] > 60 for item in incidentes)
duracoes_validas = all(item["duracao"] >= 0 for item in incidentes)
```

**Erro comum:** compactar filtro, transformação e várias condições em uma única expressão difícil de explicar.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-compreensoes-e-funcoes-uteis/comprehensions.py`.
- **Dados:** cenários e valores já preenchidos no arquivo principal.

#### O que fazer

- [ ] Crie uma lista de 20 incidentes e gere com list comprehension apenas os P1/P2 com duração superior a 60 minutos.
- [ ] Crie um dicionário por comprehension no formato `{cidade: total_de_incidentes}` e compare com a solução usando laço tradicional.
- [ ] Use `enumerate` para numerar um ranking, `zip` para combinar cidades e metas, `sorted` com `key` para ordenar por duração, `any` para detectar P1 e `all` para validar durações não negativas.

- [ ] Escreva três versões da mesma transformação: laço, comprehension legível e comprehension excessivamente compacta; explique qual manteria em produção.
- [ ] Crie cinco testes com lista vazia, cidade repetida, duração zero, valor negativo e prioridade inválida.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
