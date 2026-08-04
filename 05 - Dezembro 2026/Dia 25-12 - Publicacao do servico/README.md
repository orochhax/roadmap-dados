<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 100 — Publicação do serviço — 18/12/2026
> [!abstract] Resultado concreto do dia
> Concluir **Publicação do serviço** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Publicação do serviço.
- **Pasta/arquivo principal:** `semana-20/dia-100-publicacao-do-servico/` (pasta do projeto).
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Passo a passo completo
1. [ ] Publique localmente via Docker Compose ou em serviço gratuito compatível, quando disponível.
2. [ ] Execute teste de ponta a ponta com dados novos.
3. [ ] Crie página de documentação para consumidores da API.
4. [ ] Faça teste de carga leve e registre limites.
5. [ ] Grave demonstração de cinco minutos do dado até resposta.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Adicione ao artefato de **Publicação do serviço** um teste automatizado ou uma entrada inválida que ainda não estava coberta.
- [ ] Simule uma falha de configuração, dependência ou serviço e registre como detectá-la e como recuperar o sistema.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Publique localmente via Docker Compose ou em serviço gratuito compatível, quando disponível.

   **Pergunta:** Qual prática melhora a manutenção de uma solução de **Publicação do serviço**?

- [ ] A) Separar responsabilidades, usar configuração explícita e manter mudanças pequenas e versionadas.
- [ ] B) Colocar dados, regras e execução em uma única função.
- [ ] C) Salvar segredos diretamente no código.
- [ ] D) Alterar vários comportamentos sem registrar o motivo.
- [ ] E) Duplicar trechos para evitar criar funções.

2. **Referência — atividade 2:** Execute teste de ponta a ponta com dados novos.

   **Pergunta:** Qual estratégia de testes é mais adequada em **Publicação do serviço**?

- [ ] A) Criar testes que nunca falham para manter a integração verde.
- [ ] B) Validar somente o caminho de sucesso.
- [ ] C) Depender da mesma implementação para calcular e conferir a saída.
- [ ] D) Combinar testes pequenos das regras com testes das integrações e dos contratos principais.
- [ ] E) Testar apenas manualmente depois da publicação.

3. **Referência — atividade 3:** Crie página de documentação para consumidores da API.

   **Pergunta:** Qual cuidado é essencial ao publicar uma aplicação de **Publicação do serviço**?

- [ ] A) Remover validações para reduzir o tempo de resposta.
- [ ] B) Versionar artefatos, validar configuração e segredos, registrar logs e prever uma forma segura de reversão.
- [ ] C) Usar diretamente a última alteração sem versão.
- [ ] D) Imprimir credenciais nos logs para facilitar suporte.
- [ ] E) Modificar o ambiente de produção manualmente sem registro.

4. **Referência — atividade 4:** Faça teste de carga leve e registre limites.

   **Pergunta:** Como saber se uma solução de **Publicação do serviço** continua saudável após a publicação?

- [ ] A) Conferir somente se o computador do desenvolvedor está ligado.
- [ ] B) Considerar ausência de reclamações como prova suficiente.
- [ ] C) Observar apenas o uso de memória uma vez por mês.
- [ ] D) Avaliar somente a métrica obtida durante o treinamento.
- [ ] E) Monitorar disponibilidade, erros, latência, qualidade das entradas e comportamento das saídas.

5. **Referência — atividade 5:** Grave demonstração de cinco minutos do dado até resposta.

   **Pergunta:** Ordene uma mudança segura em **Publicação do serviço**.

- A) Definir o comportamento que precisa mudar.
- B) Criar ou ajustar testes que representem esse comportamento.
- C) Versionar, publicar e observar a mudança.
- D) Executar verificações locais e de integração.
- E) Implementar uma alteração pequena e revisável.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a resposta a um problema após publicar **Publicação do serviço**.

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

> [!todo] PUBLICAR NO LINKEDIN — projeto prioritário do portfólio
> - [ ] Publique somente após README, resultados e limitações estarem revisados.
> - [ ] Inclua problema, abordagem, principal evidência, decisão e link do GitHub.
> - [ ] **Ângulo sugerido:** demonstrar como você transformou um notebook em serviço consumível, testado e executável com Docker.

> [!project] Projeto semanal — API de scoring containerizada
> **Desafio:** Disponibilizar um modelo por API com contrato, validação, logs e Docker.
>
> **Deve reutilizar:** Modelo anterior, FastAPI, testes e Docker.
>
> **Entregáveis obrigatórios:**
> - [ ] endpoint de saúde e previsão;
> - [ ] schema de entrada/saída;
> - [ ] imagem Docker;
> - [ ] testes de integração;
> - [ ] guia de execução;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Seu modelo deixou de ser apenas um notebook e pode ser consumido por outra aplicação?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Publicação do serviço.
- **Competência sugerida:** Implantação de modelos.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Implantação de modelos** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.
