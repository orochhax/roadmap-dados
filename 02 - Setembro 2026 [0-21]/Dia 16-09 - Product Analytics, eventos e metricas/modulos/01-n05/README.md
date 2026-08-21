# Product Analytics I — instrumentação confiável

## Objetivo

Desenhar e validar a instrumentação do aplicativo de autoatendimento de uma operadora. Antes de calcular funis, você deverá provar que os eventos têm significado, schema, identidade e privacidade controlados.

## Pesquise exatamente estes nomes

- `product analytics tracking plan event taxonomy`
- `event naming convention analytics`
- `user id anonymous id identity resolution analytics`
- `North Star metric input metrics guardrail metrics`
- `data contract schema evolution events`
- `event deduplication idempotency`
- `LGPD data minimization analytics events`

## Trabalho obrigatório

Leia o [enunciado](01-exercicios/ENUNCIADO.md), complete [validar_tracking_plan.py](01-exercicios/validar_tracking_plan.py) e registre o contrato e os testes em [Evidências](03-evidencias/README.md).

## Concluído quando

- o tracking plan descreve evento, gatilho, propriedades, dono e versão;
- o validador separa eventos aceitos e rejeitados com motivo;
- duplicidade, ordem, identidade e PII são testadas;
- a North Star e suas guardrails são ligadas a uma decisão real.

