# Enunciado — núcleo tipado de incidentes de telecom

## Cenário real

O NOC recebe incidentes de várias cidades. O script atual mistura leitura, validação, regras de prioridade e geração do relatório. Uma alteração em uma regra quebra outras partes. Você deverá criar um núcleo modular que possa ser reutilizado por uma API ou pipeline sem depender de `input()`.

## Entradas

- arquivo compartilhado `dados/incidentes.csv`;
- colunas mínimas: `id`, `cidade`, `severidade`, `duracao_min`, `clientes_afetados` e `resolvido`;
- uma fixture pequena criada no próprio arquivo inicial para os testes controlados.

## Saídas

- `resumo_incidentes.json` ao lado do arquivo de exercício;
- lista separada de registros rejeitados com `linha`, `campo` e `motivo`;
- resultado dos testes no [registro de evidências](../03-evidencias/README.md).

## Regras obrigatórias

1. Modele um incidente com `@dataclass`; justifique se usará `frozen=True` e/ou `slots=True`.
2. Separe conversão/validação, regra de impacto, agregação por cidade e gravação em componentes diferentes.
3. Use composição. Não crie hierarquia de classes apenas para demonstrar herança.
4. Declare tipos das funções públicas e evite `Any` sem justificativa.
5. Rejeite id vazio ou repetido, cidade vazia, duração negativa, severidade fora de `P1`–`P4` e valor de `resolvido` não reconhecido.
6. Calcule por cidade: quantidade válida, duração média, clientes afetados e percentual resolvido.
7. Ordene o relatório por clientes afetados decrescente e depois por cidade.
8. Escreva JSON UTF-8 de forma determinística; duas execuções iguais não podem duplicar dados.

## Casos de borda obrigatórios

- entrada vazia;
- dois incidentes com o mesmo id;
- duração igual a zero;
- cidade com acento;
- valor textual inválido para `resolvido`;
- cidade com somente registros rejeitados.

## Métricas e conferências

- `taxa_validos = registros_validos / registros_lidos`;
- quantidade de rejeições por motivo;
- igualdade entre o total por cidade e o total de registros válidos;
- igualdade entre a saída procedural mínima e a modular para a fixture válida;
- resultado de `python -m compileall` e, se instalado, `mypy --strict`.

## Critério de aceite

- [ ] O fluxo roda do CSV ao JSON sem `input()` nem caminho absoluto.
- [ ] Todas as regras e os seis casos de borda têm teste ou conferência registrada.
- [ ] Nenhum registro inválido participa das métricas.
- [ ] A reconciliação de totais fecha exatamente.
- [ ] Você explica por que cada componente existe e cita uma situação em que uma simples função seria melhor que uma classe.

Implemente em [python_profissional.py](python_profissional.py). Não procure uma solução completa; pesquise apenas o conceito que estiver impedindo o próximo passo.

