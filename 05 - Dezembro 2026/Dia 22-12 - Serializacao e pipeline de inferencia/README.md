<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 97 — Serialização e pipeline de inferência — 15/12/2026
> [!abstract] Resultado concreto do dia
> Concluir **Serialização e pipeline de inferência** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Serialização e pipeline de inferência.
- **Pasta/arquivo principal:** `01-exercicios/dia-097-serializacao-e-pipeline-de-inferencia.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Passo a passo completo
1. [ ] Serializa pipeline completa com `joblib` e registre versão, data e features esperadas.
2. [ ] Crie módulo de inferência que carrega o modelo uma vez.
3. [ ] Valide ordem, tipo e categorias de entrada.
4. [ ] Compare 20 previsões do notebook e API; devem coincidir.
5. [ ] Teste modelo inexistente, arquivo corrompido e campo extra.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-097-serializacao-e-pipeline-de-inferencia.py`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-097-serializacao-e-pipeline-de-inferencia.py`:** Compare 20 previsões com ids fixos entre notebook e módulo carregado e liste qualquer diferença maior que 0,000001.
- [ ] **Em `01-exercicios/dia-097-serializacao-e-pipeline-de-inferencia.py`:** Teste caminho de modelo inexistente e uma entrada com coluna extra segredo; trate os dois casos separadamente.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Serializa pipeline completa com `joblib` e registre versão, data e features esperadas.

   **Pergunta:** Qual prática melhora a manutenção de uma solução de **Serialização e pipeline de inferência**?

- [ ] A) Salvar segredos diretamente no código.
- [ ] B) Alterar vários comportamentos sem registrar o motivo.
- [ ] C) Duplicar trechos para evitar criar funções.
- [ ] D) Separar responsabilidades, usar configuração explícita e manter mudanças pequenas e versionadas.
- [ ] E) Colocar dados, regras e execução em uma única função.

2. **Referência — atividade 2:** Crie módulo de inferência que carrega o modelo uma vez.

   **Pergunta:** Qual estratégia de testes é mais adequada em **Serialização e pipeline de inferência**?

- [ ] A) Depender da mesma implementação para calcular e conferir a saída.
- [ ] B) Combinar testes pequenos das regras com testes das integrações e dos contratos principais.
- [ ] C) Testar apenas manualmente depois da publicação.
- [ ] D) Criar testes que nunca falham para manter a integração verde.
- [ ] E) Validar somente o caminho de sucesso.

3. **Referência — atividade 3:** Valide ordem, tipo e categorias de entrada.

   **Pergunta:** Qual cuidado é essencial ao publicar uma aplicação de **Serialização e pipeline de inferência**?

- [ ] A) Usar diretamente a última alteração sem versão.
- [ ] B) Imprimir credenciais nos logs para facilitar suporte.
- [ ] C) Modificar o ambiente de produção manualmente sem registro.
- [ ] D) Remover validações para reduzir o tempo de resposta.
- [ ] E) Versionar artefatos, validar configuração e segredos, registrar logs e prever uma forma segura de reversão.

4. **Referência — atividade 4:** Compare 20 previsões do notebook e API; devem coincidir.

   **Pergunta:** Como saber se uma solução de **Serialização e pipeline de inferência** continua saudável após a publicação?

- [ ] A) Observar apenas o uso de memória uma vez por mês.
- [ ] B) Avaliar somente a métrica obtida durante o treinamento.
- [ ] C) Monitorar disponibilidade, erros, latência, qualidade das entradas e comportamento das saídas.
- [ ] D) Conferir somente se o computador do desenvolvedor está ligado.
- [ ] E) Considerar ausência de reclamações como prova suficiente.

5. **Referência — atividade 5:** Teste modelo inexistente, arquivo corrompido e campo extra.

   **Pergunta:** Ordene uma mudança segura em **Serialização e pipeline de inferência**.

- A) Definir o comportamento que precisa mudar.
- B) Criar ou ajustar testes que representem esse comportamento.
- C) Implementar uma alteração pequena e revisável.
- D) Versionar, publicar e observar a mudança.
- E) Executar verificações locais e de integração.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a resposta a um problema após publicar **Serialização e pipeline de inferência**.

- A) Detectar o sintoma por métricas, logs ou alerta.
- B) Delimitar usuários, versões e componentes afetados.
- C) Republicar com controle e documentar o incidente.
- D) Corrigir a causa e validar com testes.
- E) Conter o impacto ou reverter para uma versão estável.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Serialização e pipeline de inferência.
- **Competência sugerida:** Serialização de modelos e inferência.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Serialização de modelos e inferência** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
