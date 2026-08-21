# Problema e governança

## Aulas complementares — privacidade, LGPD e vieses

- [ ] Segurança da Informação, Módulo 2 — **Lei Geral de Proteção de Dados (LGPD)** (19:48).
- [ ] Curso em Vídeo IA #39 — **Vieses em IA: Desvendando Preconceitos na IA** (13:56).
- Conecte as aulas às variáveis sensíveis e proibidas do Núcleo essencial. Elas não substituem a análise concreta do conjunto de dados e da decisão de crédito.

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-081-problema-e-governanca.ipynb`.
- **Dados:** `dados/credito.csv`.

## Aprenda agora

- **Definição:** label é o evento previsto; proxy é uma medida substituta; variável sensível representa grupo protegido; governança define uso, revisão e responsabilidade.
- **Exemplo mínimo:** documente “default = atraso ≥90 dias em 12 meses”, usuário da decisão, ação permitida e revisão humana.
- **Erro comum:** usar uma proxy sem validar seu significado ou excluir variável sensível e assumir que não há viés.

## Núcleo essencial

1. [ ] Defina case de risco: prever default em 90 dias e apoiar aprovação, revisão ou rejeição.
2. [ ] Liste variáveis proibidas, sensíveis ou potencialmente discriminatórias.
3. [ ] Defina custos de falso negativo, falso positivo e revisão manual.

## Prática obrigatória

- [ ] Crie política de governança com responsável, frequência de revisão e trilha de auditoria.
- [ ] Escreva critérios de sucesso técnico, econômico e de equidade.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-081-problema-e-governanca.ipynb`:** Acrescente à política a regra de revisão humana para probabilidade entre 0,40 e 0,60 e calcule o volume dessa faixa.
- [ ] **Em `01-exercicios/dia-081-problema-e-governanca.ipynb`:** Liste quais colunas seriam removidas se contivessem atributo sensível ou uma proxy direta de renda familiar protegida.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-081-problema-e-governanca.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.
