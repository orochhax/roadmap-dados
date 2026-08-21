# Enunciado — Landing zone segura para eventos de telecom

## Cenário real

Arquivos diários de uso e qualidade de rede chegam de parceiros antes de alimentar análises de churn. O time precisa impedir acesso público, limitar o produtor a gravar objetos e garantir que reprocessamentos usem arquivos íntegros. Você implementará essa landing zone em um projeto GCP de laboratório com orçamento controlado.

## Entradas

Prepare localmente pelo menos três arquivos pequenos e sem dados pessoais:

- dois lotes válidos em `CSV` ou `JSONL`, cada um com uma data de referência;
- um lote inválido para testar quarentena;
- manifesto com nome, data, quantidade de linhas, tamanho e checksum esperado.

Use caminhos no padrão `raw/event_date=AAAA-MM-DD/arquivo` e `quarantine/event_date=AAAA-MM-DD/arquivo`. O nome do projeto, bucket, região e service account devem ser parâmetros no roteiro, nunca valores secretos.

## Saídas obrigatórias

Preencha `roteiro_gcp.md` com:

1. projeto/região selecionados e orçamento de laboratório;
2. criação do bucket com acesso uniforme e prevenção de acesso público;
3. versionamento ou lifecycle justificado e configurado;
4. service account de ingestão com papel mínimo no bucket;
5. upload dos arquivos com verificação de tamanho, linhas e checksum;
6. teste permitido de escrita/leitura conforme o contrato;
7. teste negado de uma ação que a identidade não deveria executar;
8. consulta aos logs de auditoria ou evidência equivalente;
9. inventário final e procedimento de limpeza dos recursos.

## Regras de segurança e custo

- Não crie nem versione chave JSON de service account.
- Prefira login interativo para administração e impersonation/credencial curta para testar a carga.
- Não conceda `Owner`, `Editor`, `Storage Admin` ou papel amplo à service account de ingestão.
- Aplique IAM no recurso mais específico possível.
- Habilite prevenção de acesso público e não compartilhe URLs assinadas no Git.
- Registre valores de projeto, e-mail e IDs de conta de forma parcialmente ocultada nas evidências.
- Defina alerta de orçamento quando o ambiente permitir e estime custo mensal do volume simulado/escalado.
- Ao finalizar a evidência, remova recursos temporários ou registre por que precisam permanecer.

## Casos de borda obrigatórios

- nome de objeto já existente;
- upload interrompido ou checksum diferente;
- prefixo/data fora do padrão;
- arquivo vazio e arquivo com schema inválido;
- tentativa de exclusão com identidade apenas produtora;
- tentativa de tornar o bucket público;
- região ou projeto configurado incorretamente.

## Métricas

- integridade: 100% dos arquivos aceitos com checksum e contagem compatíveis;
- segurança: ações previstas permitidas e ações proibidas negadas;
- operação: duração de upload, taxa de sucesso, bytes armazenados e tempo até o objeto ficar disponível;
- finanças: custo atual e estimativa para 1 GB/dia por 30 dias, com premissas explícitas.

## Critério de aceite

O laboratório só está aprovado se o bucket não for público, a service account operar sem papel amplo, o teste negativo falhar por permissão, os arquivos válidos forem reconciliados e o inválido for identificado para quarentena. Evidências não podem expor token, chave, e-mail completo ou dado pessoal. O roteiro deve permitir repetir e limpar o ambiente sem depender de cliques não documentados.

## Restrições

Não cole uma sequência pronta sem entender cada comando. Consulte a documentação oficial para cada recurso e registre o motivo de cada permissão.
