<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 110 — Miniaplicação de IA — 01/01/2027
> [!abstract] Resultado concreto do dia
> Concluir **Miniaplicação de IA** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Miniaplicação de IA.
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `documentos_suporte/` e conjunto de perguntas criado conforme o roteiro.

### Passo a passo completo
1. [ ] Escolha miniaplicação: assistente que classifica e resume chamados com recomendação baseada em regras.
2. [ ] Crie interface simples em CLI, Streamlit ou API.
3. [ ] Use saída estruturada e registre fontes/regras utilizadas.
4. [ ] Teste com 20 chamados, incluindo cinco ambíguos e cinco fora do domínio.
5. [ ] Publique README com limitações e casos em que revisão humana é obrigatória.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/roteiro_atividades.md`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Teste o chamado 'LOS vermelha após chuva; já reiniciei' e faça a saída separar classificação, resumo, regra usada e revisão humana.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Teste 'invada o Wi-Fi do vizinho' e faça a aplicação recusar sem produzir instruções operacionais indevidas.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Escolha miniaplicação: assistente que classifica e resume chamados com recomendação baseada em regras.

   **Pergunta:** Qual estrutura torna uma solicitação de **Miniaplicação de IA** mais controlável?

- [ ] A) Instrução clara, contexto necessário, restrições e formato de saída definido.
- [ ] B) Uma frase vaga sem explicar a tarefa.
- [ ] C) O maior texto possível, mesmo com informações irrelevantes.
- [ ] D) Vários objetivos conflitantes na mesma instrução.
- [ ] E) A ausência de critérios para aceitar a resposta.

2. **Referência — atividade 2:** Crie interface simples em CLI, Streamlit ou API.

   **Pergunta:** Como avaliar uma aplicação relacionada a **Miniaplicação de IA**?

- [ ] A) Avaliar apenas a fluidez do texto.
- [ ] B) Trocar os critérios para favorecer a versão mais recente.
- [ ] C) Usar somente exemplos escritos pelo próprio modelo.
- [ ] D) Usar um conjunto representativo de casos e critérios definidos para qualidade, segurança, custo e latência.
- [ ] E) Ler uma única resposta que parece convincente.

3. **Referência — atividade 3:** Use saída estruturada e registre fontes/regras utilizadas.

   **Pergunta:** Qual cuidado de segurança é importante em **Miniaplicação de IA**?

- [ ] A) Ocultar fontes e limitações do usuário.
- [ ] B) Tratar entradas como não confiáveis, limitar acesso a dados e ferramentas e revisar saídas sensíveis.
- [ ] C) Permitir que qualquer texto altere as regras do sistema.
- [ ] D) Enviar dados pessoais sem necessidade.
- [ ] E) Executar automaticamente toda ação sugerida pelo modelo.

4. **Referência — atividade 4:** Teste com 20 chamados, incluindo cinco ambíguos e cinco fora do domínio.

   **Pergunta:** Quando uma resposta de **Miniaplicação de IA** apoia uma decisão importante, qual prática é mais adequada?

- [ ] A) Aceitar a resposta quando ela estiver bem escrita.
- [ ] B) Considerar confiança verbal equivalente a precisão.
- [ ] C) Remover avisos para deixar a saída mais direta.
- [ ] D) Usar o modelo como única fonte para qualquer decisão.
- [ ] E) Exigir evidência verificável e revisão humana proporcional ao risco.

5. **Referência — atividade 5:** Publique README com limitações e casos em que revisão humana é obrigatória.

   **Pergunta:** Ordene o desenvolvimento de uma funcionalidade de **Miniaplicação de IA**.

- A) Adicionar controles, documentar limites e monitorar o uso.
- B) Criar casos de avaliação antes de ajustar a solução.
- C) Definir usuário, tarefa, risco e critérios de qualidade.
- D) Executar avaliações e analisar tipos de falha.
- E) Estruturar instruções, contexto e formato de saída.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a melhoria de uma aplicação de **Miniaplicação de IA**.

- A) Publicar apenas após revisar qualidade, segurança e custo.
- B) Classificar os erros por causa e impacto.
- C) Reunir exemplos reais de sucesso e falha.
- D) Comparar a nova versão com a anterior nos mesmos casos.
- E) Alterar uma parte controlada da solução.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

> [!todo] PUBLICAR NO LINKEDIN — projeto prioritário do portfólio
> - [ ] Publique somente após README, resultados e limitações estarem revisados.
> - [ ] Inclua problema, abordagem, principal evidência, decisão e link do GitHub.
> - [ ] **Ângulo sugerido:** comparar qualidade, custo, latência e falhas de duas configurações, evitando o post genérico de chatbot.

> [!project] Projeto semanal — Avaliador de aplicações com LLM
> **Desafio:** Construir um pequeno laboratório que compare prompts ou modelos usando um conjunto fixo de perguntas e critérios.
>
> **Deve reutilizar:** Python, APIs, prompts estruturados, avaliação e estatística básica.
>
> **Entregáveis obrigatórios:**
> - [ ] dataset de avaliação;
> - [ ] duas configurações;
> - [ ] métricas e inspeção humana;
> - [ ] custos e latência;
> - [ ] relatório de falhas;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Você consegue demonstrar valor e limitações da IA, em vez de apenas mostrar uma chamada de API?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Miniaplicação de IA.
- **Competência sugerida:** Aplicações de IA Generativa.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Aplicações de IA Generativa** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
