# TCC: universo, dados e protocolo financeiro

## Preparação
- **Enunciado local:** `01-exercicios/roteiro_tcc.md`.
- **Saídas canônicas:** `projetos/portfolio-intelligence-lab/docs/protocolo-financeiro.md`, `projetos/portfolio-intelligence-lab/src/data/pipeline.py` e `projetos/portfolio-intelligence-lab/data/raw/`.
- **Unidade de análise:** ativo × data de rebalanceamento.
- **Universo obrigatório:** uma única classe com 10–20 ativos.

## Manifesto de entradas

- **Obrigatórias:** protocolo, preços ajustados e manifesto com fonte, licença, período e hash na pasta canônica.
- **Fallback local:** use CSV/Parquet versionado; coleta online não é requisito.

## Aprenda agora

- **Definição:** disponibilidade temporal registra quando cada campo podia ser usado; survivorship bias surge ao considerar apenas ativos sobreviventes.
- **Exemplo mínimo:** tabela `campo, data_evento, data_disponivel, fonte`; audite duas datas e use preços ajustados em `projetos/portfolio-intelligence-lab/data/raw/precos_ajustados.parquet`.
- **Erro comum:** usar composição atual do universo em todo o histórico ou baixar dados sem congelar versão.

## Núcleo essencial

1. [ ] Importe preços ajustados para o universo mínimo e preserve a camada bruta.
2. [ ] Crie tabela de ativos, dicionário de dados e relatório de ausentes, duplicados e histórico insuficiente; registre `disponivel_em` quando a publicação não coincidir com a data de referência.
3. [ ] Defina elegibilidade e remova somente ativos que violem uma regra escrita antes da análise.
4. [ ] Congele protocolo walk-forward, custos, baseline e métricas antes de calcular fatores.

## Prática obrigatória

- [ ] Teste o impacto de exigir 252 pregões e registre quantos ativos permanecem.
- [ ] Audite manualmente duas datas para comprovar que nenhuma informação futura entrou no protocolo.

## Concluído quando

- [ ] O pipeline, o protocolo e o snapshot canônicos contêm todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.
