# Orquestração conceitual

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-088-orquestracao-conceitual.py`.
- **Entradas:** manifesto local com extrair, validar, transformar, publicar e auditar. **Fallback local:** estados simulados em Python.

## Aprenda agora

- **Definição:** DAG representa dependências; retry repete falha transitória, timeout limita duração, backfill processa janela ausente e runbook orienta resposta.
- **Exemplo mínimo:** `extrair → validar → transformar → publicar → auditar`; cada tarefa define entrada, saída, tentativas e estado.
- **Erro comum:** repetir erro determinístico indefinidamente ou iniciar tarefa sem validar a saída anterior.

## Núcleo essencial

1. [ ] Modele o pipeline como tarefas com dependências: extrair → validar → transformar → carregar → testar.
2. [ ] Crie um DAG conceitual em Mermaid ou use Prefect/Airflow local se desejar.
3. [ ] Defina política de retry, timeout, alerta e backfill.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-088-orquestracao-conceitual.py`:** Simule falha na transformação e confirme que carregar e testar ficam bloqueadas.
- [ ] **No mesmo arquivo:** defina retry máximo 3, timeout de 10 minutos e alerta após a última falha; escreva um runbook com diagnóstico e recuperação.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-088-orquestracao-conceitual.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.
