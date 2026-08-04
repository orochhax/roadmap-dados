<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 98 — Docker — 16/12/2026
> [!abstract] Resultado concreto do dia
> Concluir **Docker** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Docker.
- **Pasta/arquivo principal:** `01-exercicios/dia-098-docker.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Passo a passo completo
1. [ ] Crie `Dockerfile` para a API com imagem enxuta, usuário não root quando possível e dependências fixadas.
2. [ ] Crie `.dockerignore` e não copie dados sensíveis.
3. [ ] Construa imagem, execute container e teste endpoints.
4. [ ] Passe configurações por variável de ambiente.
5. [ ] Registre tamanho da imagem, tempo de build e comandos no README.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-098-docker.py`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-098-docker.py`:** Execute o container com MODEL_VERSION=teste e confirme que /model-info mostra a configuração recebida.
- [ ] **Em `01-exercicios/dia-098-docker.py`:** Tente construir sem o arquivo do modelo e faça a aplicação informar a dependência ausente ao iniciar.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Crie `Dockerfile` para a API com imagem enxuta, usuário não root quando possível e dependências fixadas.

   **Pergunta:** Qual prática melhora a manutenção de uma solução de **Docker**?

- [ ] A) Alterar vários comportamentos sem registrar o motivo.
- [ ] B) Duplicar trechos para evitar criar funções.
- [ ] C) Separar responsabilidades, usar configuração explícita e manter mudanças pequenas e versionadas.
- [ ] D) Colocar dados, regras e execução em uma única função.
- [ ] E) Salvar segredos diretamente no código.

2. **Referência — atividade 2:** Crie `.dockerignore` e não copie dados sensíveis.

   **Pergunta:** Qual estratégia de testes é mais adequada em **Docker**?

- [ ] A) Combinar testes pequenos das regras com testes das integrações e dos contratos principais.
- [ ] B) Testar apenas manualmente depois da publicação.
- [ ] C) Criar testes que nunca falham para manter a integração verde.
- [ ] D) Validar somente o caminho de sucesso.
- [ ] E) Depender da mesma implementação para calcular e conferir a saída.

3. **Referência — atividade 3:** Construa imagem, execute container e teste endpoints.

   **Pergunta:** Qual cuidado é essencial ao publicar uma aplicação de **Docker**?

- [ ] A) Imprimir credenciais nos logs para facilitar suporte.
- [ ] B) Modificar o ambiente de produção manualmente sem registro.
- [ ] C) Remover validações para reduzir o tempo de resposta.
- [ ] D) Versionar artefatos, validar configuração e segredos, registrar logs e prever uma forma segura de reversão.
- [ ] E) Usar diretamente a última alteração sem versão.

4. **Referência — atividade 4:** Passe configurações por variável de ambiente.

   **Pergunta:** Como saber se uma solução de **Docker** continua saudável após a publicação?

- [ ] A) Avaliar somente a métrica obtida durante o treinamento.
- [ ] B) Monitorar disponibilidade, erros, latência, qualidade das entradas e comportamento das saídas.
- [ ] C) Conferir somente se o computador do desenvolvedor está ligado.
- [ ] D) Considerar ausência de reclamações como prova suficiente.
- [ ] E) Observar apenas o uso de memória uma vez por mês.

5. **Referência — atividade 5:** Registre tamanho da imagem, tempo de build e comandos no README.

   **Pergunta:** Ordene uma mudança segura em **Docker**.

- A) Definir o comportamento que precisa mudar.
- B) Versionar, publicar e observar a mudança.
- C) Criar ou ajustar testes que representem esse comportamento.
- D) Executar verificações locais e de integração.
- E) Implementar uma alteração pequena e revisável.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a resposta a um problema após publicar **Docker**.

- A) Detectar o sintoma por métricas, logs ou alerta.
- B) Republicar com controle e documentar o incidente.
- C) Delimitar usuários, versões e componentes afetados.
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

- **Conhecimento praticado hoje:** Docker.
- **Competência sugerida:** Docker.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Docker** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
