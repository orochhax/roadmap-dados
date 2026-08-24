# TCC — roteiro de dados e protocolo sem respostas

> Preencha cada seção com decisões, comandos e resultados próprios. Não apague os enunciados.

## 1. Manifesto dos dados

| Dataset | Caminho | Versão/seed | Período | Linhas | Hash | Declaração sintética visível? |
|---|---|---|---|---:|---|---|
| snapshots de churn |  |  |  |  |  |  |
| piloto de retenção |  |  |  |  |  |  |

## 2. Schema do snapshot preditivo

Liste identificador anonimizado, data de decisão, features, alvo e disponibilidade.

| Campo | Tipo | Momento disponível | Regra de validade | Feature/alvo/metadado | Risco de leakage |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 3. Schema do piloto randomizado simulado

| Campo | Tipo | Papel | Regra de validade | Pós-tratamento? |
|---|---|---|---|---|
|  |  |  |  |  |

- população elegível:
- unidade de randomização:
- probabilidade de atribuição:
- tratamento:
- desfecho e horizonte:
- estimando primário:
- análise por intenção de tratar:

## 4. Geração sintética

- seed:
- regras do gerador:
- dependências entre features permitidas:
- como churn foi gerado sem virar uma feature direta:
- como o tratamento e o desfecho foram simulados:
- quais parâmetros não representam uma operadora real:
- comando de reprodução:

## 5. Divisão temporal

| Divisão | Datas | Quantidade | Positivos | Uso permitido |
|---|---|---:|---:|---|
| treino |  |  |  |  |
| validação |  |  |  |  |
| teste |  |  |  |  |

Explique por que a separação é temporal e como clientes repetidos são tratados:

<!-- Preencha aqui. -->

## 6. Auditoria de qualidade e leakage

| Teste | Entrada/caso | Resultado esperado | Resultado observado | Passou? |
|---|---|---|---|---|
| schema |  |  |  |  |
| chave duplicada |  |  |  |  |
| faixa impossível |  |  |  |  |
| data futura |  |  |  |  |
| feature pós-decisão |  |  |  |  |
| campo pós-tratamento |  |  |  |  |

## 7. Verificação da randomização simulada

- contagem por grupo:
- taxa de tratamento atribuído/recebido:
- método de checagem de equilíbrio:
- maior desequilíbrio observado:
- decisão de manter o protocolo sem rerandomizar por conveniência:

## 8. Limites de inferência

- o que a análise preditiva poderá afirmar:
- o que o piloto simulado poderá demonstrar metodologicamente:
- o que nenhuma parte poderá afirmar sobre impacto real:
- slices pequenos que não permitem conclusão confiável:

## Aceite

- Os dois arquivos estão marcados como sintéticos.
- Nenhuma feature usa informação futura ou pós-tratamento.
- Splits, elegibilidade e randomização estão congelados.
- Testes possuem esperado, observado e decisão.
