# Databricks aplicado

**Data de estudo:** 17/12/2026  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Databricks aplicado

#### O que pesquisar
- `Databricks aplicado Python explicado passo a passo`
- `Databricks aplicado Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-databricks-aplicado`](<atividades/01-databricks-aplicado/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-databricks-aplicado/dia-103-databricks-aplicado.py`.
- **Entradas:** `dados/clientes_telecom.csv`, schema de features e experimento MLflow.
- **Ambiente obrigatório:** Databricks Free ou PySpark local, com um servidor ou banco local real do MLflow.
- **Recuperação de ambiente:** se a instalação local falhar, repita a atividade no Google Colab ou Databricks Free e registre o ambiente utilizado. CSV manual não substitui as runs reais.

#### O que você precisa entender

- **Definição:** feature table registra features e chaves; MLflow rastreia parâmetros, métricas e artefatos; run é uma execução identificável.
- **Exemplo mínimo:** configure um experimento, execute duas runs nomeadas alterando apenas um hiperparâmetro e consulte os resultados pela API do MLflow.
- **Erro comum:** registrar métrica sem versão dos dados, código e modelo.

#### O que fazer

- [ ] Execute ingestão, limpeza, SQL, criação das features e treino no Databricks Free ou com PySpark local.
- [ ] Configure um experimento real do MLflow e execute duas runs nomeadas, alterando exatamente um hiperparâmetro entre elas.
- [ ] Em cada run, registre identificador dos dados, biblioteca e versão, seed, parâmetros, métrica principal, tempo de treino, tempo de inferência, artefato de avaliação e modelo.
- [ ] Consulte as duas runs pela API do MLflow, carregue o modelo da melhor run e faça uma previsão de verificação.
- [ ] Exporte a comparação para `runs_mlflow.csv` e registre os dois run IDs.

- [ ] **Em `atividades/01-databricks-aplicado/dia-103-databricks-aplicado.py`:** reconstrua uma run a partir dos parâmetros registrados e compare a métrica reproduzida com a original.
- [ ] Remova uma coluna obrigatória do DataFrame Spark e faça a validação parar antes da feature table.

#### Atualização do LinkedIn — após concluir

- **Evidência exigida:** dois run IDs reais, comparação exportada e previsão feita com o modelo recarregado.
- **Competências:** adicione **MLflow**. Adicione **Databricks** somente se a plataforma tiver sido realmente usada; PySpark local não comprova Databricks.
- **Sobre e headline:** não altere ainda; a revisão ocorrerá após retreinamento e rollback.

#### Como validar

- Existem dois run IDs reais do MLflow e o modelo da melhor run foi recarregado para uma previsão.
- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
