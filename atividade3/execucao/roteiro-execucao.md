# Roteiro das 12 execuções

Mensagens prontas para colar no Cherry Studio, geradas a partir de [`../casos.csv`](../casos.csv) e de [`../versoes/B/prompt.md`](../versoes/B/prompt.md). As regras estão em [`README.md`](README.md).

## Antes de começar

- [ ] Captura da configuração: versão do Cherry Studio (2.0.13), modelo (Gemini Flash-Lite Latest) e parâmetros. Salvar como `capturas/configuracao.png`.
- [ ] Captura da base de conhecimento com só `DOC-01`, `DOC-03` e `DOC-04`. Salvar como `capturas/base-de-conhecimento.png`.
- [ ] Anotar o commit ou build do Cherry Studio e os parâmetros do modelo, para os manifestos.

## Para cada uma das 12 execuções

1. Abrir uma conversa nova, com a base de conhecimento ligada.
2. Colar a mensagem do bloco abaixo, exatamente como está, e enviar.
3. Abrir o arquivo indicado em `saidas-brutas/` e preencher a data e o horário exibidos e a resposta literal, sem editar nada da resposta. Se houver citações ou fontes exibidas, copiar também.
4. Salvar a captura com o mesmo nome do arquivo em `capturas/` (por exemplo, `A-CT01.png`).
5. Marcar a caixa da execução.

Saída vazia, erro ou resposta truncada é registrada como veio. Não se executa de novo.

## A-CT01

- [ ] Executado. Arquivo: [`saidas-brutas/A-CT01.md`](saidas-brutas/A-CT01.md). Captura: `capturas/A-CT01.png`.

```text
Qual é o prazo para desistir da compra?
```

## A-CT02

- [ ] Executado. Arquivo: [`saidas-brutas/A-CT02.md`](saidas-brutas/A-CT02.md). Captura: `capturas/A-CT02.png`.

```text
Em quanto tempo o reembolso é feito depois que a devolução é aprovada?
```

## A-CT03

- [ ] Executado. Arquivo: [`saidas-brutas/A-CT03.md`](saidas-brutas/A-CT03.md). Captura: `capturas/A-CT03.png`.

```text
Quanto tempo de garantia total têm os eletrodomésticos de linha branca?
```

## A-CT04

- [ ] Executado. Arquivo: [`saidas-brutas/A-CT04.md`](saidas-brutas/A-CT04.md). Captura: `capturas/A-CT04.png`.

```text
Quem paga o frete da devolução?
```

## A-CT05

- [ ] Executado. Arquivo: [`saidas-brutas/A-CT05.md`](saidas-brutas/A-CT05.md). Captura: `capturas/A-CT05.png`.

```text
Qual é o telefone da central de atendimento?
```

## A-CT06

- [ ] Executado. Arquivo: [`saidas-brutas/A-CT06.md`](saidas-brutas/A-CT06.md). Captura: `capturas/A-CT06.png`.

```text
Até quando posso desistir de uma compra que fiz?
```

## B-CT01

- [ ] Executado. Arquivo: [`saidas-brutas/B-CT01.md`](saidas-brutas/B-CT01.md). Captura: `capturas/B-CT01.png`.

```text
Objetivo: responder à pergunta abaixo usando as fontes recuperadas pela Base de Conhecimento.

Contexto: use os documentos recuperados pelo Cherry Studio.

Regras:
1. Use somente informações encontradas nos documentos; não invente dados.
2. Cite o nome ou ID do documento que sustenta a resposta.
3. Se os documentos divergirem, explicite a divergência e identifique as versões e datas apresentadas, sem ocultar a versão antiga.
4. Se não houver informação suficiente, diga: "Não encontrei essa informação nos documentos."

Formato: responda em português do Brasil, em texto curto, indicando a resposta e a(s) fonte(s). Não use JSON.

Pergunta: Qual é o prazo para desistir da compra?
```

## B-CT02

- [ ] Executado. Arquivo: [`saidas-brutas/B-CT02.md`](saidas-brutas/B-CT02.md). Captura: `capturas/B-CT02.png`.

