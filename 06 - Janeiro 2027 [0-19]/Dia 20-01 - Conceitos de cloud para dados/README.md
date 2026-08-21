# Conceitos de cloud para dados

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-101-conceitos-de-cloud-para-dados.py`.
- **Entradas:** diagrama da API e tabela local de requisitos. **Fallback local:** mapeamento conceitual sem criar recurso.

## Aprenda agora

- **Definição:** IAM controla identidades e permissões; menor privilégio concede só o necessário; lock-in é custo de trocar fornecedor.
- **Exemplo mínimo:** mapeie “arquivo→objeto, API→serviço de container, segredo→cofre” em um provedor e limite leitura/escrita por recurso.
- **Erro comum:** usar credencial de administrador na aplicação ou comparar provedores apenas pelo nome do produto.

## Núcleo essencial

1. [ ] Desenhe arquitetura cloud para ingestão, armazenamento, treino, registro e serving usando um provedor à escolha.
2. [ ] Mapeie cada componente para AWS, Azure ou GCP sem tentar aprender os três.
3. [ ] Defina IAM mínimo para cientista, pipeline e API.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-101-conceitos-de-cloud-para-dados.py`:** compare a arquitetura para 10 GB e 1 TB por dia, registrando custo qualitativo, gargalos e riscos de disponibilidade.
- [ ] Retire a permissão de escrita da API no armazenamento bruto e explique qual operação permanece permitida pelo menor privilégio.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-101-conceitos-de-cloud-para-dados.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.
