# Python profissional para um pipeline de incidentes

## Objetivo

Transformar um script procedural de operações de telecom em componentes pequenos, tipados e testáveis. O foco não é “usar classes por usar”, mas separar representação do dado, validação, cálculo e serialização.

## Pesquise exatamente estes nomes

- `Python dataclasses frozen slots`
- `Python type hints collections Sequence Mapping`
- `Python Protocol structural subtyping`
- `composition over inheritance Python`
- `mypy strict mode`
- `pytest parametrization`
- `pathlib Path read_text write_text`

## Trabalho obrigatório

Leia o [enunciado](01-exercicios/ENUNCIADO.md), complete [python_profissional.py](01-exercicios/python_profissional.py) e registre a execução em [Evidências](03-evidencias/README.md).

Você deverá construir um pequeno núcleo do produto **Telecom Customer Intelligence**, comparar a versão procedural com a versão modular e provar que entradas inválidas não contaminam o resumo operacional.

## Concluído quando

- o arquivo executa com type hints e sem caminhos absolutos;
- os contratos e responsabilidades das classes podem ser explicados;
- os casos normal, inválido e duplicado foram testados;
- a saída foi reconciliada com um cálculo manual;
- a evidência registra uma limitação da modelagem escolhida.

