# Auditoria do pipeline

**Data de estudo:** 03/11/2026  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Auditoria do pipeline

#### O que pesquisar
- `Auditoria do pipeline engenharia de dados e MLOps explicado passo a passo`
- `Auditoria do pipeline engenharia de dados e MLOps exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-auditoria-do-pipeline`](<atividades/01-auditoria-do-pipeline/>)

#### Conquista para o LinkedIn

- **Competências:** depois de executar e explicar a auditoria, adicione **Machine Learning**, **scikit-learn** e **Pipelines de ML**.
- **Projetos ou Destaques:** inclua a entrega somente se ela estiver revisada, reproduzível e apresentável.
- **Título e Sobre:** não altere por suposição. Siga o posicionamento preenchido em [Perguntas para Carlos](<../../00 - Recursos Compartilhados/PERGUNTAS-PARA-CARLOS.md>) e a regra do [Guia de LinkedIn e evidências](<../../00 - Recursos Compartilhados/linkedin-e-evidencias.md>).

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-auditoria-do-pipeline/projeto-mensal/src/train.py`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** auditoria verifica dados, leakage, calibração, reprodutibilidade e código; calibração confronta probabilidade prevista e frequência observada.
- **Exemplo mínimo:** no grupo previsto entre 0,7–0,8, compare média prevista e taxa real; execute `ruff check .` e registre versão, seed e comando.
- **Erro comum:** aprovar o pipeline só pela métrica agregada, sem reproduzir e inspecionar entradas.

#### O que fazer

- [ ] Execute checklist de auditoria: definição do alvo, split, leakage, pipeline, métricas, tuning, calibração, segmentos e reprodutibilidade.
- [ ] Rode notebook do zero em kernel limpo e corrija células fora de ordem.
- [ ] Converta partes estáveis em scripts `train.py`, `evaluate.py` e `features.py`.
- [ ] Use linter ou revisão manual para encontrar código duplicado, variáveis globais e caminhos fixos.

- [ ] Crie `auditoria_modelo.md` com problemas encontrados, severidade, correção e evidência.


- [ ] **Em `atividades/01-auditoria-do-pipeline/projeto-mensal/src/train.py`:** Acrescente à auditoria uma checagem que procure caminhos absolutos contendo C:\Users e classifique a severidade.
- [ ] **Em `atividades/01-auditoria-do-pipeline/projeto-mensal/src/train.py`:** Rode train.py duas vezes com seed 42 e compare as métricas salvas para verificar reprodutibilidade.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
