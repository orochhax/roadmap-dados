<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 120 — Teste, apresentação e retrospectiva — 15/01/2027

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Teste, apresentação e retrospectiva.
- **Competência sugerida:** Testes e apresentação de produtos de dados.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Testes e apresentação de produtos de dados** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa`.
- **Próximo marco do perfil:** Dia 130 — revisão final do título, Sobre, Competências, Projetos e Destaques.

> [!abstract] Resultado concreto do dia
> Concluir **Teste, apresentação e retrospectiva** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 4–5 horas; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Teste, apresentação e retrospectiva.
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** Projetos e dados acumulados durante o roadmap.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Execute testes funcionais, de dados e de decisão sobre o fluxo essencial.
2. [ ] Corrija os problemas críticos e gere uma versão estável.
3. [ ] Apresente o produto em até cinco minutos com problema, decisão, evidência e limitação.
4. [ ] Escreva retrospectiva curta com três aprendizados úteis para o TCC.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Revisão externa e cinco feedbacks são recomendados, mas dependem da disponibilidade de outra pessoa.
- [ ] Uma segunda apresentação para público diferente é desafio de comunicação.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Peça a revisão externa para executar o caso com entrada ausente e registre o feedback sobre clareza da mensagem.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Apresente em uma frase a limitação mais grave e confirme que ela aparece na fala técnica e executiva.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** O que reduz falhas entre componentes em **Teste, apresentação e retrospectiva**?

- [ ] A) Alterar formatos sem avisar os consumidores.
- [ ] B) Depender de passos manuais não documentados.
- [ ] C) Compartilhar estado interno sem uma interface definida.
- [ ] D) Contratos explícitos para dados, esquemas, entradas, saídas, versões e tratamento de erros.
- [ ] E) Cada componente interpretar os campos de uma forma.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual teste oferece mais confiança em uma entrega de **Teste, apresentação e retrospectiva**?

- [ ] A) Ignorar erros externos quando o código local funciona.
- [ ] B) Executar o fluxo completo com casos representativos e simular falhas nas principais integrações.
- [ ] C) Testar apenas cada tela isoladamente.
- [ ] D) Conferir somente se os arquivos existem.
- [ ] E) Executar apenas com o conjunto usado no desenvolvimento.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene a construção de um produto de **Teste, apresentação e retrospectiva**.

- A) Publicar, observar o uso e iterar com evidências.
- B) Construir primeiro um fluxo mínimo de ponta a ponta.
- C) Desenhar dados, componentes e contratos entre eles.
- D) Testar qualidade, integração, segurança e falhas.
- E) Definir usuário, problema, decisão e medida de sucesso.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`



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
