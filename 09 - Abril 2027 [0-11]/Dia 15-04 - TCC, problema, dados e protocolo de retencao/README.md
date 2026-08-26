# TCC — dados sintéticos, contrato temporal e protocolo

**Data de estudo:** 15/04/2027
**Carga planejada:** 4 a 5 horas

## Objetivo do dia

Construir e auditar os dois conjuntos do TCC: snapshots temporais para prever churn e um piloto randomizado explicitamente simulado para medir resposta à campanha. O protocolo deve impedir que tratamento, resultado ou informação futura virem features do modelo de risco.

## Atividades do dia

Pesquise exatamente:

- `synthetic churn dataset temporal customer snapshots`
- `decision timestamp prediction horizon feature availability`
- `data leakage churn model post outcome variables`
- `randomized experiment intention to treat treatment assignment`
- `randomization balance check standardized mean difference`
- `data card synthetic data limitations`

Siga o guia e o roteiro disponíveis abaixo e preserve o escopo congelado do TCC.

### Conteúdo e atividades — TCC — dados, schema, leakage e protocolo experimental

**Arquivos da atividade:** [abrir a pasta `01-tcc-dados-schema-leakage-e-protocolo`](<atividades/01-tcc-dados-schema-leakage-e-protocolo/>)

#### Objetivo

Criar uma base sintética coerente com a data de decisão e um piloto randomizado simulado que permita estimar efeito incremental sem confundir correlação com causalidade. A transparência da geração vale mais que um resultado favorável.

#### Arquivos e dados

- **Enunciado local:** `atividades/01-tcc-dados-schema-leakage-e-protocolo/roteiro_tcc.md`.
- **Projeto canônico:** `projetos/telecom-customer-intelligence/`.
- **Saídas esperadas:** snapshots sintéticos, piloto sintético, manifesto/hash, `data_card.md` atualizado e `docs/tcc-protocolo.md`.
- **Unidade preditiva:** cliente elegível × data de decisão.
- **Unidade experimental:** cliente elegível randomizado no piloto simulado.

#### Pesquise exatamente

- `temporal train validation test split churn`
- `feature availability decision time leakage audit`
- `synthetic data generation reproducible seed manifest hash`
- `randomized controlled trial allocation concealment intention to treat`
- `covariate balance randomized experiment standardized difference`
- `missing data mechanism MCAR MAR MNAR practical`

#### Contratos obrigatórios

##### Snapshot preditivo

Inclua identificador anonimizado, data de decisão, features anteriores ao corte e churn observado apenas após o horizonte. Defina explicitamente a disponibilidade de cada campo.

##### Piloto randomizado simulado

Inclua elegibilidade, atribuição aleatória, tratamento ofertado/recebido, desfecho no horizonte e probabilidade de atribuição. Rotule arquivo e documentação com `SIMULADO`.

#### O que fazer

- [ ] Gere ambos os datasets com seed, versão, schema e regras documentadas.
- [ ] Valide chave, tipos, faixas, datas, duplicatas, nulos e cardinalidade.
- [ ] Faça auditoria de disponibilidade e remova features pós-decisão ou pós-tratamento.
- [ ] Congele splits temporais por data para os modelos de risco.
- [ ] Congele elegibilidade, randomização, estimando e análise por intenção de tratar do piloto.
- [ ] Faça checks de equilíbrio sem exigir igualdade perfeita nem rerandomizar até obter resultado conveniente.
- [ ] Registre limites: dados sintéticos demonstram método, não impacto real em clientes.

#### Casos de borda

- cliente duplicado na mesma data;
- horizonte ainda não observado;
- feature registrada depois da decisão;
- cliente fora da elegibilidade no piloto;
- atribuição ausente ou inválida;
- grupo sem desfecho observado;
- slice com amostra pequena.

#### Como validar

- Schemas e testes impedem dados futuros/pós-tratamento.
- Split temporal e protocolo experimental estão congelados e versionados.
- Randomização simulada e limites de inferência estão documentados.
- Contagens e hashes tornam os dois dados reproduzíveis.

## Integração do dia

O snapshot preditivo responde quem tem maior risco antes da campanha. O piloto simulado responde quanto a campanha alterou retenção entre grupos randomizados. Mantenha schemas, datas, alvos e métricas separados.

## Finalização

Antes de concluir, confirme:

- Os dois datasets têm schema, seed, período, hash e declaração de simulação.
- A disponibilidade de cada coluna foi comparada com a data de decisão, e os splits temporais e o protocolo do piloto foram congelados.
- Testes de schema, duplicatas, leakage e randomização têm resultado esperado definido.

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.
