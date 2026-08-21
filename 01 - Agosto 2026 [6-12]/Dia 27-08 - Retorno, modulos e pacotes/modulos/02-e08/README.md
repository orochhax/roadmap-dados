# Módulos e pacotes

## Objetivo

Separar responsabilidades e importar funções sem copiar sua implementação.

## Conteúdo gratuito

- [Python 3 — Mundo 3](https://www.cursoemvideo.com/curso/python-3-mundo-3/): Aula #22 — Módulos e Pacotes; exercícios #107 — Exercitando módulos em Python e #111 — Transformando módulos em pacotes.

Em cada exercício, leia o enunciado, pause e tente resolver antes de assistir à resolução.

## Aprenda agora

- Use `if __name__ == "__main__":` para definir o ponto de entrada executável.
- `__init__.py` identifica o pacote; `__pycache__` é gerado pelo Python e não contém código-fonte.

## Prática

1. Resolva os exercícios #107 e #111 em arquivos próprios.
2. Complete `01-exercicios/main.py` e `01-exercicios/noc_utils/metricas.py`.
3. Execute `python main.py` dentro de `01-exercicios`.

## Resultado esperado

O programa importa a função do pacote, informa `82.0%` para `(100, 82)` e trata `(0, 0)` sem divisão por zero.

## Concluído quando

- [ ] Os dois exercícios foram tentados antes das resoluções.
- [ ] `main.py` executa sem copiar a fórmula do módulo.
- [ ] Você explica a função de `__init__.py` e do bloco principal.
