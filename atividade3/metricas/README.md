# Métricas automáticas

Cálculo do F1 lexical das 12 respostas contra as referências dos casos.

## Como rodar

1. Montar um CSV de entrada com o cabeçalho `caso,versao,resposta,referencia` e uma linha por resposta. As referências vêm de [`../casos.csv`](../casos.csv) e as respostas de [`../execucao/saidas-brutas/`](../execucao/saidas-brutas/).
2. Rodar o script com o limiar fixado no plano:

```text
python atividade3/metricas/f1_lexical.py entrada.csv --tau 0.5 --saida resultados-f1.csv
```

A saída tem as colunas `caso,versao,precisao,revocacao,F1,sinal_auto`. O sinal automático vale 1 quando `F1 >= 0,5`. Salvar o resultado em [`../resultados/f1-lexical.csv`](../resultados/f1-lexical.csv).

## Atalho com os scripts da equipe

Depois que as 12 saídas estiverem preenchidas em `execucao/saidas-brutas/`, rodar da raiz do repositório:

```text
python atividade3/metricas/preparar_avaliacao.py
```

O script confere as 12 saídas (recusa se faltar alguma resposta), monta `resultados/entrada-f1.csv`, calcula `resultados/f1-lexical.csv` com o `f1_lexical.py` e `tau = 0,5`, e gera as planilhas cegas `avaliacao/planilha-R1.csv` (12 saídas) e `avaliacao/planilha-R2.csv` (CT01 e CT05 em A e B). Os IDs são sorteados e gravados em `avaliacao/chave-anonimizacao.csv`, que está no `.gitignore` e não é publicada antes do fim das avaliações. A chave não é sorteada de novo se já existir.

Depois que R1 e R2 preencherem `avaliacao/r1.csv` e `avaliacao/r2.csv` (e, se divergirem, `avaliacao/consenso.csv` com `id_anonimo,correcao,relevancia,suporte,falha_critica,justificativa`), rodar:

```text
python atividade3/metricas/consolidar.py
```

Ele gera `resultados/tabela-consolidada.csv`, `resultados/resumo-automatico.md` (médias, aprovação x/6, concordância x/12, R1 e R2 x/4 e lista de divergências) e `resultados/grafico-resultados.png`. Para o PNG é preciso `pip install matplotlib`, e sem ele sai um SVG simples. A aplicação do critério de avanço no resumo é só a conta. A decisão é registrada pela equipe em `decisao/decisao.md`.

## Definição

Normalização Unicode NFC, `casefold`, tokens de palavras (`\w+`) e interseção de multiconjuntos. Precisão = tokens em comum ÷ tokens da resposta. Revocação = tokens em comum ÷ tokens da referência. F1 = 2 × P × R ÷ (P + R), e F1 = 0 quando P + R = 0. Uma resposta vazia tem F1 = 0 e entra na conta.

## Origem do script

`f1_lexical.py` implementa o F1 lexical descrito no enunciado da atividade (NFC, `casefold`, tokens de palavras e interseção de multiconjuntos). [CONFERIR: se o arquivo é o do kit fornecido pelo professor, citar a origem aqui.]

## Resultados

| Versão | F1 médio | F1 mediano | Sinais automáticos positivos |
| :--- | ---: | ---: | ---: |
| A | 0,249 | 0,229 | 1/6 (CT03) |
| B | 0,300 | 0,306 | 0/6 |

Valores por saída em [`../resultados/f1-lexical.csv`](../resultados/f1-lexical.csv). A revocação foi alta na maioria das saídas (até 1,0), mas a precisão foi baixa, porque as respostas são bem mais longas que as referências curtas. Por isso quase nenhuma saída chega a `tau = 0,5`.
