# Cursos gratuitos selecionados

O roadmap não depende de curso pago. Vídeos entram somente quando ajudam a executar a prática da mesma sessão; playlist completa, certificado e maratona de conteúdo não são metas.

O arquivo `cursos.md` foi usado como fonte da curadoria. O README de cada dia é a referência final: nele ficam o **nome completo e exato da aula**, o link direto ou de pesquisa no YouTube, o trecho necessário quando uma aula longa foi dividida e a prática correspondente. Assim, basta copiar o título em negrito e pesquisar sem tentar adivinhar qual vídeo assistir.

Cada sessão aceita no máximo **duas horas de vídeo**. Assistir não conclui o estudo: ainda é obrigatório executar a prática do dia e salvar a resposta no arquivo indicado pelo enunciado. Quando um vídeo é maior que a carga segura, ele aparece dividido entre dias, com início e fim informados.

## Fontes já selecionadas

| Fonte gratuita | Uso no roadmap | Seleção |
|---|---|---|
| [Python — Curso em Vídeo](<trilha-curso-em-video-python.md>) | 24/08–04/09 | Aulas #12–#23; exercícios escolhidos até #115c |
| [Linux — Curso em Vídeo](https://www.cursoemvideo.com/curso/linux/) | 02–03/09 | Terminal #07.1/#07.2; referência global #08; arquivos #09 |
| [MySQL — Curso em Vídeo](https://www.cursoemvideo.com/curso/mysql/) | 17–25/09 | Consultas #11–#16; as aulas introdutórias #01/#03/#04 foram retiradas por repetirem a base já estudada |
| [Segurança da Informação — Curso em Vídeo](https://www.cursoemvideo.com/curso-categoria/seguranca-da-informacao/) | 15/09, 26/11 e 24/12 | Divulgação, manipulação e proteção de dados; LGPD |
| [Git e GitHub — Curso em Vídeo](https://www.cursoemvideo.com/curso/curso-de-git-e-github/) | 07/12 e 13/01 | Git, repositório, restauração, branches, issues, segurança e Markdown |
| [Inteligência Artificial — Curso em Vídeo](https://www.cursoemvideo.com/curso/curso-gratis-de-inteligencia-artificial/) | 24/12–06/01 | ML conceitual, viés, LLM, tokens, prompts, fontes e ataques a prompt |

## Trilhas oficiais e evidências externas obrigatórias

As cinco trilhas abaixo passam a acompanhar as práticas do roadmap. Preparação, simulados autorais, critérios de prontidão e regras de LinkedIn estão em [Credenciais gratuitas, preparação e simulados](<credenciais-gratuitas-e-simulados.md>).

| Fonte oficial gratuita | Evidência planejada | Distinção obrigatória |
|---|---|---|
| [Microsoft Learn — Prepare data for analysis with Power BI](https://learn.microsoft.com/en-us/training/paths/prepare-data-power-bi/) | Achievements dos módulos e trophy da learning path | Não é a certificação PL-300, cuja prova profissional é paga |
| [dbt Fundamentals (VS Code)](https://learn.getdbt.com/learn/course/dbt-fundamentals-vs-code) | Conclusão do curso no perfil da plataforma | Não é `dbt Analytics Engineering Certification Exam`, que exige avaliação separada e paga |
| [Google Cloud for students](https://cloud.google.com/edu/students) | Skill badge [Derive Insights from BigQuery Data](https://www.skills.google/paths/18/course_templates/623?locale=en), usando créditos estudantis se aprovados | Skill badge não é Google Cloud Certification profissional |
| [Databricks Fundamentals](https://customer-academy.databricks.com/learn/courses/2206/databricks-fundamentals) | `Databricks Fundamentals Accreditation` e badge verificável | Acreditação introdutória não supervisionada não é certificação profissional |
| [EF SET four-skill](https://www.efset.org/4-skill/?lang=en) | Certificado gratuito de reading, listening, writing e speaking com nível CEFR | Teste online não supervisionado; não é TOEFL ou IELTS |

Curso ou badge não substitui o artefato. A conclusão só libera uma atualização de LinkedIn quando a prática correspondente executar, for conferida e puder ser explicada.

O curso de MySQL fornece conceitos transferíveis, mas a prática continua em DuckDB ou PostgreSQL. Não é necessário instalar WAMP, XAMPP ou PHPMyAdmin. Para Linux, use PowerShell, WSL ou Git Bash já disponível; não reinstale o computador.

## Índice da curadoria incorporada

Os blocos abaixo já receberam aulas selecionadas. Esta tabela serve apenas para localizar o período; os nomes completos e exatos, links, durações e trechos estão nos READMEs dos respectivos dias, sem repetir aqui dezenas de títulos.

| Bloco coberto | Dias de estudo | Papel das aulas selecionadas |
|---|---|---|
| API REST e JSON | 02/09 | Introduzir consumo de API antes da prática com autenticação, paginação, falhas e carga incremental |
| pandas e formatos de dados | 08–09/09 e 16/12 | Dividir a formação longa de pandas, reforçar reshaping e comparar CSV, Parquet e Feather no momento de storage |
| Excel analítico e Power BI | 14–15/09 | Cobrir fórmulas, funções, tabela dinâmica, segmentação, DAX e construção de dashboard sem consumir o tempo da prática |
| SQL, DuckDB e modelagem de banco | 17–25/09 | Avançar diretamente para consultas, CTEs, funções de janela, modelagem conceitual/lógica/física e análise local com DuckDB |
| Estatística e inferência | 28/09–08/10 | Apoiar variáveis, frequências, medidas, probabilidade, distribuição normal, amostragem, intervalo de confiança, teste de hipótese e regressão |
| Machine Learning e projeto de churn | 09/10–12/11 | Acompanhar o ciclo analítico, regressão, classificação, métricas, árvores, XGBoost, pipeline, tuning e novas predições |
| Clustering | 09/11 | Ligar a teoria de K-Means a uma atividade prática de segmentação e interpretação dos grupos |
| PyTorch e visão computacional | 13–18/11 | Dividir conteúdos longos entre tensores, training loop, MLP, CNN, transfer learning, detecção e segmentação |
| Séries temporais | 19–25/11 | Construir a base de componentes, estacionariedade, autocorrelação, AR/MA, diferenciação, validação temporal e forecasting |
| Engenharia, testes e API de modelo | 01–10/12 | Conectar ETL/ELT, Docker e Airflow a testes com Pytest, validação com Pydantic, contrato com FastAPI e entrega reproduzível |
| Storage e BigQuery | 15–18/12 | Relacionar formatos colunares, particionamento, clustering, custo de consulta e execução em cloud com a prática oficial |
| NLP, entity matching e embeddings | 22–30/12 | Cobrir pipeline de NLP, lematização, NER, TF-IDF, vetores, fastText, candidatos, ranking e avaliação de matching |
| RAG | 04–06/01 | Dividir um projeto completo entre ingestão, chunking, recuperação, geração com fontes e avaliação |
| Streamlit | 11/01 | Sustentar a interface do produto integrador com filtros, gráficos, barra lateral e dashboard |

Não procure todos ao mesmo tempo. O próximo material é sempre o do primeiro dia ainda não concluído.

## O que enviar para avaliação

Copie este modelo quando encontrar um curso ou playlist:

```text
Nome do curso ou playlist:
Link (se tiver):
Aulas que parecem relevantes:
Duração de cada aula:
Assunto que quero substituir ou reforçar:
```

Uma nova aula será adicionada somente se:

- ensina um conceito usado na própria sessão;
- não repete material já dominado;
- deixa tempo para escrever código ou resolver consultas;
- tem exemplo compatível com a versão atual da ferramenta;
- melhora a prática ou a explicação, e não apenas oferece certificado.

Mesmo quando uma aula é aprovada, a prática e o arquivo de resposta continuam obrigatórios. O vídeo explica; o artefato demonstra que você sabe aplicar.
