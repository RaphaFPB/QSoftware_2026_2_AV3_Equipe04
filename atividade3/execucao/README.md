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

[PREENCHER: data e hora das execuções, se a configuração foi a mesma nas 12, saídas vazias ou com erro, e desvios do plano.]
