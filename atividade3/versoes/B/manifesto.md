# Manifesto da versão B

Registro curto da configuração da versão B e dos limites de reprodução. A tag `av3-b` aponta para o commit que salva esta versão antes das execuções.

| Campo | Registro |
| :--- | :--- |
| Código e commit | Cherry Studio 2.0.13 (tag `v2.0.13` do repositório CherryHQ/cherry-studio, commit `6e3af1beac02cdc53dd2aba382cb6af7475dc669`), com atualização automática desligada. Captura em [`../../execucao/capturas/configuracao-versao.png`](../../execucao/capturas/configuracao-versao.png). O mesmo da versão A. |
| Mudança em relação à versão anterior | Somente o prompt: de "só a pergunta" (A) para o prompt estruturado com regras de fonte e de abstenção (B). |
| Prompt | [`prompt.md`](prompt.md) |
| Modelo e revisão | Gemini Flash-Lite Latest (alias `latest`, a revisão não é congelável) |
| Parâmetros | Os mesmos da versão A. Padrão do modelo no assistente do Cherry Studio (temperatura, Top-P e máximo de tokens desligados, valendo o padrão do modelo), saída em streaming, até 100 rodadas de chamada de ferramenta, histórico sem limite e gerenciamento de contexto global (compressão automática ligada). Base `AV3-Cherry` vinculada ao assistente: embedding `gemini-embedding-001` (Gemini Embedding 001), sem processamento de arquivo, sem rerank, Top K = 6, configurações avançadas no padrão. Sem prompt de sistema. |
| Fonte e contexto | `DOC-01`, `DOC-03` e `DOC-04`, em [`../../../base-de-conhecimento/`](../../../base-de-conhecimento/) |
| Casos e referências | [`../../casos.md`](../../casos.md) |
| Rubrica e limiar | [`../../plano-gqm.md`](../../plano-gqm.md) e [`../../rubrica.md`](../../rubrica.md). `tau = 0,5` |
| Data das execuções | 11/11/2026, a partir de 18h17 (ver [`../../execucao/README.md`](../../execucao/README.md)) |
| Resultados | Aprovação humana 6/6, nenhuma falha crítica, F1 médio 0,300 e 0/6 sinais automáticos positivos. Ver [`../../resultados/`](../../resultados/). |
| Limitações de reprodução | O alias `latest` pode mudar. Há uma execução por caso e versão. O modelo decide se consulta a base, e em algumas execuções não consultou (ver `execucao/README.md`). A base é reindexada ao ser recriada, o que pode mudar os trechos recuperados. Parte das respostas foi transcrita das capturas. |
