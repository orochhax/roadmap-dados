<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 96 — FastAPI e contrato — 14/12/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** FastAPI e contrato.
- **Competência sugerida:** FastAPI e APIs REST.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **FastAPI e APIs REST** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **FastAPI e contrato** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** FastAPI e contrato.
- **Pasta/arquivo principal:** `01-exercicios/dia-096-fastapi-e-contrato.py`.
- **Dados:** Projetos anteriores e todos os arquivos da pasta `dados/`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Crie API FastAPI com endpoints `/health`, `/predict` e `/model-info`.
2. [ ] Defina esquema de entrada com Pydantic e exemplos válidos/invalidos.
3. [ ] Retorne probabilidade, classe, versão do modelo e aviso de uso.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Teste via documentação automática e `curl`/Postman.
- [ ] Garanta códigos HTTP claros para erro de validação e falha interna.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-096-fastapi-e-contrato.py`:** Adicione ao exemplo de /predict um cliente com mensalidade 129,90, NPS 4 e chamados_90d 5.
- [ ] **Em `01-exercicios/dia-096-fastapi-e-contrato.py`:** Teste payload sem nps e payload com mensalidade='texto'; confirme respostas de validação sem erro interno 500.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual estratégia de testes é mais adequada em **FastAPI e contrato**?

- [ ] A) Validar somente o caminho de sucesso.
- [ ] B) Depender da mesma implementação para calcular e conferir a saída.
- [ ] C) Combinar testes pequenos das regras com testes das integrações e dos contratos principais.
- [ ] D) Testar apenas manualmente depois da publicação.
- [ ] E) Criar testes que nunca falham para manter a integração verde.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual cuidado é essencial ao publicar uma aplicação de **FastAPI e contrato**?

- [ ] A) Versionar artefatos, validar configuração e segredos, registrar logs e prever uma forma segura de reversão.
- [ ] B) Usar diretamente a última alteração sem versão.
- [ ] C) Imprimir credenciais nos logs para facilitar suporte.
- [ ] D) Modificar o ambiente de produção manualmente sem registro.
- [ ] E) Remover validações para reduzir o tempo de resposta.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene uma mudança segura em **FastAPI e contrato**.

- A) Implementar uma alteração pequena e revisável.
- B) Criar ou ajustar testes que representem esse comportamento.
- C) Definir o comportamento que precisa mudar.
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