```text
Objetivo: responder à pergunta abaixo usando as fontes recuperadas pela Base de Conhecimento.

Contexto: use os documentos recuperados pelo Cherry Studio.

Regras:
1. Use somente informações encontradas nos documentos; não invente dados.
2. Cite o nome ou ID do documento que sustenta a resposta.
3. Se os documentos divergirem, explicite a divergência e identifique as versões e datas apresentadas, sem ocultar a versão antiga.
4. Se não houver informação suficiente, diga: "Não encontrei essa informação nos documentos."

Formato: responda em português do Brasil, em texto curto, indicando a resposta e a(s) fonte(s). Não use JSON.

Pergunta: Em quanto tempo o reembolso é feito depois que a devolução é aprovada?
```

## B-CT03

- [ ] Executado. Arquivo: [`saidas-brutas/B-CT03.md`](saidas-brutas/B-CT03.md). Captura: `capturas/B-CT03.png`.

```text
Objetivo: responder à pergunta abaixo usando as fontes recuperadas pela Base de Conhecimento.

Contexto: use os documentos recuperados pelo Cherry Studio.

Regras:
1. Use somente informações encontradas nos documentos; não invente dados.
2. Cite o nome ou ID do documento que sustenta a resposta.
3. Se os documentos divergirem, explicite a divergência e identifique as versões e datas apresentadas, sem ocultar a versão antiga.
4. Se não houver informação suficiente, diga: "Não encontrei essa informação nos documentos."

Formato: responda em português do Brasil, em texto curto, indicando a resposta e a(s) fonte(s). Não use JSON.

Pergunta: Quanto tempo de garantia total têm os eletrodomésticos de linha branca?
```

## B-CT04

- [ ] Executado. Arquivo: [`saidas-brutas/B-CT04.md`](saidas-brutas/B-CT04.md). Captura: `capturas/B-CT04.png`.

```text
Objetivo: responder à pergunta abaixo usando as fontes recuperadas pela Base de Conhecimento.

Contexto: use os documentos recuperados pelo Cherry Studio.

Regras:
1. Use somente informações encontradas nos documentos; não invente dados.
2. Cite o nome ou ID do documento que sustenta a resposta.
3. Se os documentos divergirem, explicite a divergência e identifique as versões e datas apresentadas, sem ocultar a versão antiga.
4. Se não houver informação suficiente, diga: "Não encontrei essa informação nos documentos."

Formato: responda em português do Brasil, em texto curto, indicando a resposta e a(s) fonte(s). Não use JSON.

Pergunta: Quem paga o frete da devolução?
```

## B-CT05

- [ ] Executado. Arquivo: [`saidas-brutas/B-CT05.md`](saidas-brutas/B-CT05.md). Captura: `capturas/B-CT05.png`.

```text
Objetivo: responder à pergunta abaixo usando as fontes recuperadas pela Base de Conhecimento.

Contexto: use os documentos recuperados pelo Cherry Studio.

Regras:
1. Use somente informações encontradas nos documentos; não invente dados.
2. Cite o nome ou ID do documento que sustenta a resposta.
3. Se os documentos divergirem, explicite a divergência e identifique as versões e datas apresentadas, sem ocultar a versão antiga.
4. Se não houver informação suficiente, diga: "Não encontrei essa informação nos documentos."

Formato: responda em português do Brasil, em texto curto, indicando a resposta e a(s) fonte(s). Não use JSON.

Pergunta: Qual é o telefone da central de atendimento?
```

## B-CT06

- [ ] Executado. Arquivo: [`saidas-brutas/B-CT06.md`](saidas-brutas/B-CT06.md). Captura: `capturas/B-CT06.png`.

```text
Objetivo: responder à pergunta abaixo usando as fontes recuperadas pela Base de Conhecimento.

Contexto: use os documentos recuperados pelo Cherry Studio.

Regras:
1. Use somente informações encontradas nos documentos; não invente dados.
2. Cite o nome ou ID do documento que sustenta a resposta.
3. Se os documentos divergirem, explicite a divergência e identifique as versões e datas apresentadas, sem ocultar a versão antiga.
4. Se não houver informação suficiente, diga: "Não encontrei essa informação nos documentos."

Formato: responda em português do Brasil, em texto curto, indicando a resposta e a(s) fonte(s). Não use JSON.

Pergunta: Até quando posso desistir de uma compra que fiz?
```
