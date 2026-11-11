# Manifesto da versão B

Registro curto da configuração da versão B e dos limites de reprodução. A tag `av3-b` aponta para o commit que salva esta versão antes das execuções.

| Campo | Registro |
| :--- | :--- |
| Código e commit | Cherry Studio 2.0.13. [PREENCHER: commit do Cherry Studio usado, o mesmo da versão A] |
| Mudança em relação à versão anterior | Somente o prompt: de "só a pergunta" (A) para o prompt estruturado com regras de fonte e de abstenção (B). |
| Prompt | [`prompt.md`](prompt.md) |
| Modelo e revisão | Gemini Flash-Lite Latest (alias `latest`, a revisão não é congelável) |
| Parâmetros | [PREENCHER: os mesmos da versão A] |
| Fonte e contexto | `DOC-01`, `DOC-03` e `DOC-04`, em [`../../../base-de-conhecimento/`](../../../base-de-conhecimento/) |
| Casos e referências | [`../../casos.md`](../../casos.md) |
| Rubrica e limiar | [`../../plano-gqm.md`](../../plano-gqm.md) e [`../../rubrica.md`](../../rubrica.md). `tau = 0,5` |
| Data das execuções | [PREENCHER] |
| Resultados | [PREENCHER depois das avaliações: aprovação humana x/6 e F1 médio] |
| Limitações de reprodução | O alias `latest` pode mudar. Há uma execução por caso e versão. [PREENCHER: outras] |
