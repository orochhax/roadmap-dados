# Assistente de suporte com IA

Projeto local para praticar LLMs, busca semântica e RAG sem depender de API paga. Mocks, busca lexical e respostas extrativas permitem executar e avaliar todo o fluxo localmente.

## Diagnóstico e execução

- Preencha [`governanca/gate-fundamentos.md`](<governanca/gate-fundamentos.md>).
- Execute todos os artefatos de IA/RAG, independentemente das notas.
- Use [`governanca/reforco-fundamentos.md`](<governanca/reforco-fundamentos.md>) para planejar revisões posteriores das lacunas; esse registro não substitui nenhuma entrega do projeto.

## Entradas e saídas

- **Corpus:** `data/corpus/`, com 15 documentos sintéticos e hashes no manifesto.
- **Testes da miniaplicação:** `data/chamados_teste.json`.
- **Avaliação RAG:** `data/perguntas_avaliacao.csv` e `outputs/avaliacao/avaliacao_rag.csv`.
- **Configuração reproduzível:** `config/configuracao.json`.
- **Código:** pacote `src/assistente_suporte_ia/`.
- **Fallback:** tudo pode ser executado localmente; chave de API e interface web não são requisitos.

## Ambiente

No PowerShell, mantenha o ambiente virtual fora do OneDrive:

```powershell
python -m venv "$env:LOCALAPPDATA\roadmap-venvs\assistente-suporte-ia"
& "$env:LOCALAPPDATA\roadmap-venvs\assistente-suporte-ia\Scripts\Activate.ps1"
python -m pip install -r projetos/assistente-suporte-ia/requirements.txt
python -m pip install -e projetos/assistente-suporte-ia
```

## Critérios do projeto

- [ ] A miniaplicação valida 20 chamados e recusa ou solicita revisão humana quando necessário.
- [ ] O RAG responde às dez perguntas fixas com fonte ou recusa e registra as métricas completas.
- [ ] Uma execução local reproduz configuração, resultados e limitações documentadas.
