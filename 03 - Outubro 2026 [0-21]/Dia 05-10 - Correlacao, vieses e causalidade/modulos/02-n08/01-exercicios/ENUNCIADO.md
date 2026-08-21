# Enunciado — contato proativo reduz churn?

## Cenário real

A equipe de retenção liga para clientes considerados em risco. A taxa de churn dos contatados é maior, e um gerente concluiu que as ligações “causam cancelamento”. Porém, clientes são escolhidos justamente porque já têm sinais de insatisfação. Antes de modelar, você deverá formalizar a pergunta e a identificação.

## Entradas

- dicionário de `dados/clientes_telecom.csv`;
- tratamento hipotético `contato_proativo` ocorrido no dia de corte;
- resultado `churn_30d` observado nos 30 dias seguintes;
- variáveis prévias: cidade, plano, mensalidade, tempo de cliente, NPS anterior, atrasos anteriores e chamados anteriores;
- pós-tratamento: `oferta_aceita` e `revisao_humana`;
- variável não observada proposta por você, como intenção de cancelar.

## Saídas

- [protocolo_dag.md](protocolo_dag.md) preenchido;
- DAG em Mermaid com pelo menos dez nós e setas justificadas;
- tabela temporal das variáveis;
- três conjuntos candidatos de ajuste, cada um aceito ou rejeitado;
- plano de identificação e teste de falsificação no [registro de evidências](../03-evidencias/README.md).

## Regras obrigatórias

1. Defina população elegível, versão do tratamento, comparador, horizonte e estimando principal (`ATE` ou `ATT`).
2. Desenhe setas com base no processo gerador, não em correlações calculadas.
3. Identifique ao menos um confundidor, um mediador e um collider.
4. Use o critério backdoor para escolher um conjunto mínimo de ajuste.
5. Não ajuste a análise principal por `oferta_aceita`, pois ocorre após o contato.
6. Avalie o risco de condicionar em `revisao_humana` se ela for causada pelo contato e pela gravidade do caso.
7. Declare as suposições de consistência, intercambiabilidade e positividade em linguagem simples.
8. Proponha um controle negativo ou resultado que o contato não deveria afetar.

## Casos de borda obrigatórios

- NPS medido depois do contato;
- variável chamada “perfil” sem definição temporal;
- plano sem clientes contatados;
- contato com intensidades diferentes tratado como binário;
- mediador incluído como confundidor;
- seleção somente de clientes que aceitaram a oferta;
- causa não observada da escolha e do churn;
- duas versões do DAG igualmente plausíveis.

## Métricas de qualidade do protocolo

- caminhos backdoor identificados, bloqueados e ainda abertos;
- percentual de variáveis com momento de disponibilidade definido;
- cobertura da população com ambos os tratamentos por estrato;
- quantidade de suposições testáveis e não testáveis;
- resultado do controle negativo planejado.

## Critério de aceite

- [ ] O estimando pode ser escrito em uma frase sem usar “correlação”.
- [ ] Cada variável do DAG tem fonte e momento definidos.
- [ ] O conjunto final bloqueia os caminhos listados sem incluir mediador/collider.
- [ ] Uma falta de positividade e uma causa não observada são discutidas.
- [ ] O protocolo conclui honestamente se o efeito é identificável com os dados disponíveis.

