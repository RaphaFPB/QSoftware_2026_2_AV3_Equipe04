# Métricas automáticas

Cálculo do F1 lexical das 12 respostas contra as referências dos casos.

## Como rodar

1. Montar um CSV de entrada com o cabeçalho `caso,versao,resposta,referencia` e uma linha por resposta. As referências vêm de [`../casos.csv`](../casos.csv) e as respostas de [`../execucao/saidas-brutas/`](../execucao/saidas-brutas/).
2. Rodar o script com o limiar fixado no plano:

```text
python atividade3/metricas/f1_lexical.py entrada.csv --tau 0.5 --saida resultados-f1.csv
```

A saída tem as colunas `caso,versao,precisao,revocacao,F1,sinal_auto`. O sinal automático vale 1 quando `F1 >= 0,5`. Salvar o resultado em [`../resultados/f1-lexical.csv`](../resultados/f1-lexical.csv).

## Definição

Normalização Unicode NFC, `casefold`, tokens de palavras (`\w+`) e interseção de multiconjuntos. Precisão = tokens em comum ÷ tokens da resposta. Revocação = tokens em comum ÷ tokens da referência. F1 = 2 × P × R ÷ (P + R), e F1 = 0 quando P + R = 0. Uma resposta vazia tem F1 = 0 e entra na conta.

## Origem do script

`f1_lexical.py` implementa o F1 lexical descrito no enunciado da atividade (NFC, `casefold`, tokens de palavras e interseção de multiconjuntos). [CONFERIR: se o arquivo é o do kit fornecido pelo professor, citar a origem aqui.]

## Resultados

[PREENCHER: F1 médio e mediano de A e de B, e quantos sinais automáticos positivos em cada versão.]
