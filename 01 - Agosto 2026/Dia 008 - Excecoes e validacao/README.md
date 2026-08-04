<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 8 — Exceções e validação — 12/08/2026
> [!abstract] Resultado concreto do dia
> Concluir **Exceções e validação** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Exceções e validação.
- **Pasta/arquivo principal:** `semana-02/dia-008-excecoes-e-validacao.py`.
- **Dados:** Dados pequenos definidos nos próprios exercícios e arquivos criados por você.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Crie uma cópia do CSV do dia anterior com cinco erros: duração vazia, texto em clientes, severidade inválida, cidade ausente e booleano escrito errado.
2. [ ] Implemente `validar_linha()` que retorne uma lista de erros, sem interromper o processamento das demais linhas.
3. [ ] Use `try/except` apenas nos pontos em que a conversão pode falhar; não envolva o programa inteiro em um único `except`.
4. [ ] Grave linhas válidas em `dados_validos.csv` e inválidas em `dados_rejeitados.csv` com uma coluna `motivo_rejeicao`.
5. [ ] Crie uma tabela de testes com oito casos e confirme que nenhuma linha inválida entra silenciosamente no arquivo final.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Amplie um dos programas de **Exceções e validação** com uma nova entrada e uma nova saída útil, aproveitando o código que você já escreveu.
- [ ] Crie dois testes inéditos para o código do dia — um uso comum e uma entrada problemática — e registre o resultado esperado antes de executar.

### Perguntas de checagem
1. Por que capturar `Exception` genericamente pode esconder defeitos, e quando usar `raise`?

**Resposta:**

2. Em qual exercício de **Exceções e validação** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Exceções e validação** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

5. Que parte da sua solução de **Exceções e validação** ficaria mais difícil de manter se novas regras fossem adicionadas?

**Resposta:**

6. Qual escolha de organização, tipo de dado ou validação foi mais importante neste dia e que erro ela evita?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Commit realizado com mensagem no formato `dia-008: excecoes-e-validacao`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

---

## Anotações pessoais

### Resultado esperado antes de executar


### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação
