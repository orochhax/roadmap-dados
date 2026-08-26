# Enunciado — coletor confiável de chamados por API REST

## Cenário

Uma operação de suporte recebe chamados por uma API. O endpoint devolve no máximo alguns registros por página e pode responder lentamente, limitar chamadas ou falhar por alguns instantes. O relatório diário não pode duplicar chamados nem baixar todo o histórico a cada execução.

Você construirá um coletor em `cliente_api.py`. Primeiro, use `api_fake_paginas.json` para controlar todos os cenários sem internet. Depois, faça uma chamada `GET` pequena a uma API pública de testes ou a um endpoint fornecido no momento do estudo, mantendo URL e credenciais fora do código.

Não há solução pronta neste diretório. Complete os `TODOs` depois de estudar cada conceito.

## Regras de segurança

- Nunca cole token, senha, chave ou cookie neste repositório.
- Leia `API_BASE_URL` e `API_TOKEN` de variáveis de ambiente. O modo local simulado não deve exigir token.
- Não imprima o token nos logs, nem mesmo durante erros.
- Use somente dados fictícios e requisições `GET` neste exercício.
- Defina limite de tentativas e tempo máximo de espera; nenhuma falha pode gerar repetição infinita.

## Entregas

O programa deverá produzir dentro de `entrega/`:

1. `chamados_consolidados.csv`, com uma linha por `id`;
2. `cache/`, com respostas JSON brutas e data da coleta;
3. `estado_incremental.json`, com a marca de progresso confirmada somente após uma execução completa;
4. `metricas_execucao.json`, contendo duração, chamadas tentadas, chamadas bem-sucedidas, retries, páginas, itens recebidos, itens novos, duplicados e acertos de cache;
5. um log sem segredos que permita localizar a página e a tentativa que falhou.

## Etapa 1 — contrato e requisição mínima

1. Descreva no arquivo de evidências o significado de recurso, verbo, parâmetro, cabeçalho, status e corpo JSON.
2. Identifique no arquivo fake onde estão a lista de itens e o cursor da página seguinte.
3. Implemente uma requisição com parâmetros `status`, `updated_after` e `cursor` quando aplicáveis.
4. Defina `timeout` explicitamente e valide o código de status antes de acessar os itens.
5. Rejeite JSON inválido ou resposta sem as chaves previstas com mensagem útil.

## Etapa 2 — paginação e consistência

1. Percorra as páginas até o contrato informar que não existe próximo cursor.
2. Não dependa de uma quantidade fixa de páginas.
3. Detecte cursor repetido para impedir loop infinito.
4. Elimine registros repetidos por `id` e registre quantos foram descartados.
5. Ordene o CSV final por `updated_at` e depois por `id`, para tornar duas execuções comparáveis.

## Etapa 3 — timeout, retry, backoff e rate limit

Implemente uma política e justifique-a nas evidências:

- `429`: respeitar `Retry-After` quando válido;
- `500`, `502`, `503` e `504`: realizar novas tentativas com espera crescente;
- `400`, `401`, `403` e `404`: encerrar com diagnóstico, sem retry automático;
- timeout e falha de conexão: tentar novamente apenas até o limite definido;
- espera total e número de tentativas devem ter teto.

Use a sequência `rate_limit_depois_sucesso` do arquivo fake para testar uma recuperação e `servidor_indisponivel` para provar que o programa encerra.

## Etapa 4 — cache e carga incremental

1. Grave o JSON bruto antes de transformá-lo, sem sobrescrever silenciosamente uma coleta anterior.
2. Defina quando o cache pode ser reutilizado e como sua validade será verificada.
3. Na primeira execução, faça uma carga completa.
4. Na segunda, envie a última marca `updated_at` confirmada e processe apenas itens novos ou alterados.
5. Atualize a marca de progresso somente se todas as páginas da execução terminarem corretamente.
6. Simule uma falha na última página e confirme que a marca anterior foi preservada.

## Casos de teste obrigatórios

- duas páginas válidas e fim da paginação;
- página válida sem itens;
- mesmo `id` presente em duas páginas;
- `next_cursor` repetido;
- `429` seguido de sucesso;
- falhas `5xx` acima do limite de tentativas;
- JSON sem `items`;
- primeira carga completa e segunda carga incremental;
- cache válido e cache vencido;
- token fictício não aparece em nenhum arquivo gerado.

## Perguntas para explicar sem consultar o código

1. Por que uma requisição sem `timeout` pode travar um pipeline?
2. Por que repetir automaticamente um erro `401` não resolve o problema?
3. Qual é a diferença entre paginação por número de página e por cursor?
4. O que pode acontecer se a marca incremental for salva antes da última página?
5. Quando o cache economiza custo e quando pode entregar dado antigo?
6. Como sua política limita latência, número de chamadas e risco de sobrecarregar a API?

## Critério de conclusão

O exercício termina quando todos os casos obrigatórios foram executados, os quatro artefatos foram gerados, o token não foi exposto e você consegue explicar as seis perguntas com exemplos do próprio coletor.
