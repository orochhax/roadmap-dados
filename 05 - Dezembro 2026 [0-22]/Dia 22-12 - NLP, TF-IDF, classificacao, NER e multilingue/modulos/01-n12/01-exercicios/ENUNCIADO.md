# Enunciado — Roteador multilíngue do Assistente de Suporte IA

## Cenário real

Uma empresa de telecom recebe tickets por aplicativo, chat e e-mail. Hoje uma pessoa lê cada mensagem e escolhe a fila. O produto precisa sugerir uma das filas `falha_rede`, `faturamento`, `alteracao_plano`, `cancelamento`, `fraude` ou `suporte_aparelho`. Uma previsão insegura deve virar `revisao_humana`, pois um encaminhamento errado aumenta o tempo de solução.

## Entradas

Prepare um arquivo tabular com pelo menos estas colunas:

- `ticket_id`: identificador único;
- `created_at`: data e hora de abertura;
- `customer_id_hash`: identificador anonimizado do cliente;
- `language`: `pt`, `en` ou `es`;
- `channel`: origem do contato;
- `text`: mensagem original;
- `label`: fila correta, preenchida apenas no conjunto rotulado.

Use dados públicos, anonimizados ou produzidos por você. Não coloque nomes, telefones, e-mails, documentos, credenciais ou outros dados pessoais reais no repositório. Registre a origem e a licença. Garanta exemplos dos três idiomas e de todas as classes.

## Saídas obrigatórias

Seu programa `classificador_tickets.py` deve produzir:

1. um resumo da distribuição das classes e idiomas;
2. comparação entre um `DummyClassifier` e um pipeline TF-IDF + classificador linear;
3. métricas do conjunto de teste, nunca usado para ajustar o modelo;
4. uma matriz de confusão e uma tabela de erros;
5. um arquivo de previsões com `ticket_id`, `label_real`, `label_prevista`, `confianca` e `decisao`;
6. tempo de inferência por lote e por ticket;
7. recomendação final: promover, revisar ou rejeitar o classificador.

## Regras de implementação

- Separe treino, validação e teste antes de ajustar o TF-IDF.
- Evite que textos duplicados ou tickets do mesmo cliente apareçam nos dois lados da avaliação.
- O baseline obrigatório é a classe mais frequente.
- Compare n-gramas de palavras com n-gramas de caracteres; escolha usando somente a validação.
- Não remova acentos automaticamente: trate isso como hipótese e meça o efeito.
- Defina um limiar de confiança para `revisao_humana` usando a validação.
- Fixe as seeds e mantenha o fluxo reproduzível.
- Nenhum rótulo pode ser inferido por uma coluna que só existiria depois da resolução do ticket.

## Casos de borda que precisam ser testados

- texto vazio ou contendo apenas espaços;
- mensagem muito curta, como `sem sinal`;
- erros de digitação e abreviações;
- mistura de idiomas na mesma mensagem;
- classe rara e frase ambígua entre duas filas;
- ticket praticamente duplicado de outro registro.

O programa deve tratar entradas inválidas com uma mensagem clara, sem falhar silenciosamente.

## Métricas

- principal: `macro-F1`;
- apoio: recall por classe, matriz de confusão, cobertura automática após abstenção e latência P50/P95;
- análise por fatia: idioma, canal e comprimento do texto.

## Critério de aceite

O modelo só pode ser recomendado se superar o macro-F1 do baseline em pelo menos 0,10, não deixar nenhuma classe crítica (`fraude` e `cancelamento`) com recall abaixo de 0,60 e respeitar o limite de latência definido antes do teste. Se não atingir os limites, o exercício continua válido somente se você **rejeitar a promoção**, demonstrar os resultados e explicar pelo menos cinco erros reais sem alterar o teste.

## Restrições de aprendizagem

Implemente no arquivo inicial sem copiar uma solução completa. Pesquise conceitos e APIs separadamente. Não use LLM para rotular o conjunto de teste nem para escrever as respostas do exercício.
