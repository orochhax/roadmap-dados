<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 95 — CI e versão estável — 11/12/2026
> [!abstract] Resultado concreto do dia
> Concluir **CI e versão estável** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** CI e versão estável.
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Passo a passo completo
1. [ ] Crie workflow de CI que instale dependências e rode testes em cada push/PR.
2. [ ] Adicione badge de testes ao README.
3. [ ] Quebre um teste propositalmente para verificar bloqueio.
4. [ ] Corrija e gere release `v1.0.0` com changelog.
5. [ ] Faça revisão final usando checklist de PR.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/roteiro_atividades.md`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Acrescente à CI uma etapa que execute pytest e outra que verifique formatação; faça ambas rodarem em pull request.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Crie um teste que falha, observe a CI bloquear, corrija e registre os dois commits separadamente.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Crie workflow de CI que instale dependências e rode testes em cada push/PR.

   **Pergunta:** Qual prática melhora a manutenção de uma solução de **CI e versão estável**?

- [ ] A) Separar responsabilidades, usar configuração explícita e manter mudanças pequenas e versionadas.
- [ ] B) Colocar dados, regras e execução em uma única função.
- [ ] C) Salvar segredos diretamente no código.
- [ ] D) Alterar vários comportamentos sem registrar o motivo.
- [ ] E) Duplicar trechos para evitar criar funções.

2. **Referência — atividade 2:** Adicione badge de testes ao README.

   **Pergunta:** Qual estratégia de testes é mais adequada em **CI e versão estável**?

- [ ] A) Criar testes que nunca falham para manter a integração verde.
- [ ] B) Validar somente o caminho de sucesso.
- [ ] C) Depender da mesma implementação para calcular e conferir a saída.
- [ ] D) Combinar testes pequenos das regras com testes das integrações e dos contratos principais.
- [ ] E) Testar apenas manualmente depois da publicação.

3. **Referência — atividade 3:** Quebre um teste propositalmente para verificar bloqueio.

   **Pergunta:** Qual cuidado é essencial ao publicar uma aplicação de **CI e versão estável**?

- [ ] A) Remover validações para reduzir o tempo de resposta.
- [ ] B) Versionar artefatos, validar configuração e segredos, registrar logs e prever uma forma segura de reversão.
- [ ] C) Usar diretamente a última alteração sem versão.
- [ ] D) Imprimir credenciais nos logs para facilitar suporte.
- [ ] E) Modificar o ambiente de produção manualmente sem registro.

4. **Referência — atividade 4:** Corrija e gere release `v1.0.0` com changelog.

   **Pergunta:** Como saber se uma solução de **CI e versão estável** continua saudável após a publicação?

- [ ] A) Conferir somente se o computador do desenvolvedor está ligado.
- [ ] B) Considerar ausência de reclamações como prova suficiente.
- [ ] C) Observar apenas o uso de memória uma vez por mês.
- [ ] D) Avaliar somente a métrica obtida durante o treinamento.
- [ ] E) Monitorar disponibilidade, erros, latência, qualidade das entradas e comportamento das saídas.

5. **Referência — atividade 5:** Faça revisão final usando checklist de PR.

   **Pergunta:** Ordene uma mudança segura em **CI e versão estável**.

- A) Definir o comportamento que precisa mudar.
- B) Implementar uma alteração pequena e revisável.
- C) Criar ou ajustar testes que representem esse comportamento.
- D) Versionar, publicar e observar a mudança.
- E) Executar verificações locais e de integração.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a resposta a um problema após publicar **CI e versão estável**.

- A) Detectar o sintoma por métricas, logs ou alerta.
- B) Delimitar usuários, versões e componentes afetados.
- C) Conter o impacto ou reverter para uma versão estável.
- D) Republicar com controle e documentar o incidente.
- E) Corrigir a causa e validar com testes.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

> [!project] Projeto semanal — Do notebook ao pacote testável
> **Desafio:** Transformar um notebook de modelagem em código modular, configurável e coberto por testes.
>
> **Deve reutilizar:** Git, engenharia de software e projeto anterior.
>
> **Entregáveis obrigatórios:**
> - [ ] pacote Python;
> - [ ] configuração externa;
> - [ ] testes automatizados;
> - [ ] CI simples;
> - [ ] release versionada;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Outro desenvolvedor consegue clonar, instalar, testar e executar seu projeto sem falar com você?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** CI e versão estável.
- **Competência sugerida:** Integração Contínua (CI).
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Integração Contínua (CI)** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
