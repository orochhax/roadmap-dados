# Arquivos CSV, JSON e caminhos + Exceções, validação e consumo de APIs REST

**Data de estudo:** 02/09/2026  
**Carga planejada:** 6 a 8 horas

## Atividades do dia

### Atividade 1 — Arquivos CSV, JSON e caminhos

#### O que pesquisar
- `Arquivos CSV, JSON e caminhos Python explicado passo a passo`
- `Arquivos CSV, JSON e caminhos Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-arquivos-csv-json-e-caminhos`](<atividades/01-arquivos-csv-json-e-caminhos/>)

#### O que você precisa entender

CSV representa linhas e colunas; JSON representa listas e objetos. `pathlib.Path` cria caminhos independentes da pasta usada para iniciar o programa.

```python
from pathlib import Path
import csv

base = Path(__file__).resolve().parent
with (base / "incidentes.csv").open(encoding="utf-8", newline="") as arquivo:
    incidentes = list(csv.DictReader(arquivo))
```

**Erro comum:** usar um caminho relativo ao terminal e fazer o programa funcionar apenas quando executado de uma pasta específica.

#### Aulas complementares — terminal

- [ ] Curso Linux #07.1 — **Terminal no Linux: Introdução** (32:22).
- [ ] Curso Linux #07.2 — **Terminal no Linux: Manipulando diretórios** (30:20).
- **Prática no sistema atual:** no PowerShell, use `Get-Location`, `Get-ChildItem`, `Set-Location` e `Set-Location ..`; se já usa WSL ou Git Bash, repita com `pwd`, `ls` e `cd ..`.
- Não é necessário instalar outro sistema operacional.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-arquivos-csv-json-e-caminhos/dia-007-arquivos-csv-json-e-caminhos.py`.
- **Dados:** `atividades/01-arquivos-csv-json-e-caminhos/incidentes.csv` e `atividades/01-arquivos-csv-json-e-caminhos/metas.json`.

#### O que fazer

- [ ] Use os arquivos preparados com quatro linhas válidas para praticar leitura de CSV com `csv` e leitura de JSON com `json`, sem pandas.
- [ ] Converta somente os campos numéricos e booleanos necessários e associe cada incidente à meta de sua cidade.
- [ ] Grave `relatorio_consolidado.csv` com a coluna `dentro_da_meta` e confira manualmente duas linhas.

- [ ] Acrescente ao CSV a linha `INC-013,Ilhéus,queda de energia,P2,85,140,true`, adicione ao JSON a meta de 90 minutos para Ilhéus e gere novamente o consolidado.
- [ ] Execute o programa a partir da raiz do repositório e da própria pasta; use `pathlib` e confirme que ambas as execuções encontram os mesmos arquivos e produzem o mesmo resultado.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Excecoes e validacao

#### O que pesquisar
- `Excecoes e validacao Python explicado passo a passo`
- `Excecoes e validacao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-excecoes-e-validacao`](<atividades/02-excecoes-e-validacao/>)

#### O que você precisa entender

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

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-excecoes-e-validacao/dia-008-excecoes-e-validacao.py`.
- **Dados:** cenários e valores já preenchidos no arquivo principal.

#### O que fazer

- [ ] Use uma cópia pequena do CSV com quatro erros diferentes e implemente `validar_linha()` para retornar os problemas encontrados.
- [ ] Aplique `try/except` somente nas conversões que podem falhar, sem envolver o programa inteiro.
- [ ] Separe linhas válidas e rejeitadas sem interromper o processamento no primeiro erro.
- [ ] No mesmo arquivo, implemente `calcular_taxa(resolvidos, total)` e trate `total == 0`, texto no lugar de número e valores negativos; teste com `(82, 100)`, `(0, 0)` e `("x", 10)`.

- [ ] Grave os dois CSVs de saída apenas depois de validar corretamente a lista em memória.
- [ ] Repita um mesmo id em duas linhas válidas e envie a segunda ocorrência para `dados_rejeitados.csv`.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 3 — Consumo seguro e confiável de APIs REST com Python

#### O que pesquisar
- `Python requests API REST GET parâmetros headers JSON`
- `API REST autenticação token variável de ambiente segurança`
- `requests timeout retry exponential backoff Retry-After`
- `API pagination page cursor next link`
- `HTTP status 200 400 401 404 429 500`
- `ETag Last-Modified cache HTTP`
- `API carga incremental updated_at watermark`

**Arquivos da atividade:** [abrir a pasta `03-consumo-seguro-e-confiavel-de-apis-rest`](<atividades/03-consumo-seguro-e-confiavel-de-apis-rest/>)

#### Objetivo

Construir um coletor de chamados que funcione tanto com uma API real quanto com dados locais simulados. O coletor precisa atravessar páginas, sobreviver a falhas temporárias sem repetir chamadas indefinidamente, evitar segredos no Git e baixar apenas registros novos ou alterados nas execuções seguintes.

#### O que fazer

- [ ] Entenda o contrato de uma API: URL base, recurso, verbo HTTP, parâmetros, cabeçalhos, corpo, código de status e JSON de resposta.
- [ ] Faça uma requisição pequena com `requests`, parâmetros explícitos e `timeout`; valide o status antes de interpretar o JSON.
- [ ] Separe autenticação da lógica do coletor e leia o token de variável de ambiente; nunca grave um token real no código, no README, em evidências ou em commits.
- [ ] Implemente paginação por cursor ou próximo link, encerrando somente quando o contrato indicar que não há outra página.
- [ ] Trate `429` e falhas `5xx` com tentativas limitadas, espera crescente e respeito ao cabeçalho `Retry-After`; erros permanentes não devem entrar em repetição automática.
- [ ] Crie cache dos JSONs brutos e uma marca de progresso para carga incremental, explicando quando o cache pode ficar desatualizado.
- [ ] Execute o mesmo fluxo no modo local simulado para provar a lógica sem internet, credenciais ou custo.

Leia o [enunciado](<atividades/03-consumo-seguro-e-confiavel-de-apis-rest/ENUNCIADO.md>), complete somente os `TODOs` de [cliente_api.py](<atividades/03-consumo-seguro-e-confiavel-de-apis-rest/cliente_api.py>) e use [api_fake_paginas.json](<atividades/03-consumo-seguro-e-confiavel-de-apis-rest/api_fake_paginas.json>) como fonte local. Registre comandos, resultados e decisões no próprio artefato.

#### Como validar

- Consumi e validei JSON, parâmetros, cabeçalhos e códigos HTTP sem misturar essas responsabilidades.
- Implementei autenticação segura por variável de ambiente e confirmei que nenhum segredo entrou no repositório.
- Testei paginação, página vazia, registro repetido, `429`, erro `5xx` e encerramento das tentativas.
- Comparei uma carga completa com uma incremental e medi chamadas, registros novos, tempo e uso do cache.
- Expliquei uma limitação concreta do retry, do cache ou da estratégia incremental.

## Integração do dia

Explique com suas palavras como CSV, JSON, validação e API se conectam em um fluxo de ingestão. Execute um caso comum e um caso de borda de cada atividade e registre comandos, saídas e dúvidas no próprio artefato.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
