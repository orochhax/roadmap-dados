# Enunciado — diagnosticar a queda no onboarding

## Cenário real

Após uma nova tela de vínculo do modem, cadastros cresceram, mas contatos ao suporte não caíram. Produto quer saber onde o onboarding falha, se usuários ativados retornam e qual segmento deveria receber a próxima melhoria.

## Entradas

- `eventos_validos.jsonl` produzido no módulo de tracking plan;
- se necessário para completar o período, amplie a fixture para ao menos 40 usuários, quatro semanas de cadastro e eventos até D30;
- inclua eventos financeiros `payment_confirmed` e `refund_issued` apenas na tabela analítica deste módulo, com `amount` e `currency`.

## Saídas

- consultas em [product_analytics.sql](product_analytics.sql);
- tabelas `funnel_onboarding`, `cohort_retention` e `ltv_cohort` exportadas para CSV;
- recomendação de produto no próprio artefato.

## Regras obrigatórias

1. Defina usuário como `user_id` resolvido; eventos apenas anônimos não entram em métricas de usuário até existir ligação auditável.
2. Funil ordenado: `account_created` → `modem_linked` → `diagnostic_started` → `issue_resolved`.
3. Conte cada usuário uma vez por etapa e exija que a etapa ocorra depois da anterior.
4. Ativação: primeiro `issue_resolved` em até sete dias após cadastro; calcule também tempo mediano até valor.
5. Coorte: semana do primeiro `account_created`; retenção D1, D7 e D30 exige `app_opened` na janela declarada.
6. LTV histórico: receita confirmada menos estornos, acumulada por idade da coorte; não extrapole valor futuro.
7. Compare canal de aquisição e plano apenas quando cada grupo tiver pelo menos dez usuários; mostre tamanho sempre.
8. Declare timezone e limite de cada janela antes de consultar.

## Casos de borda obrigatórios

- etapa repetida;
- etapa final antes da inicial;
- usuário anônimo nunca identificado;
- cadastro no limite da janela de dados;
- coorte sem nenhum retorno;
- pagamento totalmente estornado;
- usuário com dois cadastros;
- denominador igual a zero.

## Métricas

- conversão e abandono por etapa;
- ativação em sete dias e tempo mediano até valor;
- retenção D1/D7/D30 por coorte;
- receita líquida e LTV histórico por idade/coorte;
- reconciliação entre usuários únicos da base e denominadores usados.

## Critério de aceite

- As três tabelas são reproduzíveis a partir da entrada bruta.
- Um cálculo manual com cinco usuários confere exatamente com o SQL.
- Repetições e ordem inválida não inflam o funil.
- Coortes incompletas são sinalizadas, não comparadas como maduras.
- A recomendação escolhe uma etapa/segmento e cita conversão, tamanho e limitação.

