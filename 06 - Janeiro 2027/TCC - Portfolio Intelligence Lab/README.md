# TCC — Portfolio Intelligence Lab

> Estrutura preparada somente com o escopo e os enunciados. Nenhuma parte do TCC foi implementada.

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

> [!important] Projeto final estilo TCC — Portfolio Intelligence Lab
> **Desafio:** Entregar e defender uma plataforma de análise, ranking quantitativo e carteiras com ações, ETFs e FIIs, validada temporalmente e líquida de custos.
>
> **Entregáveis obrigatórios:**
> - [ ] pipeline de dados versionado;
> - [ ] fatores e ranking separado por classe;
> - [ ] modelos e baselines comparáveis;
> - [ ] backtest walk-forward com custos;
> - [ ] três estratégias de carteira e benchmark;
> - [ ] dashboard, API, testes e Docker;
> - [ ] relatório técnico, resumo executivo e defesa;
> - [ ] post de LinkedIn e demonstração;
>
> **Nota mínima recomendada:** `7/10`. Abaixo disso, corrija os pontos críticos sem adiar o início das candidaturas.

> [!check] Critério de conclusão do roadmap
> Outra pessoa consegue reproduzir os dados, ranking e backtest; os resultados resistem a perguntas sobre vieses e custos; e o projeto demonstra competência para uma vaga júnior sem prometer retorno financeiro?

---
