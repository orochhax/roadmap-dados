# Mini-projeto de consolidacao

**Data de estudo:** 15/09/2026
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Mini-projeto de consolidacao

#### O que pesquisar
- `Mini-projeto de consolidacao Python explicado passo a passo`
- `Mini-projeto de consolidacao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-mini-projeto-de-consolidacao`](<atividades/01-mini-projeto-de-consolidacao/>)

#### O que você precisa entender

Um esquema define campos e tipos esperados. Uma execução idempotente recria a mesma saída para a mesma entrada, sem duplicar registros.

```python
campos_obrigatorios = {"id", "cidade", "duracao_min"}
esquema_valido = campos_obrigatorios <= set(registro)

with open("relatorio.csv", "w", encoding="utf-8", newline="") as saida:
    # grave o resultado completo; não acrescente uma segunda cópia
    pass
```

**Erro comum:** abrir a saída em modo de acréscimo e duplicar linhas ao executar o projeto novamente.

#### Conquista para o LinkedIn

- **Ação concreta:** após concluir o mini-projeto, atualize o título profissional.
- **Novo título:** `Engenharia de Software | Python`.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-mini-projeto-de-consolidacao/roteiro_atividades.md`.
- **Entradas:** um CSV ou JSON de incidentes com `id`, `cidade`, `prioridade`, `duracao_min` e `resolvido`.
- **Fallback local:** se não houver módulos prontos, crie `atividades/01-mini-projeto-de-consolidacao/projeto-semanal/dados/incidentes.json` com seis registros — quatro válidos, um id duplicado e um registro com cidade vazia — e implemente no projeto apenas leitura, validação e resumo.

#### O que fazer

- [ ] Monte `projeto_semana02` usando somente os módulos necessários para leitura, validação e métricas.
- [ ] Leia a entrada, valide o esquema e gere `resumo.json` e `relatorio.csv` em uma única execução.
- [ ] Defina cinco regras de qualidade no README e implemente pelo menos três delas no código.
- [ ] Teste seis casos: dois válidos, dois inválidos e dois de borda.

- [ ] Reproduza a execução em um segundo ambiente limpo usando apenas as instruções e dependências registradas.
- [ ] Adicione um incidente com id duplicado e cidade vazia; faça o relatório informar separadamente os dois problemas.
- [ ] Execute a aplicação duas vezes com a mesma entrada e confira que `resumo.json` e `relatorio.csv` não acumulam linhas.
- [ ] Preencha `atividades/01-mini-projeto-de-consolidacao/projeto-semanal/docs/apresentacao.md` e demonstre o projeto em até três minutos.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Publicação da semana no LinkedIn

- **Tema específico:** fundação em Python do Telecom Customer Intelligence — leitura, validação e resumo reproduzível de incidentes.
- **Tipo:** entrega.
- **Formato:** carrossel de cinco páginas com uma demonstração curta do terminal e link do artefato quando estiver público.
- **Artefato/evidência exigida:** mini-projeto executado, dados válidos e rejeitados separados, `relatorio.csv`, `resumo.json`, teste de id duplicado/campo vazio e reexecução sem duplicar resultado em `atividades/01-mini-projeto-de-consolidacao/projeto-semanal/`.

### Roteiro para preencher

- **Problema:** [qual resumo operacional o script precisa produzir?]
- **Entrada e contrato:** [quais campos e validações foram definidos?]
- **Fluxo:** [como leitura, validação, cálculo e saída foram separados?]
- **Resultado verificável:** [contagens ou taxa e caminho do CSV/JSON que comprova o valor]
- **Caso de borda:** [qual registro foi rejeitado e por quê?]
- **Reexecução:** [como foi comprovado que o resultado não duplicou?]
- **Link:** [repositório, relatório ou demonstração conferidos]

### Limitação obrigatória

Declare o tamanho e a natureza educacional dos dados e uma fragilidade que ainda existe na arquitetura ou nos testes.

### Cuidado contra afirmações falsas

Não chame o mini-projeto de plataforma empresarial nem afirme ganho operacional não medido. Não transforme a conclusão em cargo, experiência ou domínio amplo de Python. Competências e headline seguem o guia central.

### Checklist de publicação

- [ ] Executei o fluxo completo e um caso de borda.
- [ ] Reconciliei manualmente pelo menos um número do CSV/JSON.
- [ ] Reexecutei o pipeline e conferi ausência de duplicação.
- [ ] Removi dados pessoais, segredos e caminhos absolutos.
- [ ] Testei o link público e citei uma limitação real.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
