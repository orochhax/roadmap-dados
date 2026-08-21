# Entrega de experimento

## Conquista para o LinkedIn

- **Competências:** depois de executar o experimento e defender sua conclusão, adicione **Análise estatística** e **Teste A/B**.
- **Projetos ou Destaques:** inclua a entrega somente se o relatório estiver reproduzível, revisado e acessível por link.
- **Sobre:** você pode mencionar sua primeira análise de experimento com incerteza e limitações. Não altere a headline somente por esta sessão.
- Siga o [Guia de LinkedIn e evidências](<../../../../00 - Recursos Compartilhados/linkedin-e-evidencias.md>).

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.
- **Entradas concretas:** uma tabela A/B com grupo e resultado, a definição da métrica primária e uma consulta SQL de validação.
- **Fallback local:** gere 500 observações por grupo com seed 42 e probabilidades de sucesso 0,10 e 0,12; grave grupo e resultado em um DataFrame e use-o em toda a entrega.

## Núcleo essencial

1. [ ] Integre as três entradas listadas em Preparação; use a base sintética local se alguma entrada estiver ausente.
2. [ ] Registre métrica primária, efeito mínimo e regra de decisão antes de olhar o resultado final.
3. [ ] Valide equilíbrio dos grupos e estime efeito com intervalo.
4. [ ] Entregue README e relatório de decisão de até duas páginas com resultado, risco e próxima ação.
5. [ ] Escreva `projeto-mensal/README.en.md` em inglês, com 150–250 palavras, cobrindo problema, dados, método, resultados, limitações e reprodução.
6. [ ] Prepare `projeto-mensal/docs/presentation-en.md` como roteiro em inglês para uma apresentação falada de 2–3 minutos.

## Prática obrigatória

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Refaça a regra de decisão usando efeito mínimo relevante de 1,0 ponto percentual e compare com a regra de 1,5 ponto.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Remova a cidade com mais observações, registre efeito e intervalo e identifique se a decisão depende desse segmento.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial, incluindo `README.en.md` e `docs/presentation-en.md`.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.
