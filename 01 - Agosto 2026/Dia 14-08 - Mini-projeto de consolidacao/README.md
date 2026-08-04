<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 10 — Mini-projeto de consolidação — 14/08/2026
> [!abstract] Resultado concreto do dia
> Concluir **Mini-projeto de consolidação** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Mini-projeto de consolidação.
- **Pasta/arquivo principal:** `semana-02/dia-010-mini-projeto-de-consolidacao/` (pasta do projeto).
- **Dados:** Dados pequenos definidos nos próprios exercícios e arquivos criados por você.

### Passo a passo completo
1. [ ] Crie uma pasta `projeto_semana02` e copie somente os módulos realmente necessários, sem levar arquivos temporários.
2. [ ] Implemente uma aplicação que leia CSV ou JSON, valide esquema, consolide incidentes e gere `resumo.json` e `relatorio.csv`.
3. [ ] Defina no README cinco regras de qualidade: campos obrigatórios, tipos, valores permitidos, limites numéricos e tratamento de duplicados.
4. [ ] Crie 15 casos de teste divididos em cinco válidos, cinco inválidos e cinco casos de borda.
5. [ ] Execute o projeto em ambiente virtual novo, grave uma demonstração de até cinco minutos e registre três limitações.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Amplie um dos programas de **Mini-projeto de consolidação** com uma nova entrada e uma nova saída útil, aproveitando o código que você já escreveu.
- [ ] Crie dois testes inéditos para o código do dia — um uso comum e uma entrada problemática — e registre o comportamento observado em cada um.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Crie uma pasta `projeto_semana02` e copie somente os módulos realmente necessários, sem levar arquivos temporários.

   **Pergunta:** Ao praticar **Mini-projeto de consolidação**, qual abordagem ajuda mais a construir uma solução correta e compreensível?

- [ ] A) Dividir o problema em etapas, usar nomes claros e conferir o comportamento do código.
- [ ] B) Copiar um código pronto e alterar valores até ele executar.
- [ ] C) Escrever tudo em uma única linha para reduzir o tamanho do arquivo.
- [ ] D) Ignorar os tipos das variáveis quando a saída parece plausível.
- [ ] E) Evitar testes para não modificar o código que já executou uma vez.

2. **Referência — atividade 2:** Implemente uma aplicação que leia CSV ou JSON, valide esquema, consolide incidentes e gere `resumo.json` e `relatorio.csv`.

   **Pergunta:** Qual prática reduz mais o risco de erro em um programa relacionado a **Mini-projeto de consolidação**?

- [ ] A) Aceitar qualquer entrada e corrigir somente se o programa fechar.
- [ ] B) Remover mensagens de erro para deixar o terminal mais limpo.
- [ ] C) Repetir o mesmo cálculo em vários lugares do arquivo.
- [ ] D) Verificar os tipos e os limites das entradas antes de realizar os cálculos.
- [ ] E) Transformar todas as entradas em texto e calcular diretamente.

3. **Referência — atividade 3:** Defina no README cinco regras de qualidade: campos obrigatórios, tipos, valores permitidos, limites numéricos e tratamento de duplicados.

   **Pergunta:** Qual teste fornece a verificação mais completa para um exercício de **Mini-projeto de consolidação**?

- [ ] A) Trocar somente o nome das variáveis e comparar o tamanho do arquivo.
- [ ] B) Executar exemplos comuns, valores-limite e entradas inadequadas para observar comportamentos diferentes.
- [ ] C) Executar apenas o exemplo numérico apresentado no enunciado.
- [ ] D) Conferir somente se o arquivo foi salvo com a extensão `.py`.
- [ ] E) Ler o código sem executá-lo porque a sintaxe parece correta.

4. **Referência — atividade 4:** Crie 15 casos de teste divididos em cinco válidos, cinco inválidos e cinco casos de borda.

   **Pergunta:** Ao usar um cálculo de **Mini-projeto de consolidação** para apoiar uma decisão, qual atitude é mais adequada?

- [ ] A) Apresentar apenas o número final sem informar de onde ele veio.
- [ ] B) Escolher a conclusão antes do cálculo e adaptar o código a ela.
- [ ] C) Considerar qualquer saída do Python como prova suficiente.
- [ ] D) Excluir valores que contradizem a primeira interpretação.
- [ ] E) Explicar o que foi calculado, conferir os dados usados e indicar as limitações da conclusão.

5. **Referência — atividade 5:** Execute o projeto em ambiente virtual novo, grave uma demonstração de até cinco minutos e registre três limitações.

   **Pergunta:** Ordene um fluxo seguro para resolver uma atividade de **Mini-projeto de consolidação**.

- A) Ler o enunciado e identificar o objetivo.
- B) Implementar a solução em pequenas etapas.
- C) Definir as entradas, as regras e a saída necessária.
- D) Executar testes com valores diferentes.
- E) Revisar o código e registrar o aprendizado.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene as ações para investigar um erro durante a prática de **Mini-projeto de consolidação**.

- A) Anotar o que provocou o erro e como ele foi corrigido.
- B) Isolar a parte do código que causa o problema.
- C) Corrigir a causa identificada.
- D) Executar novamente os testes afetados.
- E) Reproduzir o erro e observar a mensagem ou a saída.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

> [!project] Projeto semanal — Pipeline de Qualidade de Dados Operacionais
> **Desafio:** Ingerir arquivos CSV e JSON de fontes diferentes, validar esquema e regras, separar registros aprovados/rejeitados e publicar uma base confiável para análise.
>
> **Deve reutilizar:** Python da semana 1, arquivos, exceções, módulos e ambientes.
>
> **Entregáveis obrigatórios:**
> - [ ] pipeline executável por comando e idempotente para a mesma entrada;
> - [ ] contagem de registros recebidos, aprovados, rejeitados e duplicados;
> - [ ] percentual rejeitado e ranking dos motivos de rejeição;
> - [ ] comparação antes/depois da qualidade dos dados;
> - [ ] registro de linhagem: arquivo de origem, horário, versão e transformação aplicada;
> - [ ] saídas CSV e JSON, relatório de qualidade, README e fluxograma;
>
> **Defesa:** demonstrar que um erro de origem não contamina silenciosamente a base publicada e explicar como rastrear cada registro.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Você consegue provar quantos registros foram processados, por que alguns foram rejeitados e de onde veio cada dado publicado?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Mini-projeto de consolidação.
- **Competência sugerida:** Python e construção de pipelines.
- **Ação recomendada:** Após concluir todas as atividades do dia, atualize o título profissional e adicione ou reforce **Python e construção de pipelines** na seção Competências. Se a entrega estiver revisada e apresentável, inclua-a também em Projetos ou Destaques.
- **Novo título sugerido:** `Engenharia de Software | Python`.
- **Próximo marco do perfil:** Dia 20 — Engenharia de Software | Análise de Dados | Python e Power BI.
