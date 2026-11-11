# Tentativas descartadas

Execuções feitas em 11/11/2026 que não entram nas 12 saídas porque não seguiram o protocolo de [`README.md`](README.md). Ficam registradas para transparência e não foram usadas no F1 nem na avaliação. Os textos abaixo foram transcritos das capturas de tela, salvo indicação, e podem ter perdido a formatação (negrito, listas e marcas de citação).

## Rodada 1 da versão A (descartada: conversa única)

Os casos foram enviados um após o outro na mesma conversa, e não em conversas novas. Assim cada resposta tinha no contexto as perguntas e respostas anteriores. Horários exibidos entre 18h06 e 18h07.

| Caso | Horário exibido | Base usada (indício na tela) | Resposta (transcrita da captura) |
| :--- | :--- | :--- | :--- |
| CT01 | 11/11 18:06 | Sim ("Processed", 1 citação, 10,8 mil tokens) | O prazo para desistir da compra (direito de arrependimento) é de até 7 (sete) dias corridos a contar da data de recebimento do produto, sem a necessidade de apresentar justificativa [1]. |
| CT02 | não exibido | Sim ("Processed", 1 citação) | Aprovada a devolução, o valor é reembolsado em até 10 (dez) dias úteis, utilizando a mesma forma de pagamento que foi escolhida na compra [1]. |
| CT03 | 11/11 18:07 | Sim ("Processed", 1 citação, 15,1 mil tokens) | Os eletrodomésticos de linha branca têm 12 meses (1 ano) de garantia total, que é a soma dos 90 dias de garantia legal com mais 9 meses de garantia contratual [1]. |
| CT04 | 11/11 18:07 | Sim ("Processed", 1 citação) | O frete da devolução (seja por arrependimento ou por defeito) é pago pela Cereja Eletro [1]. |
| CT05 | não exibido | Sim ("Processed", 2 citações) | Nos documentos disponíveis da empresa, não há menção a um número de telefone para atendimento. O contato de suporte e para abertura de chamados é feito por e-mail através do endereço suporte@cereja-ficticia.example [1][2]. |

O CT01 foi a primeira mensagem dessa conversa e não tinha contexto anterior, por isso foi mantido como a saída válida `A-CT01`. Os casos CT02 a CT05 da rodada 1 foram descartados e refeitos em conversas novas a partir de 18h11 (rodada 2), junto com o CT06. As saídas válidas estão em [`saidas-brutas/`](saidas-brutas/).
