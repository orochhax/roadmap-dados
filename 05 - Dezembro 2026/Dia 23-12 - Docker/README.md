<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 98 — Docker — 16/12/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Docker.
- **Competência sugerida:** Docker.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Docker** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Docker** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Docker.
- **Pasta/arquivo principal:** `01-exercicios/dia-098-docker.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Crie `Dockerfile` para a API com imagem enxuta, usuário não root quando possível e dependências fixadas.
2. [ ] Crie `.dockerignore` e não copie dados sensíveis.
3. [ ] Construa imagem, execute container e teste endpoints.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Passe configurações por variável de ambiente.
- [ ] Registre tamanho da imagem, tempo de build e comandos no README.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-098-docker.py`:** Execute o container com MODEL_VERSION=teste e confirme que /model-info mostra a configuração recebida.
- [ ] **Em `01-exercicios/dia-098-docker.py`:** Tente construir sem o arquivo do modelo e faça a aplicação informar a dependência ausente ao iniciar.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual estratégia de testes é mais adequada em **Docker**?

- [ ] A) Combinar testes pequenos das regras com testes das integrações e dos contratos principais.
- [ ] B) Testar apenas manualmente depois da publicação.
- [ ] C) Criar testes que nunca falham para manter a integração verde.
- [ ] D) Validar somente o caminho de sucesso.
- [ ] E) Depender da mesma implementação para calcular e conferir a saída.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual cuidado é essencial ao publicar uma aplicação de **Docker**?

- [ ] A) Imprimir credenciais nos logs para facilitar suporte.
- [ ] B) Modificar o ambiente de produção manualmente sem registro.
- [ ] C) Remover validações para reduzir o tempo de resposta.
- [ ] D) Versionar artefatos, validar configuração e segredos, registrar logs e prever uma forma segura de reversão.
- [ ] E) Usar diretamente a última alteração sem versão.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene uma mudança segura em **Docker**.

- A) Definir o comportamento que precisa mudar.
- B) Versionar, publicar e observar a mudança.
- C) Criar ou ajustar testes que representem esse comportamento.
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
