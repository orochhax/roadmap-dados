<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 120 — Teste, apresentação e retrospectiva — 15/01/2027
> [!abstract] Resultado concreto do dia
> Concluir **Teste, apresentação e retrospectiva** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Teste, apresentação e retrospectiva.
- **Pasta/arquivo principal:** `semana-24/dia-120-teste-apresentacao-e-retrospectiva/` (pasta do projeto).
- **Dados:** Projetos e dados acumulados durante o roadmap.

### Passo a passo completo
1. [ ] Execute testes funcionais, de dados e de decisão.
2. [ ] Peça revisão externa e registre pelo menos cinco feedbacks.
3. [ ] Corrija itens críticos e faça release.
4. [ ] Apresente em oito minutos para público técnico e executivo.
5. [ ] Escreva retrospectiva e lições para o TCC.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Acrescente um cenário de uso ponta a ponta ainda não coberto em **Teste, apresentação e retrospectiva** e acompanhe os dados da entrada até a saída.
- [ ] Escolha uma falha provável do produto e adicione uma validação, mensagem ou teste que a torne visível.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Qual decisão deve orientar um produto de **Teste, apresentação e retrospectiva**?

- [ ] A) Resolver uma necessidade clara de um usuário com uma saída que apoie uma ação mensurável.
- [ ] B) Incluir o maior número possível de tecnologias.
- [ ] C) Começar pela interface sem definir o problema.
- [ ] D) Treinar um modelo antes de conhecer os dados.
- [ ] E) Trocar o objetivo sempre que surgir uma ferramenta nova.

2. O que reduz falhas entre componentes em **Teste, apresentação e retrospectiva**?

- [ ] A) Alterar formatos sem avisar os consumidores.
- [ ] B) Depender de passos manuais não documentados.
- [ ] C) Compartilhar estado interno sem uma interface definida.
- [ ] D) Contratos explícitos para dados, esquemas, entradas, saídas, versões e tratamento de erros.
- [ ] E) Cada componente interpretar os campos de uma forma.

3. Qual teste oferece mais confiança em uma entrega de **Teste, apresentação e retrospectiva**?

- [ ] A) Ignorar erros externos quando o código local funciona.
- [ ] B) Executar o fluxo completo com casos representativos e simular falhas nas principais integrações.
- [ ] C) Testar apenas cada tela isoladamente.
- [ ] D) Conferir somente se os arquivos existem.
- [ ] E) Executar apenas com o conjunto usado no desenvolvimento.

4. Como avaliar o valor de uma solução de **Teste, apresentação e retrospectiva** após a entrega?

- [ ] A) Medir apenas a quantidade de linhas de código.
- [ ] B) Usar somente o número de tecnologias integradas.
- [ ] C) Considerar publicação equivalente a sucesso.
- [ ] D) Avaliar apenas comentários da equipe que desenvolveu.
- [ ] E) Acompanhar uso, qualidade técnica e efeito sobre a decisão ou processo que motivou o produto.

5. Ordene a construção de um produto de **Teste, apresentação e retrospectiva**.

- A) Publicar, observar o uso e iterar com evidências.
- B) Construir primeiro um fluxo mínimo de ponta a ponta.
- C) Desenhar dados, componentes e contratos entre eles.
- D) Testar qualidade, integração, segurança e falhas.
- E) Definir usuário, problema, decisão e medida de sucesso.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene a preparação da entrega de **Teste, apresentação e retrospectiva**.

- A) Coletar feedback e priorizar correções ou melhorias.
- B) Revisar documentação, configuração e instruções de execução.
- C) Executar testes automatizados e manuais do fluxo completo.
- D) Apresentar a solução com limitações e decisões técnicas.
- E) Congelar o escopo e registrar critérios de conclusão.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

> [!project] Projeto semanal — MVP Data + AI orientado à decisão
> **Desafio:** Construir um produto pequeno que combine análise ou modelo com IA somente onde ela gerar valor verificável.
>
> **Deve reutilizar:** Todo o conteúdo técnico acumulado.
>
> **Entregáveis obrigatórios:**
> - [ ] problema e métricas;
> - [ ] base e baseline;
> - [ ] componente analítico;
> - [ ] componente de IA opcional justificado;
> - [ ] teste com usuário;
> - [ ] retrospectiva;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> O MVP resolve uma decisão concreta, funciona de ponta a ponta e possui evidência de que a IA não foi adicionada apenas por aparência?

---


# Tema definido para o TCC final

## Portfolio Intelligence Lab — Plataforma de Análise, Ranking Quantitativo e Construção de Carteiras

> [!goal] Objetivo do TCC
> Construir uma plataforma reproduzível que analise **ações, ETFs e FIIs**, gere rankings quantitativos dentro de cada classe, monte carteiras a partir desses rankings e avalie se as estratégias entregam uma relação risco-retorno superior a baselines simples fora da amostra.

> [!warning] Limite do projeto
> O projeto não promete prever a bolsa nem recomenda compra ou venda. O resultado é uma pesquisa educacional sobre métodos quantitativos, sujeita a perdas, ruído, mudanças de regime e limitações dos dados.

### Pergunta central

**Como combinar fatores quantitativos, Machine Learning e técnicas de alocação para ranquear ações, ETFs e FIIs e construir carteiras com melhor equilíbrio entre retorno, risco, diversificação, liquidez e drawdown, usando somente informações disponíveis na data de cada decisão?**

