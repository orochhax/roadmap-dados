# Modulos, pacotes e ambientes + Python profissional: OOP, dataclasses, tipos e módulos

**Data de estudo:** 14/09/2026
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Modulos, pacotes e ambientes

#### O que pesquisar
- `Modulos, pacotes e ambientes Python explicado passo a passo`
- `Modulos, pacotes e ambientes Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-modulos-pacotes-e-ambientes`](<atividades/01-modulos-pacotes-e-ambientes/>)

#### O que você precisa entender

Um ambiente virtual isola dependências do projeto. Como este repositório está no OneDrive, mantenha o ambiente fora da pasta sincronizada e registre somente as dependências:

```powershell
$roadmapVenv = Join-Path $env:LOCALAPPDATA "roadmap-venvs\roadmap-ds"
python -m venv $roadmapVenv
& "$roadmapVenv\Scripts\Activate.ps1"
python -m pip install pandas
python -m pip freeze > "atividades/01-modulos-pacotes-e-ambientes/requirements.txt"
```

Use `assert resultado == esperado` apenas para verificações de desenvolvimento, não para validar entrada do usuário.

**Erro comum:** executar `pip` fora do ambiente e gerar um `requirements.txt` com pacotes de outros projetos.

Se o PowerShell bloquear a ativação, não altere a política global: execute diretamente `& "$roadmapVenv\Scripts\python.exe" -m pip ...`.

#### Aulas complementares — terminal Linux

- [ ] Curso em Vídeo — Aula #22: **Módulos e Pacotes**.
- [ ] Curso Linux #08 — **Terminal Linux: Referência Global** (30:29).
- [ ] Curso Linux #09 — **Manipulação de Arquivos com Linux** (33:12).
- **Prática:** localize o projeto, crie uma pasta temporária dentro do exercício, copie um arquivo de teste e remova apenas essa cópia.
- Use PowerShell, WSL ou Git Bash já disponível; não troque de sistema operacional.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-modulos-pacotes-e-ambientes/main.py`.
- **Dados:** cenários e valores já preenchidos no arquivo principal.

#### O que fazer

- [ ] Separe uma função em `noc_utils/validacao.py` e outra em `noc_utils/metricas.py` e importe ambas em `main.py`.
- [ ] Crie e ative o ambiente fora do OneDrive, instale uma dependência de demonstração e gere `atividades/01-modulos-pacotes-e-ambientes/requirements.txt`.
- [ ] Execute `main.py` importando o pacote e use pelo menos dois `assert` simples para conferir uma métrica e uma validação.

- [ ] Separe também a leitura e a gravação em `noc_utils/io.py`.
- [ ] Reproduza a execução em um segundo ambiente virtual limpo usando somente `atividades/01-modulos-pacotes-e-ambientes/requirements.txt`.
- [ ] Documente apenas os comandos executados com sucesso.
- [ ] Crie em `noc_utils/metricas.py` uma função `percentual_resolvido(total, resolvidos)` e use-a em `main.py` sem copiar o cálculo.
- [ ] Teste a função com `(100, 82)` e `(0, 0)`; o segundo caso deve ser tratado sem divisão por zero.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Python profissional: OOP, dataclasses, tipos e módulos

#### O que pesquisar
- `Python dataclasses`
- `type hints e mypy`
- `composição vs herança`
- `estrutura de pacote Python`

**Arquivos da atividade:** [abrir a pasta `02-python-profissional-oop-dataclasses-tipos`](<atividades/02-python-profissional-oop-dataclasses-tipos/>)

#### Objetivo

Transformar um script procedural de operações de telecom em componentes pequenos, tipados e testáveis. O foco não é “usar classes por usar”, mas separar representação do dado, validação, cálculo e serialização.

#### Termos complementares para pesquisar

- `Python dataclasses frozen slots`
- `Python type hints collections Sequence Mapping`
- `Python Protocol structural subtyping`
- `composition over inheritance Python`
- `mypy strict mode`
- `pytest parametrization`
- `pathlib Path read_text write_text`

#### O que fazer

Leia o [enunciado](<atividades/02-python-profissional-oop-dataclasses-tipos/ENUNCIADO.md>), complete [python_profissional.py](<atividades/02-python-profissional-oop-dataclasses-tipos/python_profissional.py>) e registre a execução no próprio artefato.

Você deverá construir um pequeno núcleo do produto **Telecom Customer Intelligence**, comparar a versão procedural com a versão modular e provar que entradas inválidas não contaminam o resumo operacional.

#### Como validar

- o arquivo executa com type hints e sem caminhos absolutos;
- os contratos e responsabilidades das classes podem ser explicados;
- os casos normal, inválido e duplicado foram testados;
- a saída foi reconciliada com um cálculo manual;
- a evidência registra uma limitação da modelagem escolhida.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
