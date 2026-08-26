# Simulado autoral — Databricks Fundamentals Accreditation

Este material prepara para a acreditação introdutória gratuita da Databricks Academy. Não copia o quiz oficial e não é uma certificação profissional supervisionada.

## Estrutura

- **Parte A:** 20 questões conceituais em formato de cenário, próximas ao tipo de decisão cobrado em um quiz introdutório;
- **Parte B:** conferência do artefato Spark/Databricks já executado no roadmap.

Não existe um segundo laboratório neste simulado. O código obrigatório do dia 03/12 comprova a aplicação prática.

## Regras

- Tempo: 30 minutos para as 20 questões.
- Faça a primeira tentativa sem consulta.
- Responda em `respostas-databricks-fundamentals.md` com a alternativa escolhida e uma justificativa de uma frase.
- Não há respostas nem gabarito neste repositório. Envie a tentativa e o artefato existente para correção.

## Parte A — 20 questões conceituais

### 1. Escolha de arquitetura

Uma equipe precisa unir arquivos brutos, consultas SQL e modelos de Machine Learning sem manter cópias desconectadas dos mesmos dados. Qual proposta melhor representa o objetivo de um lakehouse?

- A. Guardar apenas tabelas relacionais para BI.
- B. Combinar flexibilidade de data lake com confiabilidade e governança de tabelas.
- C. Substituir armazenamento por memória de cluster.
- D. Manter um banco separado e isolado para cada workload.

### 2. Data Intelligence Platform

Além de armazenar e processar dados, qual necessidade uma Data Intelligence Platform procura atender?

- A. Remover toda intervenção humana de qualquer decisão.
- B. Integrar dados, governança, análise e IA com contexto compartilhado.
- C. Converter automaticamente todo arquivo em modelo de ML.
- D. Executar somente notebooks Python.

### 3. Armazenamento e computação

Qual é uma consequência útil de separar armazenamento e computação?

- A. Cada dado precisa ser copiado para todo cluster.
- B. O armazenamento deixa de precisar de controle de acesso.
- C. Workloads podem dimensionar computação sem mover toda a base.
- D. Consultas deixam de ter custo.

### 4. Workspace, notebook e compute

Um notebook foi salvo, mas nenhuma célula consegue executar. Qual componente deve ser verificado primeiro?

- A. A existência de compute associado e disponível.
- B. A quantidade de dashboards publicados.
- C. O nome do workspace no navegador.
- D. A extensão do arquivo de origem.

### 5. SQL warehouse

Para qual carga um SQL warehouse tende a ser a escolha mais direta?

- A. Consultas de BI e dashboards usando SQL.
- B. Armazenamento definitivo de arquivos sem consultas.
- C. Edição manual de imagens.
- D. Treinamento local que não usa dados da plataforma.

### 6. Papel do Spark

Qual descrição representa melhor o papel do Apache Spark?

- A. Sistema de versionamento de código.
- B. Motor distribuído para processamento de dados.
- C. Formato de arquivo de apresentação.
- D. Serviço exclusivo de controle de acesso.

### 7. Avaliação lazy

Uma transformação de DataFrame foi declarada, mas o erro aparece somente ao contar ou gravar os dados. Qual conceito explica esse comportamento?

- A. Replicação síncrona.
- B. Avaliação preguiçosa das transformações até uma ação.
- C. Exclusão automática do schema.
- D. Criptografia do notebook.

### 8. Tabelas Delta

Que capacidade diferencia uma tabela Delta de um diretório de arquivos sem camada transacional?

- A. Garantias de transação e metadados para operações confiáveis.
- B. Ausência de schema.
- C. Execução sem armazenamento.
- D. Impossibilidade de atualizar dados.

### 9. Histórico de tabela

Por que o histórico de versões pode ajudar após uma carga incorreta?

- A. Porque elimina a necessidade de validar dados.
- B. Porque permite investigar versões e, quando aplicável, recuperar um estado anterior.
- C. Porque impede qualquer alteração na tabela.
- D. Porque transforma batch em streaming.

### 10. Batch e streaming

Qual combinação está correta?

- A. Batch processa conjuntos delimitados; streaming trata eventos contínuos com baixa latência quando necessário.
- B. Batch é sempre mais caro e streaming é sempre gratuito.
- C. Streaming serve apenas para dashboards e batch apenas para ML.
- D. Os dois termos descrevem tipos de permissão.

### 11. Workloads

Qual conjunto representa workloads diferentes suportados em uma plataforma de dados?

- A. Engenharia de dados, BI/SQL, Machine Learning e aplicações de IA.
- B. Apenas armazenamento e compactação de imagens.
- C. Somente planilhas e apresentações.
- D. Exclusivamente treinamento de redes neurais.

### 12. Catálogo central

