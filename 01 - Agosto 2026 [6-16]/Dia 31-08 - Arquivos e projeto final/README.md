# Arquivos e projeto final

## Objetivo

Persistir cadastros em arquivo e concluir um programa modular executável.

## Conteúdo gratuito

- [Python 3 — Mundo 3](https://www.cursoemvideo.com/curso/python-3-mundo-3/): exercícios #115b — Arquivos com Python e #115c — Finalizando o projeto.

Em cada exercício, leia o enunciado, pause e tente resolver antes de assistir à resolução.

## Aprenda agora

- Use `Path(__file__).resolve().parent` para localizar o arquivo de dados sem depender do terminal.
- Abra texto com `encoding="utf-8"` para preservar nomes acentuados.
- Teste persistência encerrando e executando o programa novamente.

## Prática

1. Resolva os exercícios #115b e #115c em arquivos próprios.
2. Complete o checkpoint autossuficiente:

```text
01-exercicios/projeto_cadastro/
├── main.py
├── interface.py
└── arquivo.py
```

3. Execute o roteiro em `03-evidencias/teste_aceitacao.md`.

## Resultado esperado

O sistema cria seu arquivo de dados, cadastra duas pessoas, recusa entradas inválidas e exibe os mesmos registros em uma segunda execução.

## Concluído quando

- [ ] Os exercícios #115b e #115c foram tentados antes das resoluções.
- [ ] O teste de aceitação prova persistência e tratamento de entrada inválida.
- [ ] Você executa o sistema inteiro e explica a responsabilidade de cada módulo.
