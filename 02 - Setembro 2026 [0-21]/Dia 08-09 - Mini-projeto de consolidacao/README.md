# Mini-projeto de consolidação

## Aprenda agora

Um esquema define campos e tipos esperados. Uma execução idempotente recria a mesma saída para a mesma entrada, sem duplicar registros.

```python
campos_obrigatorios = {"id", "cidade", "duracao_min"}
esquema_valido = campos_obrigatorios <= set(registro)

with open("relatorio.csv", "w", encoding="utf-8", newline="") as saida:
    # grave o resultado completo; não acrescente uma segunda cópia
    pass
```

**Erro comum:** abrir a saída em modo de acréscimo e duplicar linhas ao executar o projeto novamente.

## Conquista para o LinkedIn

- **Ação concreta:** após concluir o mini-projeto, atualize o título profissional.
- **Novo título:** `Engenharia de Software | Python`.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Entradas:** um CSV ou JSON de incidentes com `id`, `cidade`, `prioridade`, `duracao_min` e `resolvido`.
- **Fallback local:** se não houver módulos prontos, crie `projeto-semanal/dados/incidentes.json` com seis registros — quatro válidos, um id duplicado e um registro com cidade vazia — e implemente no projeto apenas leitura, validação e resumo.

## Núcleo essencial

1. [ ] Monte `projeto_semana02` usando somente os módulos necessários para leitura, validação e métricas.
2. [ ] Leia a entrada, valide o esquema e gere `resumo.json` e `relatorio.csv` em uma única execução.
3. [ ] Defina cinco regras de qualidade no README e implemente pelo menos três delas no código.
4. [ ] Teste seis casos: dois válidos, dois inválidos e dois de borda.

## Prática obrigatória

- [ ] Reproduza a execução em um segundo ambiente limpo usando apenas as instruções e dependências registradas.
- [ ] Adicione um incidente com id duplicado e cidade vazia; faça o relatório informar separadamente os dois problemas.
- [ ] Execute a aplicação duas vezes com a mesma entrada e confira que `resumo.json` e `relatorio.csv` não acumulam linhas.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.
