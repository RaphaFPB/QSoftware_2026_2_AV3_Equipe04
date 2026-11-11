# Prompt P2 — Estruturado

> **Propósito:** Registrar a especificação e versionamento do Prompt Estruturado (P2), decompondo o comando em seções claras de Objetivo, Contexto, Restrições e Formato.

---

## 1. Tarefa
Especificar o prompt estruturado com guardrails explícitos de delimitação de escopo, regras de não-alucinação e formatação padronizada para verificação de citações.

---

## 2. Análise do Artefato

### 2.1 Metadados do Prompt
- **ID do Prompt:** `P-CIT-02`
- **Nome:** Prompt Estruturado
- **Técnica:** Instrução Estruturada com Guardrails
- **Versão:** 1.0.0

### 2.2 Seções do Prompt

#### Objetivo
Responder qual é o prazo para desistir da compra usando as fontes recuperadas pela Base de Conhecimento.

#### Contexto
O contexto será fornecido pelo Cherry Studio. Na primeira condição, a base selecionada contém somente o `DOC-01`. Na segunda, contém o `DOC-01` e o `DOC-02`.

#### Restrições
1. Use somente informações encontradas nos documentos recuperados; não invente dados.
2. Cite o nome ou ID do documento que sustenta a resposta.
3. Se os documentos divergirem, explicite a divergência e identifique as versões e datas apresentadas, sem ocultar a versão antiga.
4. Se não houver informação suficiente, diga: "Não encontrei essa informação nos documentos."

#### Formato de Saída
Responda em português do Brasil, em texto curto, indicando a resposta e a(s) fonte(s). Não é necessário JSON neste experimento.

### 2.3 Conteúdo do Prompt (Texto Integral)
```text
Objetivo: responder qual é o prazo para desistir da compra usando as fontes recuperadas pela Base de Conhecimento.

Contexto: use os documentos recuperados pelo Cherry Studio. A base selecionada contém o contexto definido para esta execução.

Regras:
1. Use somente informações encontradas nos documentos; não invente dados.
2. Cite o nome ou ID do documento que sustenta a resposta.
3. Se os documentos divergirem, explicite a divergência e identifique as versões e datas apresentadas, sem ocultar a versão antiga.
4. Se não houver informação suficiente, diga: "Não encontrei essa informação nos documentos."

Formato: responda em português do Brasil, em texto curto, indicando a resposta e a(s) fonte(s). Não use JSON.

Pergunta: Qual é o prazo para desistir da compra?
```

---

## 3. Resultados
- **Pergunta escolhida para as seis execuções:** "Qual é o prazo para desistir da compra?"
- **Cenário com contexto correto:** selecionar na Base de Conhecimento somente o `DOC-01`.
- **Cenário conflitante:** selecionar uma base com `DOC-01` e `DOC-02`.
- **Importante:** manter a pergunta e as demais configurações do Cherry Studio iguais nas seis execuções. O contexto deve ser fornecido pela Base de Conhecimento selecionada no aplicativo, não copiado manualmente para o prompt.
- **Condições de Teste Avaliadas:**
  - **Condição A — somente `DOC-01`:** “O prazo para desistir da compra é de até 7 (sete) dias corridos a partir do recebimento do produto, sem precisar justificar. Fonte: `DOC-01-politica-reembolso-v2.md`.” Avaliação: fato correto e documento citado.
  - **Condição B — `DOC-01` + `DOC-02`:** “Há uma divergência entre os documentos encontrados na base:
    - Versão atual (Versão 2.0, vigente desde 01/03/2026): O prazo para desistir da compra é de até 7 (sete) dias corridos a partir do recebimento do produto, sem precisar justificar 1. (Fonte: `DOC-01-politica-reembolso-v2.md`).
    - Versão antiga (Versão 1.0, publicada em 10/05/2024): O prazo informado era de até 15 (quinze) dias corridos a partir do recebimento do produto 2. (Fonte: `DOC-02-politica-reembolso-v1-desatualizada.md`).”
    Avaliação: identificou corretamente a divergência e as fontes. O integrante informou os trechos de apoio: DOC-01 — “O cliente pode desistir da compra em até 7 (sete) dias corridos a partir do recebimento do produto, sem precisar justificar”; DOC-02 — “O cliente pode desistir da compra em até 15 (quinze) dias corridos a partir do recebimento do produto”.
- **Síntese do P2:** resposta correta e com fontes nas duas condições; na condição conflitante, os trechos informados sustentam os dois prazos.
- **Registro:** resultados transcritos a partir das respostas enviadas pelo integrante. Horários informados: 12:08 (A) e 12:16 (B); latências não informadas.
