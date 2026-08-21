# Módulos, pacotes e ambientes

## Aprenda agora

Um ambiente virtual isola dependências do projeto. Como este repositório está no OneDrive, mantenha o ambiente fora da pasta sincronizada e registre somente as dependências:

```powershell
$roadmapVenv = Join-Path $env:LOCALAPPDATA "roadmap-venvs\roadmap-ds"
python -m venv $roadmapVenv
& "$roadmapVenv\Scripts\Activate.ps1"
python -m pip install pandas
python -m pip freeze > 03-evidencias/requirements.txt
```

Use `assert resultado == esperado` apenas para verificações de desenvolvimento, não para validar entrada do usuário.

**Erro comum:** executar `pip` fora do ambiente e gerar um `requirements.txt` com pacotes de outros projetos.

Se o PowerShell bloquear a ativação, não altere a política global: execute diretamente `& "$roadmapVenv\Scripts\python.exe" -m pip ...`.

## Aulas complementares — terminal Linux

- [ ] Curso em Vídeo — Aula #22: **Módulos e Pacotes**.
- [ ] Curso Linux #08 — **Terminal Linux: Referência Global** (30:29).
- [ ] Curso Linux #09 — **Manipulação de Arquivos com Linux** (33:12).
- **Prática:** localize o projeto, crie uma pasta temporária dentro do exercício, copie um arquivo de teste e remova apenas essa cópia.
- Use PowerShell, WSL ou Git Bash já disponível; não troque de sistema operacional.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/main.py`.
- **Dados:** cenários e valores já preenchidos no arquivo principal.

## Núcleo essencial

1. [ ] Separe uma função em `noc_utils/validacao.py` e outra em `noc_utils/metricas.py` e importe ambas em `main.py`.
2. [ ] Crie e ative o ambiente fora do OneDrive, instale uma dependência de demonstração e gere `03-evidencias/requirements.txt`.
3. [ ] Execute `main.py` importando o pacote e use pelo menos dois `assert` simples para conferir uma métrica e uma validação.

## Prática obrigatória

- [ ] Separe também a leitura e a gravação em `noc_utils/io.py`.
- [ ] Reproduza a execução em um segundo ambiente virtual limpo usando somente `03-evidencias/requirements.txt`.
- [ ] Documente apenas os comandos executados com sucesso.
- [ ] Crie em `noc_utils/metricas.py` uma função `percentual_resolvido(total, resolvidos)` e use-a em `main.py` sem copiar o cálculo.
- [ ] Teste a função com `(100, 82)` e `(0, 0)`; o segundo caso deve ser tratado sem divisão por zero.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.
