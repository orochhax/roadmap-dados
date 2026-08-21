# Pipeline em Python

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/transform.py`.
- **Entradas:** `dados/pedidos.csv`, schema e `01-exercicios/config.yaml`. **Fallback local:** Parquet ou DuckDB.

## Aprenda agora

- **Definição:** idempotência significa que a mesma entrada produz o mesmo estado; configuração separa parâmetros; log registra evento, tempo e contexto.
- **Exemplo mínimo:** leia CSV, valide schema, grave Parquet/DuckDB e execute duas vezes; contagem e chaves não podem duplicar.
- **Erro comum:** usar append sem chave de execução ou esconder caminhos dentro do código.

## Núcleo essencial

1. [ ] Implemente `extract.py` para ler CSV/JSON, `transform.py` para limpar e criar features, e `load.py` para gravar Parquet ou DuckDB.
2. [ ] Use arquivo de configuração para caminhos, sem valores fixos no código.
3. [ ] Adicione logs com quantidade lida, rejeitada e gravada.

## Prática obrigatória

- [ ] Teste arquivo ausente, coluna faltante e linha inválida; registre a falha esperada e a observada.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/transform.py`:** Adicione validação obrigatória das colunas cliente_id e data_ativacao antes da transformação.
- [ ] **Em `01-exercicios/transform.py`:** Execute duas vezes com o mesmo arquivo e depois com uma linha nova; compare contagens para provar idempotência e incremento.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/transform.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.
