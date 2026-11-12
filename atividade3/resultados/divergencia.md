# Divergência entre o sinal automático e a decisão humana

Houve 8 divergências em 12 saídas, todas do mesmo tipo: o F1 ficou abaixo de `tau = 0,5` e a decisão humana foi aprovar (ver [`resumo-automatico.md`](resumo-automatico.md)). Não houve sinal positivo com reprovação humana. Esta análise usa a saída B-CT05 e, como contraste, a A-CT02.

## Saída analisada: B-CT05

| Campo | Registro |
| :--- | :--- |
| Pergunta | Qual é o telefone da central de atendimento? |
| Referência | Os documentos não informam o telefone da central de atendimento |
| Resposta | Não encontrei essa informação nos documentos. |
| F1 | 0,250 (precisão 0,333, revocação 0,200). Sinal automático 0 |
| R1 e R2 | Correção 2, relevância 2, suporte 2, falha crítica 0 nas duas avaliações. Aprovada |
| Arquivo | [`../execucao/saidas-brutas/B-CT05.md`](../execucao/saidas-brutas/B-CT05.md) |

A resposta é exatamente o comportamento esperado para o caso sem evidência suficiente. Ela não inventa telefone e usa a frase de abstenção pedida pelo prompt B. Mesmo assim, das 6 palavras da resposta só 2 aparecem na referência ("não" e "documentos"). A referência diz a mesma coisa com outras palavras ("os documentos não informam o telefone"), e o F1 não reconhece a paráfrase.

## Contraste: A-CT02

A A-CT02 mostra o limite no sentido oposto. A resposta não usou a base e disse que o reembolso leva de 1 a 7 dias úteis ou até 2 faturas. A política diz 10 dias úteis. R1 deu correção 0, suporte 0 e falha crítica 1. O F1 foi 0,109, e o sinal automático acertou ao reprovar, mas a revocação foi 0,800. Das 10 palavras da referência, 8 aparecem na resposta ("o", "para", "reembolso", "é", "de", "até", "dias", "úteis"). Só faltaram "tempo" e "10", e o "10" é justamente o dado que importa. O F1 só ficou baixo porque a resposta é longa (precisão de 0,058), e não porque detectou o erro.

## O que isso mostra sobre o F1

- O F1 compara palavras e não verifica se a informação está correta nem se está sustentada pela fonte.
- Ele penaliza respostas corretas escritas de outro jeito (B-CT05) e respostas longas, mesmo quando estão certas.
- Uma resposta errada pode compartilhar quase todas as palavras da referência e diferir só no número decisivo (A-CT02), como no exemplo do enunciado de trocar "10/11" por "11/11".
- Neste experimento, a concordância entre o sinal e a decisão humana foi 4/12. O F1 com `tau = 0,5` não serviu como substituto da avaliação humana para estas respostas.
