# Critérios de aceitação

- O notebook executa do início ao fim em kernel limpo.
- Alvo, split e variáveis foram revisados contra leakage.
- Métricas, calibração e segmentos foram inspecionados.
- `train.py`, `evaluate.py` e `features.py` contêm as partes estáveis.
- Duplicação, variáveis globais e caminhos fixos foram revisados.
- Cada problema tem severidade, correção, evidência e status.
- Duas execuções com seed 42 produzem resultados compatíveis.
