# TCC — dados, schema, leakage e protocolo experimental

## Objetivo

Criar uma base sintética coerente com a data de decisão e um piloto randomizado simulado que permita estimar efeito incremental sem confundir correlação com causalidade. A transparência da geração vale mais que um resultado favorável.

## Preparação

- **Enunciado local:** `01-exercicios/roteiro_tcc.md`.
- **Projeto canônico:** `projetos/telecom-customer-intelligence/`.
- **Saídas esperadas:** snapshots sintéticos, piloto sintético, manifesto/hash, `data_card.md` atualizado e `docs/tcc-protocolo.md`.
- **Unidade preditiva:** cliente elegível × data de decisão.
- **Unidade experimental:** cliente elegível randomizado no piloto simulado.

## Pesquise exatamente

- `temporal train validation test split churn`
- `feature availability decision time leakage audit`
- `synthetic data generation reproducible seed manifest hash`
- `randomized controlled trial allocation concealment intention to treat`
- `covariate balance randomized experiment standardized difference`
- `missing data mechanism MCAR MAR MNAR practical`

## Contratos obrigatórios

### Snapshot preditivo

Inclua identificador anonimizado, data de decisão, features anteriores ao corte e churn observado apenas após o horizonte. Defina explicitamente a disponibilidade de cada campo.

### Piloto randomizado simulado

Inclua elegibilidade, atribuição aleatória, tratamento ofertado/recebido, desfecho no horizonte e probabilidade de atribuição. Rotule arquivo e documentação com `SIMULADO`.

## Núcleo essencial

1. [ ] Gere ambos os datasets com seed, versão, schema e regras documentadas.
2. [ ] Valide chave, tipos, faixas, datas, duplicatas, nulos e cardinalidade.
3. [ ] Faça auditoria de disponibilidade e remova features pós-decisão ou pós-tratamento.
4. [ ] Congele splits temporais por data para os modelos de risco.
5. [ ] Congele elegibilidade, randomização, estimando e análise por intenção de tratar do piloto.
6. [ ] Faça checks de equilíbrio sem exigir igualdade perfeita nem rerandomizar até obter resultado conveniente.
7. [ ] Registre limites: dados sintéticos demonstram método, não impacto real em clientes.

## Casos de borda

- cliente duplicado na mesma data;
- horizonte ainda não observado;
- feature registrada depois da decisão;
- cliente fora da elegibilidade no piloto;
- atribuição ausente ou inválida;
- grupo sem desfecho observado;
- slice com amostra pequena.

## Concluído quando

- [ ] Schemas e testes impedem dados futuros/pós-tratamento.
- [ ] Split temporal e protocolo experimental estão congelados e versionados.
- [ ] Randomização simulada e limites de inferência estão documentados.
- [ ] Contagens e hashes tornam os dois dados reproduzíveis.
