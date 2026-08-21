# Enunciado — estrela do Telecom Customer Intelligence

## Cenário real

Operações calcula incidentes por cidade, Finanças calcula receita por plano e Retenção cruza ambos. Hoje cada equipe faz joins diretamente nos CSVs e obtém totais diferentes. Sua missão é criar uma camada dimensional única em DuckDB.

## Entradas

- `dados/clientes.csv`;
- `dados/planos.csv`;
- `dados/incidentes.csv`;
- `dados/pagamentos.csv`;
- três alterações históricas de plano que você adicionará como fixture: um upgrade, um downgrade e uma correção recebida com atraso.

## Saídas

- DDL e carga em [modelo_estrela.sql](modelo_estrela.sql);
- diagrama Mermaid ou texto com relações e grão;
- quatro consultas de negócio e tabela de reconciliação no [registro de evidências](../03-evidencias/README.md).

## Regras obrigatórias

1. Declare o grão antes de criar cada tabela.
2. Crie ao menos `dim_data`, `dim_cidade`, `dim_plano`, `dim_cliente` e fatos para incidentes e pagamentos.
3. Use chave substituta nas dimensões e preserve as chaves naturais para rastreio.
4. Modele a troca de plano do cliente como SCD tipo 2, com início, fim e indicador atual.
5. Um intervalo SCD não pode se sobrepor a outro para o mesmo cliente.
6. Associe cada fato à versão da dimensão válida na data do evento.
7. Defina membro “desconhecido” para uma chave ainda não cadastrada; não descarte silenciosamente o fato.
8. Responda: receita por plano/mês; incidentes por mil clientes/cidade; inadimplência por tempo de relacionamento; clientes afetados por severidade.

## Casos de borda obrigatórios

- cliente troca de plano exatamente na data de um pagamento;
- alteração chega atrasada, mas tem vigência anterior;
- plano do fato ainda não existe na dimensão;
- cliente sem pagamento;
- cidade sem incidente;
- join que multiplica pagamentos por incidentes.

## Métricas e conferências

- contagem e soma monetária antes/depois da carga;
- percentual de fatos no membro desconhecido;
- quantidade de intervalos SCD sobrepostos;
- quantidade de linhas antes/depois de cada join;
- comparação manual de dois clientes em duas datas.

## Critério de aceite

- [ ] Todas as tabelas têm grão, chave e regra de atualização documentados.
- [ ] Contagem e soma dos fatos reconciliam com as fontes, exceto rejeições explicitadas.
- [ ] Não existe sobreposição SCD.
- [ ] As quatro perguntas produzem resultados sem dupla contagem.
- [ ] Os seis casos de borda têm resultado esperado e observado.

