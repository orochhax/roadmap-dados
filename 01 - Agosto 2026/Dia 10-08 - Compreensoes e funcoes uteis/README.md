<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 6 — Compreensões e funções úteis — 10/08/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Compreensões e funções úteis.
- **Competência sugerida:** Python e list comprehensions.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Python e list comprehensions** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software`.
- **Próximo marco do perfil:** Dia 10 — Engenharia de Software | Python.

> [!abstract] Resultado concreto do dia
> Concluir **Compreensões e funções úteis** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Compreensões e funções úteis.
- **Pasta/arquivo principal:** `01-exercicios/comprehensions.py`.
- **Dados:** Dados pequenos definidos nos próprios exercícios e arquivos criados por você.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Crie `comprehensions.py` com uma lista de 20 incidentes; gere com list comprehension apenas os P1/P2 com duração superior a 60 minutos.
2. [ ] Crie um dicionário por comprehension no formato `{cidade: total_de_incidentes}` e compare com a solução usando laço tradicional.
3. [ ] Use `enumerate` para numerar um ranking, `zip` para combinar cidades e metas, `sorted` com `key` para ordenar por duração, `any` para detectar P1 e `all` para validar durações não negativas.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Escreva três versões de uma mesma transformação: laço, comprehension legível e comprehension excessivamente compacta; explique qual manteria em produção.
- [ ] Crie cinco testes com lista vazia, cidade repetida, duração zero, valor negativo e prioridade inválida.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/comprehensions.py`:** Inclua o incidente {'cidade': 'Ilhéus', 'prioridade': 'P2', 'duracao_min': 75} e gere novamente o filtro de P1/P2 acima de 60 minutos.
- [ ] **Em `01-exercicios/comprehensions.py`:** Faça uma cópia da lista com duracao_min=-5 em um registro e confirme separadamente o valor produzido por all() antes e depois da alteração.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual prática reduz mais o risco de erro em um programa relacionado a **Compreensões e funções úteis**?

- [ ] A) Remover mensagens de erro para deixar o terminal mais limpo.
- [ ] B) Repetir o mesmo cálculo em vários lugares do arquivo.
- [ ] C) Verificar os tipos e os limites das entradas antes de realizar os cálculos.
- [ ] D) Transformar todas as entradas em texto e calcular diretamente.
- [ ] E) Aceitar qualquer entrada e corrigir somente se o programa fechar.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual teste fornece a verificação mais completa para um exercício de **Compreensões e funções úteis**?

- [ ] A) Executar exemplos comuns, valores-limite e entradas inadequadas para observar comportamentos diferentes.
- [ ] B) Executar apenas o exemplo numérico apresentado no enunciado.
- [ ] C) Conferir somente se o arquivo foi salvo com a extensão `.py`.
- [ ] D) Ler o código sem executá-lo porque a sintaxe parece correta.
- [ ] E) Trocar somente o nome das variáveis e comparar o tamanho do arquivo.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo seguro para resolver uma atividade de **Compreensões e funções úteis**.

- A) Ler o enunciado e identificar o objetivo.
- B) Definir as entradas, as regras e a saída necessária.
- C) Implementar a solução em pequenas etapas.
- D) Revisar o código e registrar o aprendizado.
- E) Executar testes com valores diferentes.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`
