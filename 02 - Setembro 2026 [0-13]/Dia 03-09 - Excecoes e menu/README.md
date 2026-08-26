# Excecoes e menu

**Data de estudo:** 03/09/2026
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Excecoes e menu

#### O que pesquisar
- `Excecoes e menu Python explicado passo a passo`
- `Excecoes e menu Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-excecoes-e-menu`](<atividades/01-excecoes-e-menu/>)

#### Objetivo

Tratar erros de entrada esperados e construir um menu funcional em um projeto organizado.

#### Conteúdo gratuito

- [Python 3 — Mundo 3](https://www.cursoemvideo.com/curso/python-3-mundo-3/): Aula #23 — Tratamento de Erros e Exceções; exercícios #113 — Funções aprofundadas em Python e #115a — Criando um menu.

Em cada exercício, leia o enunciado, pause e tente resolver antes de assistir à resolução.

#### O que você precisa entender

- Coloque no `try` somente a conversão que pode falhar e capture a exceção específica.
- Evite `except:` genérico; apresente uma mensagem que permita corrigir a entrada.

#### O que fazer

- [ ] Resolva os exercícios #113 e #115a em arquivos próprios.
- [ ] Complete `atividades/01-excecoes-e-menu/entrada_segura.py`.
- [ ] Complete o checkpoint local:

```text
atividades/01-excecoes-e-menu/projeto_cadastro/
├── main.py
└── interface.py
```

- [ ] Teste o menu com uma opção inválida e com a opção de saída.

#### Como validar

Texto vazio, texto não numérico e número negativo não encerram o programa; o menu permanece ativo e encerra pela opção definida.

- Os exercícios #113 e #115a foram tentados antes das resoluções.
- A leitura segura aceita somente inteiro não negativo.
- O menu local abre, recusa opção inválida e encerra corretamente.

#### Arquivos vazios dos desafios do Curso em Vídeo

Cole o enunciado em cada arquivo e escreva sua própria tentativa antes de assistir à resolução:

- [#113 — `DESAFIO113.py`](<atividades/01-excecoes-e-menu/DESAFIO113.py>)
- [#115a — `DESAFIO115a.py`](<atividades/01-excecoes-e-menu/DESAFIO115a.py>)

## Publicação da semana no LinkedIn

- **Tema específico:** como validação e exceções impedem que uma entrada inválida derrube um menu em Python.
- **Tipo:** progresso.
- **Formato:** texto curto com duas capturas do terminal: uma entrada inválida tratada e uma execução concluída.
- **Artefato/evidência exigida:** `atividades/01-excecoes-e-menu/entrada_segura.py` e o `projeto_cadastro` executados com caso comum, texto onde se espera número, opção fora do menu e saída registrada.

### Roteiro para preencher

- **Problema inicial:** [qual entrada fazia o fluxo falhar ou produzir resultado incorreto?]
- **Regra de validação:** [o que passou a ser verificado antes de continuar?]
- **Caso comum:** [entrada, resultado esperado e observado]
- **Caso de borda:** [entrada inválida, mensagem e continuidade do programa]
- **Aprendizado:** [o que exceção, repetição e validação fazem de diferente?]
- **Próximo passo:** [qual parte ainda precisa de arquivo, teste ou organização em módulos?]

### Limitação obrigatória

Explique que o exercício é um fluxo local e pequeno, ainda sem provar persistência, testes automatizados ou comportamento sob uso real.

### Cuidado contra afirmações falsas

Não use `sistema robusto`, `pronto para produção` ou `domínio de Python`. Descreva somente o caso executado e o erro tratado. Esta publicação não libera Competências nem mudança de headline.

### Checklist de publicação

- [ ] Reexecutei os casos mostrados imediatamente antes de publicar.
- [ ] As capturas exibem entrada e saída reais, sem dados pessoais.
- [ ] Expliquei uma limitação e o próximo passo.
- [ ] Removi caminhos locais, nomes de usuário e informações sensíveis.
- [ ] Não apresentei o exercício como experiência profissional.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
