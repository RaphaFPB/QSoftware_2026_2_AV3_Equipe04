# Decisão experimental

Conclusão descritiva sobre as versões A e B, a partir dos resultados em [`../resultados/`](../resultados/) e da regra fixada em [`../plano-gqm.md`](../plano-gqm.md).

## Regra de decisão

- **Condição de bloqueio:** se B tiver uma ou mais falhas críticas, B não avança, e a decisão é manter A ou revisar B.
- **Critério de avanço:** B é levada à próxima etapa se a aprovação humana de B for maior que a de A (x/6) e B não tiver nenhuma falha crítica.
- **Empate ou piora:** com aprovação igual ou menor e sem bloqueio, a decisão é manter A.

## Resultados considerados

| Campo | Valor |
| :--- | :--- |
| Aprovação humana de A (x/6) | 3/6 |
| Aprovação humana de B (x/6) | 6/6 |
| Falhas críticas em B | 0 |
| Critério de avanço atendido? | Sim, 6/6 é maior que 3/6 e B não tem falha crítica |
| Condição de bloqueio acionada? | Não |

## Decisão

**Levar B para a próxima etapa.** Pela regra fixada antes do teste, B avança, porque a aprovação humana de B (6/6) foi maior que a de A (3/6) e B não teve falha crítica. A melhora apareceu na avaliação humana, e não na métrica automática, que quase não mudou (F1 médio de 0,249 em A e 0,300 em B). A decisão é experimental e não autoriza uso em produção. Seis casos com uma execução cada não demonstram risco zero. A próxima etapa seria repetir o teste com mais casos e mais de uma execução por caso.

## Limitações

- Só seis casos, com uma execução por caso e versão, e o CT06 depende do CT01.
- O modelo usa o alias `latest`, que não congela a revisão, e decide sozinho se consulta a base. Em quatro execuções ele não consultou, três delas em A.
- R1 decide sozinho oito das 12 saídas, e R2 revisou só CT01 e CT05.
- O cegamento foi parcial. As respostas de B terminam com "Fonte:" e as saídas brutas no repositório têm a versão no nome.
- O F1 com referências curtas penalizou respostas longas e paráfrases, e teve concordância de 4/12 com a decisão humana.
- Parte dos textos foi transcrita de capturas de tela, e a primeira tentativa da versão A foi descartada por ter sido feita numa conversa única.

## Acompanhamento

Acompanhar, por versão, a aprovação humana (x/6), as falhas críticas e se a resposta consultou a base e citou a fonte. Qualquer falha crítica em B bloqueia B até revisão. Para voltar a A, restaurar o prompt da tag `av3-a` com o mesmo aplicativo, modelo e base, registrar a data e o motivo e rodar os seis casos de novo para conferir. Os detalhes estão em [`../ciclo-de-vida/ciclo-de-vida.md`](../ciclo-de-vida/ciclo-de-vida.md).
