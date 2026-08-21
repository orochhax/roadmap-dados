# Projeto — Auditoria do pipeline

## Manifesto de entradas

- **Obrigatórias:** notebook executável, dados permitidos, pipeline, métricas, seeds e versões.
- **Saídas:** `auditoria_modelo.md`, `train.py`, `evaluate.py` e `features.py`.
- **Fallback local:** use a amostra versionada e um kernel/ambiente novo; nenhuma conexão externa é necessária.

## Núcleo essencial

1. [ ] Audite alvo, split, leakage, pipeline, métricas, tuning, calibração, segmentos e reprodução.
2. [ ] Execute do zero e corrija dependência de ordem, caminho fixo e estado oculto.
3. [ ] Registre problema, severidade, correção e evidência em `auditoria_modelo.md`.

## Prática obrigatória

- [ ] Rode linter e elimine duplicação relevante.

## Concluído quando

- [ ] A execução limpa termina sem etapa manual não documentada.
- [ ] Cada achado possui severidade e evidência da correção.
- [ ] Os scripts reproduzem a métrica publicada.