Qual é o objetivo principal de um catálogo central de dados e permissões?

- A. Esconder tabelas dos consumidores autorizados.
- B. Organizar descoberta, propriedade, acesso e governança dos ativos.
- C. Substituir todos os testes de qualidade.
- D. Manter senhas dentro de notebooks.

### 13. Lineage

Um indicador incorreto aparece em um dashboard. Como lineage ajuda na investigação?

- A. Mostra dependências entre fontes, transformações e consumidores.
- B. Corrige automaticamente qualquer regra de negócio.
- C. Reduz o número de linhas da tabela.
- D. Escolhe o tamanho do cluster.

### 14. Planos da plataforma

Qual afirmação descreve melhor a separação entre plano de controle e plano de dados?

- A. Um organiza serviços e configurações; o outro envolve processamento e acesso aos dados conforme a arquitetura.
- B. Os dois são nomes diferentes para a mesma tabela.
- C. O plano de dados contém apenas telas da interface.
- D. O plano de controle substitui IAM.

### 15. Menor privilégio

Uma pessoa precisa apenas consultar uma tabela aprovada. Qual política é mais adequada?

- A. Dar acesso administrativo ao workspace inteiro.
- B. Conceder somente leitura no menor escopo necessário.
- C. Compartilhar a credencial de um administrador.
- D. Tornar a tabela pública para evitar solicitações.

### 16. Reprodutibilidade de notebooks

Qual prática reduz o risco de um notebook funcionar apenas para seu autor?

- A. Depender da ordem manual e não documentada das células.
- B. Versionar código, declarar dependências e testar execução do início ao fim.
- C. Salvar resultados sem o código que os produziu.
- D. Copiar dados para células de texto.

### 17. Cache

Quando cache pode produzir uma interpretação errada?

- A. Quando o resultado armazenado ficou desatualizado após mudança na fonte.
- B. Quando a consulta nunca reutiliza dados.
- C. Quando o usuário documenta a atualização.
- D. Quando não existe compute.

### 18. Falha durante gravação

Um job falhou no meio da escrita. Qual investigação é mais importante antes de executar novamente?

- A. Integridade da tabela, garantias transacionais e idempotência do pipeline.
- B. Cor do tema do notebook.
- C. Quantidade de usuários no LinkedIn.
- D. Nome da variável usada no relatório.

### 19. Custo de compute

Qual ação representa controle responsável de custo?

- A. Manter compute ligado para evitar qualquer espera.
- B. Usar dimensionamento adequado, término automático e medir o workload.
- C. Escolher sempre o menor compute, independentemente do tempo total.
- D. Executar `collect()` em toda base para facilitar inspeção.

### 20. Nome da conquista

Após concluir a avaliação gratuita, qual afirmação é correta?

- A. A pessoa conquistou automaticamente uma certificação profissional supervisionada.
- B. A pessoa pode publicar `Databricks Fundamentals Accreditation` com o nome emitido, sem chamá-la de certificação profissional.
- C. A pessoa pode declarar experiência profissional em produção.
- D. A pessoa não precisa explicar a diferença entre curso, acreditação e certificação.

## Parte B — comprovação aplicada existente

Use o arquivo já produzido em [Databricks e Spark introdutório — dia 03/12](<../../07 - Fevereiro 2027 [0-12]/Dia 02-02 - Spark e Databricks/atividades/01-databricks-e-spark-introdutorio/dia-089-databricks-e-spark-introdutorio.py>). Não crie um novo laboratório.

Apresente para correção a execução que já comprova:

- schema explícito e inspeção das colunas;
- seleção, filtro, agregação, `JOIN` e criação de coluna;
- reconciliação do mesmo resultado entre Spark e pandas;
- falha controlada quando `cliente_id` não existe;
- explicação de quando Spark seria excesso;
- ambiente ou compute utilizado e como ele foi encerrado.

Se o artefato ainda não executa do início ao fim, conclua o exercício do dia 03/12 antes de fazer a avaliação oficial.

## Rubrica de correção — sem respostas

| Critério | Pontos |
|---|---:|
| Lakehouse, Data Intelligence e arquitetura | 20 |
| Spark, compute, SQL warehouse e workloads | 20 |
| Delta Lake, confiabilidade, batch e streaming | 15 |
| Governança, segurança, catálogo e lineage | 15 |
| Artefato Spark executado, reconciliado e explicado | 30 |
| **Total** | **100** |

### Falhas críticas

- publicar credencial ou dado sensível;
- deixar compute pago ativo sem justificativa;
- apresentar resultado sem reconciliação;
- responder ao acaso sem conseguir justificar decisões;
- confundir Databricks Fundamentals Accreditation com certificação profissional.

Prontidão recomendada: 80 pontos ou mais, nenhuma falha crítica e artefato existente executado do início ao fim.
