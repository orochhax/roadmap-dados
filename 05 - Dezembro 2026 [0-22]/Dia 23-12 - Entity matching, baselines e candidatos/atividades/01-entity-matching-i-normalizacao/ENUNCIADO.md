# Enunciado — Vinculação de empresas com baselines auditáveis

## Cenário real

O Assistente IA extraiu nomes e domínios dos tickets, mas eles chegam como `ACME TELECOM LTDA`, `Acme Telecom`, `acme.com.br` e até com erros. Você deve associar cada registro recebido a uma empresa do cadastro mestre sem criar falsos vínculos entre nomes parecidos.

## Entradas

Prepare dois arquivos:

**Cadastro canônico**

- `entity_id`, `legal_name`, `trade_name`, `domain`, `country`, `city`.

**Registros recebidos**

- `record_id`, `raw_name`, `raw_domain`, `country`, `city`, `true_entity_id`.

`true_entity_id` é usado apenas para avaliação. Inclua registros sem correspondência usando valor nulo e mantenha exemplos de empresas homônimas, subsidiárias e nomes multilíngues. Divida os registros recebidos em validação e teste antes de escolher limiares.

## Saídas obrigatórias

O programa `normalizacao_baseline.py` deve gerar:

1. colunas normalizadas sem sobrescrever os valores originais;
2. previsão de três abordagens: igualdade exata, RapidFuzz e TF-IDF de caracteres;
3. para cada registro, `predicted_entity_id`, `score`, `method` e `decision` (`match`, `review` ou `no_match`);
4. métricas por método e por fatias de qualidade dos campos;
5. tabelas separadas de falsos merges e falsos splits;
6. tempo total e latência por consulta.

## Regras

- Defina e documente quais sufixos jurídicos serão removidos; não remova palavras sem justificativa.
- Normalize domínio separadamente de nome empresarial.
- Um domínio exato pode ser um sinal forte, mas valores vazios nunca podem coincidir entre si.
- Escolha limiares na validação e use-os sem alteração no teste.
- Compare sempre com igualdade exata; não apresente apenas o método vencedor.
- Preserve registros sem correspondência e permita abstenção/revisão.
- Não use `true_entity_id` em nenhuma feature ou regra.

## Casos de borda obrigatórios

- acentos, caixa, pontuação e sufixos como `Ltda.` ou `S.A.`;
- domínio vazio, subdomínio e prefixo `www`;
- duas empresas com nomes quase iguais e países diferentes;
- razão social diferente do nome fantasia;
- registro sem correspondência no cadastro;
- abreviação, transposição ou erro de digitação;
- nomes curtos, como `Oi`, que podem gerar similaridade enganosa.

## Métricas

- principal: precisão dos matches automáticos;
- apoio: recall, F1, taxa de revisão, falso merge, falso split e latência P95;
- fatias: presença de domínio, idioma/país e tamanho do nome.

## Critério de aceite

Para recomendar automação, o método deve manter precisão mínima de 0,95 nos matches automáticos e elevar o recall em pelo menos 0,10 sobre a igualdade exata, sem tratar `no_match` como erro de entrada. Se nenhum método atingir isso, aceite apenas a faixa de revisão humana e registre por que a automação foi rejeitada. O trabalho precisa conter ao menos cinco falsos merges/splits analisados ou todos os erros, caso existam menos de cinco.

## Restrições

Não procure código completo de entity matching. Implemente as etapas no arquivo inicial e use o teste uma única vez para a avaliação final.
