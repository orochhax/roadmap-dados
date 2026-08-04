<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 5 — Funções e primeiro mini-projeto — 07/08/2026
> [!abstract] Resultado concreto do dia
> Concluir **Funções e primeiro mini-projeto** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Funções e primeiro mini-projeto.
- **Pasta/arquivo principal:** `semana-01/dia-005-funcoes-e-primeiro-mini-projeto/` (pasta do projeto).
- **Dados:** Dados pequenos definidos nos próprios exercícios e arquivos criados por você.

### Passo a passo completo
1. [ ] Refatore os códigos dos dias 2 a 4 em funções com nomes claros, parâmetros tipados e docstrings curtas.
2. [ ] Crie `noc_insights.py` com menu: adicionar incidente, listar incidentes, calcular resumo e sair.
3. [ ] Implemente funções separadas para validar entrada, classificar prioridade, calcular métricas e formatar relatório.
4. [ ] Cadastre manualmente 10 incidentes e confirme: contagem por cidade, média de duração, prioridade mais frequente e total de clientes afetados.
5. [ ] Crie `testes_manuais.md` com 10 cenários, entrada usada, resultado obtido e status aprovado/reprovado.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Amplie um dos programas de **Funções e primeiro mini-projeto** com uma nova entrada e uma nova saída útil, aproveitando o código que você já escreveu.
- [ ] Crie dois testes inéditos para o código do dia — um uso comum e uma entrada problemática — e registre o comportamento observado em cada um.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Ao praticar **Funções e primeiro mini-projeto**, qual abordagem ajuda mais a construir uma solução correta e compreensível?

- [ ] A) Dividir o problema em etapas, usar nomes claros e conferir o comportamento do código.
- [ ] B) Copiar um código pronto e alterar valores até ele executar.
- [ ] C) Escrever tudo em uma única linha para reduzir o tamanho do arquivo.
- [ ] D) Ignorar os tipos das variáveis quando a saída parece plausível.
- [ ] E) Evitar testes para não modificar o código que já executou uma vez.

2. Qual prática reduz mais o risco de erro em um programa relacionado a **Funções e primeiro mini-projeto**?

- [ ] A) Aceitar qualquer entrada e corrigir somente se o programa fechar.
- [ ] B) Remover mensagens de erro para deixar o terminal mais limpo.
- [ ] C) Repetir o mesmo cálculo em vários lugares do arquivo.
- [ ] D) Verificar os tipos e os limites das entradas antes de realizar os cálculos.
- [ ] E) Transformar todas as entradas em texto e calcular diretamente.

3. Qual teste fornece a verificação mais completa para um exercício de **Funções e primeiro mini-projeto**?

- [ ] A) Trocar somente o nome das variáveis e comparar o tamanho do arquivo.
- [ ] B) Executar exemplos comuns, valores-limite e entradas inadequadas para observar comportamentos diferentes.
- [ ] C) Executar apenas o exemplo numérico apresentado no enunciado.
- [ ] D) Conferir somente se o arquivo foi salvo com a extensão `.py`.
- [ ] E) Ler o código sem executá-lo porque a sintaxe parece correta.

4. Ao usar um cálculo de **Funções e primeiro mini-projeto** para apoiar uma decisão, qual atitude é mais adequada?

- [ ] A) Apresentar apenas o número final sem informar de onde ele veio.
- [ ] B) Escolher a conclusão antes do cálculo e adaptar o código a ela.
- [ ] C) Considerar qualquer saída do Python como prova suficiente.
- [ ] D) Excluir valores que contradizem a primeira interpretação.
- [ ] E) Explicar o que foi calculado, conferir os dados usados e indicar as limitações da conclusão.

5. Ordene um fluxo seguro para resolver uma atividade de **Funções e primeiro mini-projeto**.

- A) Definir as entradas, as regras e a saída necessária.
- B) Implementar a solução em pequenas etapas.
- C) Executar testes com valores diferentes.
- D) Revisar o código e registrar o aprendizado.
- E) Ler o enunciado e identificar o objetivo.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene as ações para investigar um erro durante a prática de **Funções e primeiro mini-projeto**.

- A) Reproduzir o erro e observar a mensagem ou a saída.
- B) Corrigir a causa identificada.
- C) Isolar a parte do código que causa o problema.
- D) Executar novamente os testes afetados.
- E) Anotar o que provocou o erro e como ele foi corrigido.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

> [!project] Projeto semanal — Sistema Inteligente de Triagem de Incidentes
> **Desafio:** Construir uma aplicação de terminal que receba incidentes, valide campos, aplique regras configuráveis de prioridade e produza uma visão gerencial do impacto operacional.
>
> **Deve reutilizar:** Python básico, condicionais, coleções, funções e Git.
>
> **Entregáveis obrigatórios:**
> - [ ] código dividido em funções e regras carregadas de arquivo configurável;
> - [ ] ranking dos incidentes por impacto (`clientes_afetados × duração × peso da severidade`);
> - [ ] resumo por cidade, causa e prioridade;
> - [ ] dashboard simples em Markdown/HTML ou gráficos exportados;
> - [ ] relatório executivo com três ações recomendadas;
> - [ ] dez casos de teste documentados;
> - [ ] README com regras de negócio e demonstração de três minutos;
>
> **Defesa:** explicar por que a regra de priorização é coerente e mostrar um caso em que a ordem das condições altera a decisão.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Você consegue transformar regras operacionais em um sistema configurável, testável e útil para priorizar recursos?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Funções e primeiro mini-projeto.
- **Competência sugerida:** Python e desenvolvimento de mini-projetos.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Python e desenvolvimento de mini-projetos** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software`.
- **Próximo marco do perfil:** Dia 10 — Engenharia de Software | Python.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação
