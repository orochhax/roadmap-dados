<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 99 — Logs e monitoramento básico — 17/12/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Logs e monitoramento básico.
- **Competência sugerida:** Logs e monitoramento.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Logs e monitoramento** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Logs e monitoramento básico** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Logs e monitoramento básico.
- **Pasta/arquivo principal:** `01-exercicios/dia-099-logs-e-monitoramento-basico.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Adicione logs de requisição com tempo, status e versão sem registrar dados sensíveis.
2. [ ] Meça contagem, latência e erros em 20 requisições válidas e cinco inválidas.
3. [ ] Defina um alerta conceitual e escreva um runbook curto para investigá-lo.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Amplie para 100 requisições somente para observar percentis com uma amostra maior.
- [ ] Distribuição de probabilidades e drift ficam como extensão após as métricas operacionais básicas.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-099-logs-e-monitoramento-basico.py`:** Simule 50 requisições com latência adicional de 200 ms e compare p50 e p95 com as requisições normais.
- [ ] **Em `01-exercicios/dia-099-logs-e-monitoramento-basico.py`:** Envie 10 payloads sem campo obrigatório e confirme que logs contam erros sem registrar o conteúdo completo.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual estratégia de testes é mais adequada em **Logs e monitoramento básico**?

- [ ] A) Testar apenas manualmente depois da publicação.
- [ ] B) Criar testes que nunca falham para manter a integração verde.
- [ ] C) Validar somente o caminho de sucesso.
- [ ] D) Depender da mesma implementação para calcular e conferir a saída.
- [ ] E) Combinar testes pequenos das regras com testes das integrações e dos contratos principais.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual cuidado é essencial ao publicar uma aplicação de **Logs e monitoramento básico**?

- [ ] A) Modificar o ambiente de produção manualmente sem registro.
- [ ] B) Remover validações para reduzir o tempo de resposta.
- [ ] C) Versionar artefatos, validar configuração e segredos, registrar logs e prever uma forma segura de reversão.
- [ ] D) Usar diretamente a última alteração sem versão.
- [ ] E) Imprimir credenciais nos logs para facilitar suporte.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene uma mudança segura em **Logs e monitoramento básico**.

- A) Versionar, publicar e observar a mudança.
- B) Criar ou ajustar testes que representem esse comportamento.
- C) Definir o comportamento que precisa mudar.
- D) Executar verificações locais e de integração.
- E) Implementar uma alteração pequena e revisável.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`
