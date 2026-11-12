# Avaliação humana

Anotações das duas pessoas avaliadoras. A rubrica e o procedimento estão em [`../rubrica.md`](../rubrica.md).

## Quem avalia

- **R1 (Thayla Almeida Figueiredo):** avalia as 12 saídas.
- **R2 (Enzo Emanuel Costa Maia):** avalia de forma independente as quatro saídas de CT01 e CT05 nas duas versões, antes de conversar com R1.

## Arquivos

| Arquivo | Conteúdo |
| :--- | :--- |
| `r1.csv` | As 12 anotações de R1 |
| `r2.csv` | As quatro anotações de R2 |
| `consenso.md` | Comparação R1 e R2 e consenso, quando houver divergência |
| `chave-anonimizacao.csv` | Chave que liga cada ID anônimo ao caso e à versão. **Não é publicada** antes do fim das avaliações |

Cada linha dos CSVs tem o ID anônimo, as três notas (0 a 2), a falha crítica (0 ou 1), se foi aprovada, a justificativa e o trecho da resposta que sustenta a nota.

## Cegamento

A planilha entregue às pessoas avaliadoras mostra só o ID, a pergunta, a referência e a resposta, sem a versão, sem a ordem e sem o F1. As planilhas `planilha-R1.csv` (12 saídas) e `planilha-R2.csv` (CT01 e CT05 em A e B) foram geradas por `metricas/preparar_avaliacao.py`, com IDs `S01` a `S12` sorteados. A chave que liga cada ID ao caso e à versão ficou fora do repositório até o fim das avaliações.

Limitações do cegamento: o estilo das respostas denuncia a versão, porque as saídas de B costumam terminar com uma linha "Fonte:" pedida pelo prompt estruturado. As saídas brutas estão no repositório com a versão no nome do arquivo, então quem avaliou foi orientado a usar só a planilha. As planilhas entregues a R1 e R2 mostram só o ID, a pergunta, a referência e a resposta, sem a versão e sem o F1.

## Resultados

R1 aprovou 9 de 12 saídas, 3/6 em A e 6/6 em B. A única falha crítica foi em A-CT02, que apresentou prazos de reembolso diferentes dos 10 dias úteis da política. A concordância entre R1 e R2 nas quatro saídas revisadas foi 4/4, antes de qualquer conversa. Nas outras oito saídas, a nota de R1 é a decisão final.
