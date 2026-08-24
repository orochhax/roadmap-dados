# Funcoes com retorno + Modulos e pacotes

**Data de estudo:** 27/08/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Funcoes com retorno

#### O que pesquisar
- `Funcoes com retorno Python explicado passo a passo`
- `Funcoes com retorno Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-funcoes-com-retorno`](<atividades/01-funcoes-com-retorno/>)

#### Objetivo

Validar entradas, retornar valores e construir dicionários dentro de funções.

#### Conteúdo gratuito

- [Python 3 — Mundo 3](https://www.cursoemvideo.com/curso/python-3-mundo-3/): Aula #21 — Funções, parte 2; exercícios #104 — Validando entrada de dados em Python e #105 — Analisando e gerando Dicionários.

Em cada exercício, leia o enunciado, pause e tente resolver antes de assistir à resolução.

#### O que você precisa entender

- `print` apresenta um valor; `return` entrega o valor para outra parte do programa.
- Separe leitura de entrada, validação e construção do resultado em funções pequenas.

#### O que fazer

- [ ] Resolva os exercícios #104 e #105 em arquivos próprios.
- [ ] Complete `atividades/01-funcoes-com-retorno/funcoes_com_retorno.py`.
- [ ] Teste entradas inválidas antes de criar o dicionário final.

#### Como validar

Somente um inteiro não negativo é aceito, e o retorno final é um dicionário com cidade, prioridade e duração.

- Os dois exercícios foram tentados antes das resoluções.
- Uma entrada inválida solicita nova tentativa sem encerrar o programa.
- O dicionário retornado contém os campos e tipos esperados.

#### Arquivos vazios dos desafios do Curso em Vídeo

Cole o enunciado em cada arquivo e escreva sua própria tentativa antes de assistir à resolução:

- [#104 — `DESAFIO104.py`](<atividades/01-funcoes-com-retorno/DESAFIO104.py>)
- [#105 — `DESAFIO105.py`](<atividades/01-funcoes-com-retorno/DESAFIO105.py>)

### Atividade 2 — Modulos e pacotes

#### O que pesquisar
- `Modulos e pacotes Python explicado passo a passo`
- `Modulos e pacotes Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-modulos-e-pacotes`](<atividades/02-modulos-e-pacotes/>)

#### Objetivo

Separar responsabilidades e importar funções sem copiar sua implementação.

#### Conteúdo gratuito

- [Python 3 — Mundo 3](https://www.cursoemvideo.com/curso/python-3-mundo-3/): Aula #22 — Módulos e Pacotes; exercícios #107 — Exercitando módulos em Python e #111 — Transformando módulos em pacotes.

Em cada exercício, leia o enunciado, pause e tente resolver antes de assistir à resolução.

#### O que você precisa entender

- Use `if __name__ == "__main__":` para definir o ponto de entrada executável.
- `__init__.py` identifica o pacote; `__pycache__` é gerado pelo Python e não contém código-fonte.

#### O que fazer

- [ ] Resolva os exercícios #107 e #111 em arquivos próprios.
- [ ] Complete `atividades/02-modulos-e-pacotes/main.py` e `atividades/02-modulos-e-pacotes/noc_utils/metricas.py`.
- [ ] Execute `python main.py` dentro de `atividades/02-modulos-e-pacotes`.

#### Como validar

O programa importa a função do pacote, informa `82.0%` para `(100, 82)` e trata `(0, 0)` sem divisão por zero.

- Os dois exercícios foram tentados antes das resoluções.
- `main.py` executa sem copiar a fórmula do módulo.
- Você explica a função de `__init__.py` e do bloco principal.

#### Arquivos vazios dos desafios do Curso em Vídeo

Cole o enunciado em cada arquivo e escreva sua própria tentativa antes de assistir à resolução:

- [#107 — `DESAFIO107.py`](<atividades/02-modulos-e-pacotes/DESAFIO107.py>)
- [#111 — `DESAFIO111.py`](<atividades/02-modulos-e-pacotes/DESAFIO111.py>)

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