### Decisões de escopo já definidas

- O universo obrigatório contém **ações brasileiras, ETFs negociados no Brasil e FIIs**.
- O ranking será feito **separadamente por classe**, porque ações, ETFs e FIIs possuem fundamentos e estruturas diferentes.
- A comparação entre classes acontecerá na etapa de alocação da carteira, não por um único ranking bruto que misture indicadores incompatíveis.
- O projeto deve trabalhar com uma janela histórica definida no pré-projeto e documentar ativos removidos, dados ausentes e mudanças no universo.
- O split deve ser temporal; divisão aleatória é proibida para o resultado principal.
- Custos de transação, rebalanceamento e liquidez devem aparecer no backtest.

### Módulo 1 — Dados e inteligência de mercado

- pipeline para coletar ou importar preços ajustados, volume/liquidez, proventos e indicadores disponíveis;
- armazenamento em camadas `raw`, `clean` e `analytics`;
- dicionário de dados, versionamento e testes de qualidade;
- cálculo de retornos, volatilidade, correlação, beta, Sharpe, Sortino e máximo drawdown;
- painel de comparação por ativo, classe e período;
- documentação de vieses como survivorship bias, look-ahead bias e data leakage.

### Módulo 2 — Motor Quantitativo de Ranking

**Fatores comuns mínimos:**

- momentum em diferentes janelas;
- volatilidade;
- drawdown;
- liquidez;
- consistência dos retornos;
- correlação com o restante do universo.

**Fatores específicos opcionais, conforme disponibilidade dos dados:**

- ações: qualidade, valor e crescimento;
- FIIs: distribuição, vacância, concentração e preço/valor patrimonial;
- ETFs: liquidez, concentração, aderência ao índice e custos conhecidos.

**Modelos e comparação:**

- score quantitativo simples como baseline;
- regressão logística ou regressão para prever faixa de desempenho futuro;
- árvore, Random Forest ou boosting;
- explicabilidade das variáveis;
- ranking por classe e classificação em faixas A–E;
- avaliação por Precision@K, retorno dos Top-K, estabilidade do ranking e turnover.

### Módulo 3 — Construção e avaliação de carteiras

Comparar pelo menos estas estratégias:

1. carteira de pesos iguais;
2. carteira formada pelos ativos mais bem ranqueados;
3. carteira de mínima volatilidade ou risk parity;
4. benchmark de mercado escolhido e documentado.

O backtest deve incluir:

- validação walk-forward;
- rebalanceamento com frequência definida;
- custos e regras de liquidez;
- retorno acumulado e anualizado;
- volatilidade, Sharpe, Sortino e máximo drawdown;
- análise por diferentes regimes/períodos;
- comparação dentro e fora da amostra;
- teste de sensibilidade a parâmetros.

### Produto demonstrável

- dashboard para explorar ativos, fatores, ranking e carteiras;
- simulador que permite escolher classe, perfil de risco, número de ativos e frequência de rebalanceamento;
- API para consultar ranking e métricas de uma carteira;
- relatório técnico e resumo executivo;
- testes, Docker e instruções de reprodução;
- módulo opcional de IA para explicar métricas e limitações, sem emitir recomendação de investimento.

### Critérios de sucesso

- superar pelo menos um baseline simples em parte relevante do período fora da amostra, sem esconder períodos ruins;
- provar que cada feature estava disponível antes da data prevista;
- demonstrar resultados líquidos de custos;
- apresentar estabilidade ou explicar claramente quando o ranking falha;
- comparar risco e retorno, sem usar apenas rentabilidade acumulada;
- permitir que outra pessoa reproduza a coleta, o ranking e o backtest;
- comunicar limitações, vieses e ausência de garantia de retorno.

### Riscos que precisam ser tratados

- **Look-ahead bias:** usar informação que só ficou disponível após a data da decisão;
- **Survivorship bias:** analisar apenas ativos que sobreviveram até hoje;
- **Overfitting:** ajustar fatores e modelos demais ao passado;
- **Data snooping:** testar muitas estratégias e mostrar apenas a vencedora;
- **Custos e liquidez:** simular negociações impossíveis ou gratuitas;
- **Mistura de classes:** comparar indicadores incompatíveis entre ações, ETFs e FIIs;
- **Mudança de regime:** assumir que relações históricas continuarão iguais.

### Escopo mínimo e extensões

**Escopo mínimo obrigatório:** dados, fatores, ranking separado por classe, três estratégias de carteira, walk-forward, custos, dashboard e relatório.

**Extensões cortáveis:** IA explicativa, fatores fundamentalistas adicionais, otimização avançada, mais classes de ativos e atualização em tempo real.

> [!success] Por que este TCC é forte para o portfólio
> Ele integra Python, SQL, estatística, séries temporais, Machine Learning, explicabilidade, backtesting, engenharia de dados, API, Docker, visualização, decisão de negócio e comunicação de riscos.

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Teste, apresentação e retrospectiva.
- **Competência sugerida:** Testes e apresentação de produtos de dados.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Testes e apresentação de produtos de dados** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa`.
- **Próximo marco do perfil:** Dia 130 — revisão final do título, Sobre, Competências, Projetos e Destaques.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação
