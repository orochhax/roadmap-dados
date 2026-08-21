# Exceções e menu

## Objetivo

Tratar erros de entrada esperados e construir um menu funcional em um projeto organizado.

## Conteúdo gratuito

- [Python 3 — Mundo 3](https://www.cursoemvideo.com/curso/python-3-mundo-3/): Aula #23 — Tratamento de Erros e Exceções; exercícios #113 — Funções aprofundadas em Python e #115a — Criando um menu.

Em cada exercício, leia o enunciado, pause e tente resolver antes de assistir à resolução.

## Aprenda agora

- Coloque no `try` somente a conversão que pode falhar e capture a exceção específica.
- Evite `except:` genérico; apresente uma mensagem que permita corrigir a entrada.

## Prática

1. Resolva os exercícios #113 e #115a em arquivos próprios.
2. Complete `01-exercicios/entrada_segura.py`.
3. Complete o checkpoint local:

```text
01-exercicios/projeto_cadastro/
├── main.py
└── interface.py
```

4. Teste o menu com uma opção inválida e com a opção de saída.

## Resultado esperado

Texto vazio, texto não numérico e número negativo não encerram o programa; o menu permanece ativo e encerra pela opção definida.

## Concluído quando

- [ ] Os exercícios #113 e #115a foram tentados antes das resoluções.
- [ ] A leitura segura aceita somente inteiro não negativo.
- [ ] O menu local abre, recusa opção inválida e encerra corretamente.
