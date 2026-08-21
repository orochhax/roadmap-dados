# Data card — TCC de retenção em telecom

Preencha este documento antes de treinar o benchmark final. Ele complementa o
[data card do projeto pai](../data_card.md); não o substitui.

## Declaração obrigatória de origem

- dados de clientes: **sintéticos**;
- atribuição da campanha do TCC: **sintética**;
- resposta e desfecho causal do TCC: **sintéticos**;
- pessoas reais ou dados pessoais: **não contém**;
- versão do gerador: TODO;
- seed: TODO;
- data da geração: TODO;
- responsável pela geração: TODO.

Todo arquivo novo usado na avaliação causal deve conter uma coluna ou metadado
equivalente a `origem_sintetica = true`. O README, o relatório e as figuras
também devem repetir essa limitação.

## Fontes herdadas e imutáveis

| Fonte | Papel possível | Regra |
|---|---|---|
| `../../../dados/clientes_telecom.csv` | alvo histórico e atributos | não editar; excluir campos posteriores à decisão |
| `../../../dados/clientes.csv` | dimensão de clientes | não editar |
| `../../../dados/planos.csv` | dimensão de planos | não editar |
| `../../../dados/chamados.csv` | eventos de suporte | agregar somente eventos já ocorridos |
| `../../../dados/pagamentos.csv` | eventos financeiros | agregar somente eventos já ocorridos |
| `../../../dados/incidentes.csv` | contexto operacional | agregar somente eventos já ocorridos |

Confirme as contagens, chaves e hashes; não copie valores esperados como se
fossem resultados verificados.

## Unidade, decisão e desfecho

- unidade de análise: cliente em uma data de decisão;
- data ou frequência de decisão: TODO;
- população elegível: TODO;
- horizonte de churn/retenção: TODO;
- tratamento: TODO definir uma única ação de retenção;
- atribuição do tratamento: TODO descrever a randomização sintética;
- desfecho primário: TODO;
- capacidade operacional: TODO;
- custo por contato: TODO;
- valor atribuído à retenção: TODO.

## Tabelas derivadas esperadas

### `base_decisao.parquet`

Uma linha por cliente e data de decisão. Documente cada feature:

| Campo | Fonte | Disponível na decisão? | Janela | Tratamento | Risco de vazamento |
|---|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO | TODO |

Campos como `data_cancelamento`, `motivo_cancelamento`, status posterior e
eventos posteriores à data de decisão não podem ser usados como features.

### `piloto_retencao_sintetico.parquet`

Contrato mínimo a validar:

| Campo | Significado |
|---|---|
| `cliente_id` | chave para a unidade elegível |
| `data_decisao` | instante anterior a qualquer informação do horizonte |
| `tratamento_atribuido` | grupo definido pela randomização sintética |
| `tratamento_recebido` | execução simulada da ação, se diferente da atribuição |
| `desfecho_horizonte` | retenção ou churn observado no horizonte simulado |
| `estrato_randomizacao` | estrato usado antes da atribuição, quando aplicável |
| `custo_acao` | custo declarado da ação |
| `origem_sintetica` | deve ser verdadeiro para todas as linhas |
| `versao_gerador` | versão reproduzível do mecanismo de geração |
| `seed_gerador` | seed usada para reproduzir o piloto |

Não exponha resultados potenciais não observáveis como features ou como dados
que uma política real teria no instante de decisão.

### `splits.json`

Registre datas e hashes para:

- treino: TODO;
- validação: TODO;
- teste final: TODO;
- monitoramento intocado: TODO.

O mesmo cliente pode aparecer em mais de uma janela somente se o protocolo
explicar a dependência e impedir vazamento entre horizontes.

## Qualidade e validação

- unicidade da unidade cliente-data;
- integridade de chaves e datas;
- ausência de informação futura;
- proporção de tratamento por estrato;
- determinismo com a mesma seed;
- variação controlada ao trocar a seed;
- capacidade de distinguir tratamento atribuído de recebido;
- marcação sintética em 100% dos registros gerados;
- distribuição do desfecho e tamanho de cada segmento.

## Premissas causais

Preencha antes de estimar efeitos:

- consistência entre tratamento definido e executado: TODO;
- ausência de interferência entre clientes: TODO avaliar;
- positividade: TODO avaliar;
- mecanismo de atribuição conhecido: TODO documentar;
- perdas, não adesão ou dados ausentes: TODO;
- estimando ITT, ATE, CATE ou outro estimando: TODO justificar.

## Ética e limitações

- uma política de retenção pode excluir sistematicamente segmentos;
- score de risco não deve justificar pior atendimento;
- contato excessivo pode causar fadiga ou dano;
- dados sintéticos não garantem validade externa;
- o mecanismo gerador pode favorecer sem intenção um dos métodos;
- análises por segmento devem informar tamanho e incerteza.

## Manifesto dos derivados

| Artefato | Comando | Parâmetros/seed | Hash | Criado em |
|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO |

