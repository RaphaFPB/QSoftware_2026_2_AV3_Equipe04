# Prompt P1 — Direto

> **Propósito:** Registrar a especificação e versionamento do Prompt Direto (P1), baseado em instruções sucintas e diretas sem formatação complexa.

---

## 1. Tarefa
Definir o prompt de linha de base (baseline) com instrução direta, servindo como referencial comparativo para os prompts estruturados e com poucos exemplos.

---

## 2. Análise do Artefato

### 2.1 Metadados do Prompt
- **ID do Prompt:** `P-CIT-01`
- **Nome:** Prompt Direto
- **Técnica:** Zero-Shot Direto
- **Versão:** 1.0.0
- **Objetivo:** Responder à pergunta do usuário utilizando a base de conhecimento do Cherry Studio sem restrições estritas de formatação.

### 2.2 Conteúdo do Prompt
```text
Qual é o prazo para desistir da compra?
```

---

## 3. Resultados
- **Pergunta escolhida para as seis execuções:** "Qual é o prazo para desistir da compra?"
- **Cenário com contexto correto:** selecionar na Base de Conhecimento somente o `DOC-01`.
- **Cenário conflitante:** selecionar uma base com `DOC-01` e `DOC-02`.
- **Importante:** manter a pergunta e as demais configurações do Cherry Studio iguais nas seis execuções. O contexto deve ser fornecido pela Base de Conhecimento selecionada no aplicativo, não copiado manualmente para o prompt.
- **Condições de Teste Avaliadas:**
  - **Condição A — somente `DOC-01`:** “O prazo para desistir da compra é de até 7 (sete) dias corridos a partir do recebimento do produto, sem precisar justificar.” Avaliação: prazo correto; não houve citação explícita no texto enviado.
  - **Condição B — `DOC-01` + `DOC-02`:** “Há uma divergência entre os documentos encontrados na base:
    - Versão atual (Versão 2.0, vigente desde 01/03/2026): O prazo para desistir da compra é de até 7 (sete) dias corridos a partir do recebimento do produto, sem precisar justificar 1. (Fonte: `DOC-01-politica-reembolso-v2.md`).
    - Versão antiga (Versão 1.0, publicada em 10/05/2024): O prazo informado era de até 15 (quinze) dias corridos a partir do recebimento do produto 2. (Fonte: `DOC-02-politica-reembolso-v1-desatualizada.md`).”
    Avaliação: identificou corretamente a divergência, os prazos, as versões e as fontes. O integrante não informou os trechos recuperados.
- **Síntese do P1:** acertou o fato nas duas condições e tratou o conflito; a resposta na Condição A não trouxe fonte explícita, ficando menos rastreável que as respostas de P2 e P3 nessa condição.
- **Registro:** resultados transcritos a partir das respostas enviadas pelo integrante. Horário da execução B informado: 12:16; horário da execução A e latências não informados.
