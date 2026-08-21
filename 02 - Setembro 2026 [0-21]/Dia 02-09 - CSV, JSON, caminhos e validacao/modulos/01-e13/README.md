# Arquivos CSV, JSON e caminhos

## Aprenda agora

CSV representa linhas e colunas; JSON representa listas e objetos. `pathlib.Path` cria caminhos independentes da pasta usada para iniciar o programa.

```python
from pathlib import Path
import csv

base = Path(__file__).resolve().parent
with (base / "incidentes.csv").open(encoding="utf-8", newline="") as arquivo:
    incidentes = list(csv.DictReader(arquivo))
```

**Erro comum:** usar um caminho relativo ao terminal e fazer o programa funcionar apenas quando executado de uma pasta específica.

## Aulas complementares — terminal

- [ ] Curso Linux #07.1 — **Terminal no Linux: Introdução** (32:22).
- [ ] Curso Linux #07.2 — **Terminal no Linux: Manipulando diretórios** (30:20).
- **Prática no sistema atual:** no PowerShell, use `Get-Location`, `Get-ChildItem`, `Set-Location` e `Set-Location ..`; se já usa WSL ou Git Bash, repita com `pwd`, `ls` e `cd ..`.
- Não é necessário instalar outro sistema operacional.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-007-arquivos-csv-json-e-caminhos.py`.
- **Dados:** `01-exercicios/incidentes.csv` e `01-exercicios/metas.json`.

## Núcleo essencial

1. [ ] Use os arquivos preparados com quatro linhas válidas para praticar leitura de CSV com `csv` e leitura de JSON com `json`, sem pandas.
2. [ ] Converta somente os campos numéricos e booleanos necessários e associe cada incidente à meta de sua cidade.
3. [ ] Grave `relatorio_consolidado.csv` com a coluna `dentro_da_meta` e confira manualmente duas linhas.

## Prática obrigatória

- [ ] Acrescente ao CSV a linha `INC-013,Ilhéus,queda de energia,P2,85,140,true`, adicione ao JSON a meta de 90 minutos para Ilhéus e gere novamente o consolidado.
- [ ] Execute o programa a partir da raiz do repositório e da própria pasta; use `pathlib` e confirme que ambas as execuções encontram os mesmos arquivos e produzem o mesmo resultado.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.
