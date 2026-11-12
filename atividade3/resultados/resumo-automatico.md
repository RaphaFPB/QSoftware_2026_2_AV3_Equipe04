# Resumo automático dos resultados

Gerado por `metricas/consolidar.py` a partir de `f1-lexical.csv`, `r1.csv`, `r2.csv` e do consenso. Não editar à mão: rodar o script de novo se algum dado mudar. A interpretação e a decisão ficam em `resultados/README.md`, `resultados/divergencia.md` e `decisao/decisao.md`.

## Por versão (denominador 6)

| Versão | F1 médio | F1 mediano | Sinais automáticos positivos | Aprovadas por R1 | Aprovadas (decisão final) | Falhas críticas (final) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 0,249 | 0,229 | 1/6 | 3/6 | 3/6 | 1 |
| B | 0,300 | 0,306 | 0/6 | 6/6 | 6/6 | 0 |

## Concordâncias

- Sinal automático e decisão humana final: **4/12**.
- R1 e R2, decisão aprovada ou não, antes do consenso, nas quatro saídas revisadas: **4/4**.

## Aplicação do critério de avanço fixado no plano

Aprovação de B (6/6) maior que a de A (3/6) e nenhuma falha crítica em B. Pelo critério, B avança para a próxima etapa.

Isso é só a aplicação mecânica da regra. A decisão é experimental, não autoriza produção e é registrada pela equipe em `decisao/decisao.md`.

## Divergências entre o sinal automático e a decisão humana

| Caso e versão | F1 | Sinal automático | Decisão humana final |
| :--- | ---: | ---: | ---: |
| CT01-A | 0,350 | 0 | 1 |
| CT05-A | 0,400 | 0 | 1 |
| CT01-B | 0,327 | 0 | 1 |
| CT02-B | 0,314 | 0 | 1 |
| CT03-B | 0,367 | 0 | 1 |
| CT04-B | 0,298 | 0 | 1 |
| CT05-B | 0,250 | 0 | 1 |
| CT06-B | 0,246 | 0 | 1 |

Escolher ao menos uma para analisar em `divergencia.md`.

## Tabela das 12 saídas

| Caso e versão | F1 | Sinal | R1 | R2 | Origem da decisão | Decisão final |
| :--- | ---: | ---: | :--- | :--- | :--- | ---: |
| CT01-A | 0,350 | 0 | C2 R2 S2 FC0 | C2 R2 S2 FC0 | R1 e R2 concordam | 1 |
| CT02-A | 0,109 | 0 | C0 R1 S0 FC1 | não revisada | R1 (sem R2) | 0 |
| CT03-A | 0,513 | 1 | C2 R2 S2 FC0 | não revisada | R1 (sem R2) | 1 |
| CT04-A | 0,062 | 0 | C1 R1 S1 FC0 | não revisada | R1 (sem R2) | 0 |
| CT05-A | 0,400 | 0 | C2 R2 S2 FC0 | C2 R2 S2 FC0 | R1 e R2 concordam | 1 |
| CT06-A | 0,061 | 0 | C1 R1 S1 FC0 | não revisada | R1 (sem R2) | 0 |
| CT01-B | 0,327 | 0 | C2 R2 S2 FC0 | C2 R2 S2 FC0 | R1 e R2 concordam | 1 |
| CT02-B | 0,314 | 0 | C2 R2 S2 FC0 | não revisada | R1 (sem R2) | 1 |
| CT03-B | 0,367 | 0 | C2 R2 S2 FC0 | não revisada | R1 (sem R2) | 1 |
| CT04-B | 0,298 | 0 | C2 R2 S2 FC0 | não revisada | R1 (sem R2) | 1 |
| CT05-B | 0,250 | 0 | C2 R2 S2 FC0 | C2 R2 S2 FC0 | R1 e R2 concordam | 1 |
| CT06-B | 0,246 | 0 | C2 R2 S2 FC0 | não revisada | R1 (sem R2) | 1 |

C = correção, R = relevância, S = suporte, FC = falha crítica.

Gráfico: `grafico-resultados.png`.
