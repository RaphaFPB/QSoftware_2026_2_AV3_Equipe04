# Prompt da versão B

**ID:** `P-CIT-02`. Prompt estruturado, com regras de uso de fonte e de abstenção, adaptado do `P2` da Atividade 2 ([`../../../prompts/P2-estruturado.md`](../../../prompts/P2-estruturado.md)). O `P2` original tinha a pergunta do CT01 escrita no texto, e aqui ela é trocada por `[pergunta do caso]` para servir às seis perguntas.

## Texto enviado em cada execução

Este texto, com `[pergunta do caso]` substituída pela pergunta de cada caso (em [`../../casos.md`](../../casos.md)):

```text
Objetivo: responder à pergunta abaixo usando as fontes recuperadas pela Base de Conhecimento.

Contexto: use os documentos recuperados pelo Cherry Studio.

Regras:
1. Use somente informações encontradas nos documentos; não invente dados.
2. Cite o nome ou ID do documento que sustenta a resposta.
3. Se os documentos divergirem, explicite a divergência e identifique as versões e datas apresentadas, sem ocultar a versão antiga.
4. Se não houver informação suficiente, diga: "Não encontrei essa informação nos documentos."

Formato: responda em português do Brasil, em texto curto, indicando a resposta e a(s) fonte(s). Não use JSON.

Pergunta: [pergunta do caso]
```

## Condições

É a única mudança em relação à versão A. As demais condições são as mesmas:

- Conversa nova a cada execução.
- Base de conhecimento com `DOC-01`, `DOC-03` e `DOC-04`.
- Cherry Studio 2.0.13 e Gemini Flash-Lite Latest.
