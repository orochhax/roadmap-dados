<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 97 — Serialização e pipeline de inferência — 15/12/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Serialização e pipeline de inferência.
- **Competência sugerida:** Serialização de modelos e inferência.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Serialização de modelos e inferência** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Serialização e pipeline de inferência** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Serialização e pipeline de inferência.
- **Pasta/arquivo principal:** `01-exercicios/dia-097-serializacao-e-pipeline-de-inferencia.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Serializa pipeline completa com `joblib` e registre versão, data e features esperadas.
2. [ ] Crie módulo de inferência que carrega o modelo uma vez.
3. [ ] Valide ordem, tipo e categorias de entrada.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Compare 20 previsões do notebook e API; devem coincidir.
- [ ] Teste modelo inexistente, arquivo corrompido e campo extra.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-097-serializacao-e-pipeline-de-inferencia.py`:** Compare 20 previsões com ids fixos entre notebook e módulo carregado e liste qualquer diferença maior que 0,000001.
- [ ] **Em `01-exercicios/dia-097-serializacao-e-pipeline-de-inferencia.py`:** Teste caminho de modelo inexistente e uma entrada com coluna extra segredo; trate os dois casos separadamente.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual estratégia de testes é mais adequada em **Serialização e pipeline de inferência**?

- [ ] A) Depender da mesma implementação para calcular e conferir a saída.
- [ ] B) Combinar testes pequenos das regras com testes das integrações e dos contratos principais.
- [ ] C) Testar apenas manualmente depois da publicação.
- [ ] D) Criar testes que nunca falham para manter a integração verde.
- [ ] E) Validar somente o caminho de sucesso.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual cuidado é essencial ao publicar uma aplicação de **Serialização e pipeline de inferência**?

- [ ] A) Usar diretamente a última alteração sem versão.
- [ ] B) Imprimir credenciais nos logs para facilitar suporte.
- [ ] C) Modificar o ambiente de produção manualmente sem registro.
- [ ] D) Remover validações para reduzir o tempo de resposta.
- [ ] E) Versionar artefatos, validar configuração e segredos, registrar logs e prever uma forma segura de reversão.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene uma mudança segura em **Serialização e pipeline de inferência**.

- A) Definir o comportamento que precisa mudar.
- B) Criar ou ajustar testes que representem esse comportamento.
- C) Implementar uma alteração pequena e revisável.
- D) Versionar, publicar e observar a mudança.
- E) Executar verificações locais e de integração.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`
