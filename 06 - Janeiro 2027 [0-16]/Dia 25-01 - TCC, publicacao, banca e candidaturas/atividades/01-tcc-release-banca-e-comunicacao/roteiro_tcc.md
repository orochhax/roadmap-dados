# TCC — roteiro de release, banca e candidaturas

> Preencha com resultados próprios. Não invente respostas de banca, impacto real ou domínio profissional.

## 1. Auditoria da release

- tag/versão candidata:
- commit:
- ambiente limpo utilizado:
- comando de instalação:
- comando único de reprodução:
- versão/hash dos dados sintéticos:
- runs MLflow reconciliados:

| Artefato | Esperado | Obtido | Caminho/link | Passou? |
|---|---|---|---|---|
| dados processados |  |  |  |  |
| benchmark preditivo |  |  |  |  |
| análise do piloto |  |  |  |  |
| testes |  |  |  |  |
| monitoramento |  |  |  |  |
| retreino/rollback simulados |  |  |  |  |
| relatório |  |  |  |  |

## 2. Reconciliação final

| Número/afirmação | Output de origem | README PT | README EN | Relatório | Apresentação | Consistente? |
|---|---|---|---|---|---|---|
| PR-AUC |  |  |  |  |  |  |
| recall@K |  |  |  |  |  |  |
| calibração |  |  |  |  |  |  |
| efeito/IC |  |  |  |  |  |  |
| ganho por 100 |  |  |  |  |  |  |
| custo por retenção |  |  |  |  |  |  |

## 3. Segurança e honestidade

- confirmação de ausência de dados pessoais:
- confirmação de ausência de credenciais/segredos:
- declaração visível de dados sintéticos:
- declaração visível de piloto randomizado simulado:
- resultado negativo ou inconclusivo mantido:
- afirmação exagerada removida:
- itens fora do escopo que continuam fora:

## 4. Defesa de 8–10 minutos

- duração:
- link/caminho da gravação:
- artefato usado para cada afirmação:
- duas respostas mais fracas:
  1.
  2.
- correção de cada resposta com evidência:
  1.
  2.

## 5. README e apresentação em inglês

- caminho do `README.en.md`:
- contagem de palavras entre 150 e 250:
- caminho de `docs/presentation-en.md`:
- duração entre 2 e 3 minutos:
- perguntas respondidas sem roteiro decorado:
- termos que ainda precisam de prática:

## 6. Banco de perguntas para a banca

Para cada pergunta, escreva resposta curta, evidência e limitação.

1. Qual decisão, data de corte, horizonte e capacidade foram congelados?
2. Por que risco de churn não equivale a resposta à campanha?
3. Como provou ausência de leakage temporal e pós-tratamento?
4. Qual baseline foi mais difícil de superar?
5. Por que PR-AUC e recall@K são adequados?
6. Como avaliou a calibração?
7. Como gerou os dados sintéticos e quais vieses introduziu?
8. Por que a análise principal do piloto é por intenção de tratar?
9. O que conclui se o intervalo de confiança cruza zero?
10. Como tratou custo por retenção quando o efeito foi zero/negativo?
11. Quais slices não têm amostra suficiente?
12. Como escolheu champion/challenger no MLflow?
13. Como simulou retreino e rollback?
14. Qual limitação mais enfraquece a generalização?

### Respostas e evidências

| Pergunta | Resposta própria | Evidência real | Limitação reconhecida |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |
| 7 |  |  |  |
| 8 |  |  |  |
| 9 |  |  |  |
| 10 |  |  |  |
| 11 |  |  |  |
| 12 |  |  |  |
| 13 |  |  |  |
| 14 |  |  |  |

## 7. Publicação e candidaturas

- URL da release:
- URL do relatório:
- URL da demonstração:
- teste em janela anônima:
- texto revisado contra alegações falsas:

| Vaga | Requisitos realmente atendidos | Evidência citada | Lacuna declarada | Data |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

## Aceite

- Release reproduzida em ambiente limpo.
- Todos os números estão reconciliados.
- Defesa e inglês usam evidências próprias.
- Publicação e candidaturas declaram caráter educacional/sintético.
