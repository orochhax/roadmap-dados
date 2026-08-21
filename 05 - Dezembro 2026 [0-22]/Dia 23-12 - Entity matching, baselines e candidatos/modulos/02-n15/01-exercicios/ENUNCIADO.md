# Enunciado — Índice de candidatos para um cadastro empresarial

## Cenário real

O cadastro mestre cresceu e comparar todos os registros recebidos com todas as empresas ficou caro. Sua missão é reduzir drasticamente os pares avaliados, preservando quase todos os vínculos verdadeiros. A equipe aceitará alguns candidatos extras; perder a empresa correta antes do ranker é muito mais grave.

## Entradas

Reutilize os dois conjuntos do N14:

- cadastro canônico com `entity_id`, nomes, domínio, país e cidade;
- registros recebidos com `record_id`, campos bagunçados e `true_entity_id` somente para avaliação.

Inclua no benchmark registros com domínio/país ausentes, nomes muito comuns, subsidiárias e casos `no_match`. Mantenha validação e teste congelados.

## Saídas obrigatórias

`gerar_candidatos.py` deve produzir:

1. tamanho do produto cartesiano teórico;
2. candidatos de um baseline com uma única chave de blocking;
3. candidatos de pelo menos três passagens complementares;
4. união deduplicada com `record_id`, `candidate_entity_id`, `source_pass` e `cheap_score`;
5. ranking inicial e arquivo `candidates` limitado a `k` itens por registro;
6. métricas de cobertura, redução, volume e tempo por passagem;
7. lista dos pares verdadeiros perdidos pelo gerador.

## Regras

- Defina o valor de `k` antes da avaliação final.
- Valores nulos não formam uma chave válida entre si.
- Cada passagem deve ter uma justificativa: por exemplo, domínio, nome+país ou vizinhos por TF-IDF.
- Una passagens sem duplicar o mesmo par e preserve a origem de cada candidato.
- Calcule as métricas antes e depois do corte em `k`.
- Não use `true_entity_id` para criar chaves ou ordenar candidatos.
- Meça tempo e quantidade de pares; qualidade sem custo não responde ao problema.

## Casos de borda obrigatórios

- registro sem domínio e sem país;
- nome curto ou extremamente comum;
- erro no primeiro caractere, que quebra blocking por prefixo;
- empresas homônimas em cidades diferentes;
- entidade verdadeira recuperada por duas passagens;
- registro `no_match` que ainda recebe candidatos;
- cadastro vazio ou registro com todos os campos vazios.

## Métricas

- principal: recall dos candidatos, também chamado pair completeness;
- apoio: Recall@1, Recall@5, Recall@10, reduction ratio, candidatos P50/P95 por consulta, tempo total, memória e pares por segundo;
- diagnóstico: contribuição exclusiva e pares adicionados por passagem.

## Critério de aceite

O gerador só segue para os modelos mais caros se alcançar recall de candidatos de pelo menos 0,95 em `k=10`, reduction ratio mínimo de 0,90 e no máximo 50 candidatos no percentil 95 antes do corte. Se o benchmark pequeno impedir a meta de redução, reporte também uma simulação de escala e explique a limitação. Toda entidade verdadeira perdida deve ser analisada; se as metas não forem atingidas, não aprove o desenho.

## Restrições

Não faça busca exaustiva escondida dentro de cada passagem. Implemente no arquivo inicial e não ajuste as regras após examinar o teste.
