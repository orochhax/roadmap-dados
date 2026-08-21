# Auditoria do pipeline

## Conquista para o LinkedIn

- **Competências:** depois de executar e explicar a auditoria, adicione **Machine Learning**, **scikit-learn** e **Pipelines de ML**.
- **Projetos ou Destaques:** inclua a entrega somente se ela estiver revisada, reproduzível e apresentável.
- **Título e Sobre:** não altere por suposição. Siga o posicionamento preenchido em [Perguntas para Carlos](<../../00 - Recursos Compartilhados/PERGUNTAS-PARA-CARLOS.md>) e a regra do [Guia de LinkedIn e evidências](<../../00 - Recursos Compartilhados/linkedin-e-evidencias.md>).

## Preparação
- **Pasta/arquivo principal:** `projeto-mensal/src/train.py`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Aprenda agora

- **Definição:** auditoria verifica dados, leakage, calibração, reprodutibilidade e código; calibração confronta probabilidade prevista e frequência observada.
- **Exemplo mínimo:** no grupo previsto entre 0,7–0,8, compare média prevista e taxa real; execute `ruff check .` e registre versão, seed e comando.
- **Erro comum:** aprovar o pipeline só pela métrica agregada, sem reproduzir e inspecionar entradas.

## Núcleo essencial

1. [ ] Execute checklist de auditoria: definição do alvo, split, leakage, pipeline, métricas, tuning, calibração, segmentos e reprodutibilidade.
2. [ ] Rode notebook do zero em kernel limpo e corrija células fora de ordem.
3. [ ] Converta partes estáveis em scripts `train.py`, `evaluate.py` e `features.py`.
4. [ ] Use linter ou revisão manual para encontrar código duplicado, variáveis globais e caminhos fixos.

## Prática obrigatória

- [ ] Crie `auditoria_modelo.md` com problemas encontrados, severidade, correção e evidência.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `projeto-mensal/src/train.py`:** Acrescente à auditoria uma checagem que procure caminhos absolutos contendo C:\Users e classifique a severidade.
- [ ] **Em `projeto-mensal/src/train.py`:** Rode train.py duas vezes com seed 42 e compare as métricas salvas para verificar reprodutibilidade.

## Concluído quando

- [ ] O núcleo foi executado e `projeto-mensal/src/train.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.
