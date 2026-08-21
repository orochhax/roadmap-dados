# Evidências — N12: classificação de tickets

Preencha este arquivo durante o exercício. Não apague resultados ruins: eles também são evidência de aprendizado.

## Dados e segurança

- origem/licença ou processo de criação:
- período coberto:
- quantidade por classe, idioma e canal:
- verificação de dados pessoais e duplicatas:

## Ambiente reproduzível

- versão do Python:
- versões de `pandas` e `scikit-learn`:
- seed:
- comando exato de execução:

## Desenho da avaliação

- regra de separação entre treino, validação e teste:
- risco de vazamento identificado e prevenção aplicada:
- macro-F1 e limite de latência definidos antes do teste:
- limiar de abstenção escolhido somente na validação:

## Comparação

| abordagem | macro-F1 | recall fraude | recall cancelamento | cobertura | latência P95 |
|---|---:|---:|---:|---:|---:|
| classe mais frequente |  |  |  |  |  |
| TF-IDF de palavras |  |  |  |  |  |
| TF-IDF de caracteres |  |  |  |  |  |

## Análise de erros

Registre ao menos cinco exemplos anonimizados: texto resumido, classe real, previsão, confiança, categoria do erro e provável causa. Inclua resultados separados por idioma.

## Decisão operacional

- decisão: promover, revisar ou rejeitar?
- qual fila sofre o maior risco?
- qual limitação impede uso mais amplo?
- próximo experimento com hipótese mensurável:
