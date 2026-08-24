# Entrega de experimento

**Data de estudo:** 08/10/2026  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Entrega de experimento

#### O que pesquisar
- `Entrega de experimento estatística para data science explicado passo a passo`
- `Entrega de experimento estatística para data science exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-entrega-de-experimento`](<atividades/01-entrega-de-experimento/>)

#### Conquista para o LinkedIn

- **Competências:** depois de executar o experimento e defender sua conclusão, adicione **Análise estatística** e **Teste A/B**.
- **Projetos ou Destaques:** inclua a entrega somente se o relatório estiver reproduzível, revisado e acessível por link.
- **Sobre:** você pode mencionar sua primeira análise de experimento com incerteza e limitações. Não altere a headline somente por esta sessão.
- Siga o [Guia de LinkedIn e evidências](<../../00 - Recursos Compartilhados/linkedin-e-evidencias.md>).

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-entrega-de-experimento/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.
- **Entradas concretas:** uma tabela A/B com grupo e resultado, a definição da métrica primária e uma consulta SQL de validação.
- **Fallback local:** gere 500 observações por grupo com seed 42 e probabilidades de sucesso 0,10 e 0,12; grave grupo e resultado em um DataFrame e use-o em toda a entrega.

#### O que fazer

- [ ] Integre as três entradas listadas em Preparação; use a base sintética local se alguma entrada estiver ausente.
- [ ] Registre métrica primária, efeito mínimo e regra de decisão antes de olhar o resultado final.
- [ ] Valide equilíbrio dos grupos e estime efeito com intervalo.
- [ ] Entregue README e relatório de decisão de até duas páginas com resultado, risco e próxima ação.
- [ ] Escreva `atividades/01-entrega-de-experimento/projeto-mensal/README.en.md` em inglês, com 150–250 palavras, cobrindo problema, dados, método, resultados, limitações e reprodução.
- [ ] Prepare `atividades/01-entrega-de-experimento/projeto-mensal/docs/presentation-en.md` como roteiro em inglês para uma apresentação falada de 2–3 minutos.

- [ ] **Em `atividades/01-entrega-de-experimento/roteiro_atividades.md`:** Refaça a regra de decisão usando efeito mínimo relevante de 1,0 ponto percentual e compare com a regra de 1,5 ponto.
- [ ] **Em `atividades/01-entrega-de-experimento/roteiro_atividades.md`:** Remova a cidade com mais observações, registre efeito e intervalo e identifique se a decisão depende desse segmento.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Entrega real de portfólio

**Telecom Customer Intelligence — impacto causal**

Siga o [brief do projeto](<../../projetos/telecom-customer-intelligence/README.md>). A entrega precisa ter problema e usuário definidos, data card, dados reproduzíveis, baseline, métricas escolhidas antes do resultado, análise de erros, testes, README em português e inglês e apresentação de 2–3 minutos em inglês. Documente também resultados negativos.

## Publicação da semana no LinkedIn

- **Tema específico:** avaliar se um contato proativo reduz churn usando hipótese pré-definida, DAG, balanceamento, diferenças em diferenças, controle sintético e placebos.
- **Tipo:** entrega.
- **Formato:** carrossel técnico com DAG, estimativa principal, diagnóstico de premissas, placebo e decisão.
- **Artefato/evidência exigida:** protocolo causal congelado, resultados das atividades de contrafactual, propensity score, diferenças em diferenças e controle sintético, grupos/métricas formados por SQL, estimativa com incerteza, balanceamento ou pré-tendências, placebos, relatório reproduzível e conclusão que aceite resultado negativo.

### Roteiro para preencher

- **Pergunta e estimando:** [população, tratamento, comparador, resultado e horizonte]
- **DAG:** [qual caminho de confusão foi identificado e qual conjunto de ajuste foi usado?]
- **Método e premissas:** [qual desenho foi aplicado e o que ele exige?]
- **Resultado verificável:** [estimativa, intervalo e caminho do artefato]
- **Diagnóstico/placebo:** [qual teste fortaleceu ou enfraqueceu a interpretação?]
- **Decisão:** [a evidência sustenta efeito, é inconclusiva ou rejeita a hipótese?]
- **Link:** [relatório, código ou apresentação conferidos]

### Limitação obrigatória

Explique a premissa causal mais frágil e qual dado, experimento ou falsificação seria necessário para aumentar a confiança.

### Cuidado contra afirmações falsas

Não use `causou` quando identificação, overlap, pré-tendências ou placebos falharem. Não transforme estimativa educacional em impacto empresarial. Este post não antecipa Competências ou headline.

### Checklist de publicação

- [ ] Mantive pergunta, métrica e regra de decisão definidas antes do resultado.
- [ ] Conferi estimativa, intervalo, diagnósticos e placebos.
- [ ] Mostrei premissa, limitação e resultado negativo quando ocorreu.
- [ ] Removi dados sensíveis e linguagem de impacto real.
- [ ] Testei todos os links e a reprodução do relatório.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
