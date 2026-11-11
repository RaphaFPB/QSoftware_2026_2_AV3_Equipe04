# Manifesto da versão A

Registro curto da configuração da versão A (baseline) e dos limites de reprodução. A tag `av3-a` aponta para o commit que salva esta versão antes das execuções.

| Campo | Registro |
| :--- | :--- |
| Código e commit | Cherry Studio 2.0.13. [CONFERIR: commit `6e3af1beac02cdc53dd2aba382cb6af7475dc669`, registrado pela equipe para a 2.0.13] |
| Mudança em relação à versão anterior | Baseline. Prompt direto: só a pergunta do caso. |
| Prompt | [`prompt.md`](prompt.md) |
| Modelo e revisão | Gemini Flash-Lite Latest (alias `latest`, a revisão não é congelável) |
| Parâmetros | Padrão do modelo no assistente do Cherry Studio (temperatura, Top-P e máximo de tokens desligados, valendo o padrão do modelo), saída em streaming, até 100 rodadas de chamada de ferramenta, histórico sem limite e gerenciamento de contexto global (compressão automática ligada). Base `AV3-Cherry` vinculada ao assistente: embedding `gemini-embedding-001` (Gemini Embedding 001), sem processamento de arquivo, sem rerank, Top K = 6, configurações avançadas no padrão. Sem prompt de sistema. |
| Fonte e contexto | `DOC-01`, `DOC-03` e `DOC-04`, em [`../../../base-de-conhecimento/`](../../../base-de-conhecimento/) |
| Casos e referências | [`../../casos.md`](../../casos.md) |
| Rubrica e limiar | [`../../plano-gqm.md`](../../plano-gqm.md) e [`../../rubrica.md`](../../rubrica.md). `tau = 0,5` |
| Data das execuções | 11/11/2026, a partir de 18h06 (ver [`../../execucao/README.md`](../../execucao/README.md)) |
| Resultados | [PREENCHER depois das avaliações: aprovação humana x/6 e F1 médio] |
| Limitações de reprodução | O alias `latest` pode mudar. Há uma execução por caso e versão. O modelo decide se consulta a base, e em algumas execuções não consultou (ver `execucao/README.md`). A base é reindexada ao ser recriada, o que pode mudar os trechos recuperados. Parte das respostas foi transcrita das capturas. |
