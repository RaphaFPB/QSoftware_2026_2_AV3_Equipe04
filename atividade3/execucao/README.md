# Execução das 12 saídas

Registro das execuções dos seis casos em cada versão (A e B), com uma execução por caso e por versão.

## Regras

- Conversa nova a cada execução.
- Cherry Studio 2.0.13, Gemini Flash-Lite Latest e base de conhecimento só com `DOC-01`, `DOC-03` e `DOC-04`. Os documentos `DOC-02` e `DOC-05` não entram.
- Versão A: enviar somente a pergunta do caso. Versão B: enviar o texto de [`../versoes/B/prompt.md`](../versoes/B/prompt.md) com a pergunta do caso no final.
- Copiar a resposta completa, sem editar, e salvar uma captura com a pergunta, a resposta, as citações e o horário exibido.
- Uma saída vazia, com erro ou truncada é registrada como está, tem F1 = 0 e entra na conta. Não se executa de novo para melhorar o resultado.

## Arquivos esperados

Uma saída por arquivo em [`saidas-brutas/`](saidas-brutas/), com esta estrutura: caso, versão, data e horário exibido, pergunta enviada, resposta literal e nome da captura.

| Versão | Casos | Arquivos |
| :--- | :--- | :--- |
| A | CT01 a CT06 | `A-CT01.md` a `A-CT06.md` |
| B | CT01 a CT06 | `B-CT01.md` a `B-CT06.md` |

As capturas ficam em [`capturas/`](capturas/), com o mesmo nome da saída (por exemplo, `A-CT01.png`). Antes das 12 execuções, guardar também uma captura da configuração (versão do aplicativo e modelo) e da lista de documentos da base.

## Registro

- **Data e horários:** 11/11/2026. A primeira saída válida (A-CT01) foi às 18h06, a rodada válida da versão A começou às 18h11 e a primeira saída da versão B foi às 18h17. Os horários de B-CT02 a B-CT06 não aparecem nas capturas.
- **Configuração:** a mesma nas 12. Cherry Studio 2.0.13, Gemini Flash-Lite Latest, assistente padrão sem prompt de sistema [CONFERIR com o Vinícius] e com parâmetros padrão, base `AV3-Cherry` (DOC-01, DOC-03 e DOC-04, embedding `gemini-embedding-001`, Top K = 6, sem rerank) vinculada ao assistente. Cada execução foi feita em um tópico novo.
- **Saídas vazias ou com erro:** nenhuma.
- **Uso da base:** em A-CT02, A-CT04, A-CT06 e B-CT05 a tela não mostra "Processed" nem citações, e o consumo de tokens foi bem menor (de 3,1 mil a 6,8 mil, contra 10,8 mil a 37,6 mil nas demais). A base estava vinculada, mas no Cherry Studio ela funciona como uma ferramenta que o modelo decide chamar (até 100 rodadas de chamada de ferramenta, configuração padrão). Nesses quatro casos o modelo não chamou a ferramenta e respondeu sem consultar os documentos. As respostas de A-CT02, A-CT04 e A-CT06 trazem regras gerais do Código de Defesa do Consumidor, e não a política da Cereja Eletro.
- **Desvios do plano:** a primeira tentativa da versão A foi feita em uma única conversa. O CT01, que foi a primeira mensagem dessa conversa e não tinha contexto anterior, foi mantido. Os demais casos foram descartados e refeitos em tópicos novos (ver [`tentativas-descartadas.md`](tentativas-descartadas.md)). Parte das respostas foi transcrita das capturas de tela, e não copiada pelo botão do aplicativo, o que está indicado em cada arquivo.
