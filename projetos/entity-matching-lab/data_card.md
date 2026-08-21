# Data card — Entity Matching Lab

## Escopo

- unidade canônica: empresa;
- unidade recebida: registro potencialmente ruidoso;
- label: id canônico verdadeiro ou sem correspondência;
- países/idiomas: TODO definir e justificar;
- seed do gerador: TODO;
- licença de qualquer fonte externa: TODO registrar antes de usar.

## Schemas mínimos

### empresas_canonicas.csv

| Campo | Descrição |
|---|---|
| entity_id | identificador estável |
| legal_name | nome canônico |
| domain | domínio normalizado |
| country | país |

### registros_ruidosos.csv

| Campo | Descrição |
|---|---|
| record_id | identificador do registro |
| observed_name | nome recebido |
| observed_domain | domínio recebido ou ausente |
| country | país informado ou ausente |
| true_entity_id | rótulo reservado à avaliação |
| corruption_type | slice de erro, sem entrar no modelo |

## Perturbações obrigatórias

- acentos e caixa;
- sufixos societários;
- abreviações;
- troca, remoção ou inserção de caracteres;
- aliases;
- subdomínios e protocolos;
- nomes parecidos de entidades diferentes;
- sem correspondência;
- pelo menos um slice multilíngue.

## Split e vazamento

Separe por entity_id. Variantes da mesma entidade não podem aparecer em treino
e teste. corruption_type é metadado de avaliação e não pode virar feature.

## Riscos

- viés geográfico ou linguístico;
- falso positivo entre lookalikes;
- domínio compartilhado ou ausente;
- dados sintéticos mais fáceis que cadastros reais;
- custo e privacidade ao chamar serviços externos.
