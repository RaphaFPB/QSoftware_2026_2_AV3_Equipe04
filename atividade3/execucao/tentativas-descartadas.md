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

## Rodada 2 da versão A (descartada: base de conhecimento desligada em parte dos casos)

Casos enviados em conversas novas, mas no CT02 e no CT04 a tela não mostra "Processed" nem citações, e o consumo foi de cerca de 3 mil tokens, contra cerca de 10,8 mil quando a base é usada. As respostas são genéricas e não mencionam a Cereja Eletro. A base não foi aplicada nesses tópicos novos. A rodada inteira foi refeita com a base fixada nas configurações do assistente.

| Caso | Horário exibido | Base usada (indício na tela) |
| :--- | :--- | :--- |
| CT02 | 11/11 18:11 | Não (sem "Processed", sem citação, 3,1 mil tokens) |
| CT03 | 11/11 18:12 | Sim ("Processed", 1 citação, 10,8 mil tokens) |
| CT04 | 11/11 18:12 | Não (sem citação, 3,4 mil tokens) |

### CT02 (transcrita da captura)

```text
O prazo para o reembolso ser efetuado após a aprovação da devolução varia de acordo com a forma de pagamento utilizada na compra. Veja os prazos mais comuns:

- Cartão de Crédito: O estorno é solicitado imediatamente após a aprovação, mas o valor pode ser creditado em até 1 a 2 faturas subsequentes, dependendo da data de fechamento da sua fatura e dos procedimentos da administradora do cartão.
- Pix / Boleto Bancário / Carteira Digital: O reembolso geralmente é feito em conta corrente ou PIX em um prazo que costuma variar de 1 a 7 dias úteis após a conclusão da análise/aprovação.

Nota: Como cada loja, marketplace ou plataforma possui políticas próprias, vale a pena conferir os termos de troca e devolução específicos do site ou aplicativo onde você realizou a compra para ter a confirmação exata do prazo.
```

### CT03 (transcrita da captura)

```text
Os eletrodomésticos de linha branca têm garantia total de 12 meses, que é a soma de 90 dias de garantia legal com mais 9 meses de garantia contratual [1].
```

### CT04 (texto copiado da tela e enviado pela equipe)

```text
A responsabilidade pelo pagamento do frete da devolução depende do motivo da devolução e do tipo de compra (loja física, internet, defeito ou arrependimento), conforme estabelecido pelo Código de Defesa do Consumidor (CDC) no Brasil:
1. Arrependimento ou Desistência (Compras pela Internet)
Se você comprou um produto pela internet, telefone ou catálogo e se arrependeu no prazo de até 7 dias corridos após o recebimento (o chamado "direito de arrependimento"):

* Quem paga: O vendedor/loja é totalmente responsável pelos custos de postagem e logística reversa. Você não deve pagar nada pelo frete de devolução.

2. Produto com Defeito ou Vício
Se o produto apresentou defeito de fabricação (seja comprado na internet ou em loja física):

* Quem paga: O fornecedor/fabricante é responsável por todos os custos de envio para a troca ou devolução. A lei determina que o consumidor não pode ter nenhum prejuízo financeiro por receber um produto defeituoso.

3. Produto Divergente ou Errado (Produto errado enviado pela loja)
Se a loja enviou um modelo, cor ou tamanho diferente do que você comprou:

* Quem paga: O vendedor arca com o frete de devolução e reenvio do produto correto.

4. Troca por Tamanho, Cor ou Gosto (Sem defeito, em Loja Física)
Se você comprou um produto em uma loja física (onde é possível ver e testar o produto antes) e quer trocar apenas porque não serviu ou não gostou:

* Quem paga: Por lei, lojas físicas não são obrigadas a realizar trocas por motivo de cor, tamanho ou gosto (a não ser que tenham prometido isso no ato da compra). Se a loja aceitar trocar por gentileza, as regras de frete ou deslocamento ficam a critério do estabelecimento.

Resumo prático para compras online (que é a dúvida mais comum):
Seja por arrependimento (dentro dos 7 dias) ou por defeito, o frete da devolução é sempre por conta da loja.
```
