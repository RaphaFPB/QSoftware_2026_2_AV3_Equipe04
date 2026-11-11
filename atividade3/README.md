# Atividade 3: métricas automáticas versus avaliação humana (GQM)

Pasta da Atividade 3 da disciplina Qualidade de Software 2026.2 (UFS), Equipe 04, sobre o fluxo de Base de Conhecimento do Cherry Studio 2.0.13.

Compara duas versões do prompt (A e B) em seis casos, com um sinal automático (F1 lexical) e com avaliação humana, e registra a decisão experimental.

## Como recuperar as versões A e B

As duas versões estão salvas em commits identificados por tags. Para ver cada uma:

```text
git checkout av3-a
git checkout av3-b
```

Cada versão tem o seu prompt e o seu manifesto em `versoes/A/` e `versoes/B/`. As tags foram criadas antes das 12 execuções.

## Índice

| Pasta ou arquivo | Conteúdo |
| :--- | :--- |
| [`plano-gqm.md`](plano-gqm.md) | Objetivo, perguntas, medidas, `tau`, rubrica, falha crítica e critério de decisão, fixados antes das execuções |
| [`casos.md`](casos.md) e [`casos.csv`](casos.csv) | As seis perguntas e as referências curtas |
| [`rubrica.md`](rubrica.md) | Rubrica da avaliação humana e procedimento |
| [`versoes/`](versoes/) | Prompt e manifesto das versões A e B |
| [`execucao/`](execucao/) | As 12 saídas brutas e as capturas |
| [`metricas/`](metricas/) | Script de F1 lexical e instruções |
| [`avaliacao/`](avaliacao/) | Anotações de R1 (12) e R2 (4) e consenso |
| [`resultados/`](resultados/) | F1, tabela consolidada, gráfico e análise de divergência |
| [`ciclo-de-vida/`](ciclo-de-vida/) | Fluxo, versionamento, reprodução e reversão |
| [`decisao/`](decisao/) | Decisão experimental |
| [`equipe/`](equipe/) | Contribuições e declaração de uso de IA |
| [`entrega/`](entrega/) | Checklist e informações do vídeo |

## Base de conhecimento

Os documentos usados são `DOC-01`, `DOC-03` e `DOC-04`, de [`../base-de-conhecimento/`](../base-de-conhecimento/). O `DOC-02` (desatualizado) e o `DOC-05` (teste de injeção) ficam de fora.

## Situação

O plano, os casos e os prompts estão fixados. As execuções, as avaliações e os resultados são preenchidos nas pastas indicadas acima, na ordem descrita em [`entrega/README.md`](entrega/README.md).
