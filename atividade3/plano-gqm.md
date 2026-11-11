# Plano GQM da Atividade 3

> **Situação:** plano fixado antes das 12 execuções. Depois do commit deste arquivo, ninguém altera o plano, o tau, a rubrica nem o critério de decisão.

**Responsável:** Raphael Ferreira Portella Bacelar (bloco 1). Os casos e as referências estão em [`casos.md`](casos.md).

---

## 1. Objetivo (formato GQM)

| Elemento | Definição |
| :--- | :--- |
| Analisar | duas versões do prompt do fluxo de Base de Conhecimento do Cherry Studio, A (baseline) e B |
| Com o propósito de | comparar a qualidade das respostas e verificar se um sinal automático (F1 lexical) representa a adequação avaliada por pessoas |
| Do ponto de vista de | equipe de qualidade de software |
| No contexto de | seis casos sobre a política de reembolso e a garantia de uma empresa fictícia (Cereja Eletro), no Cherry Studio 2.0.13, com o modelo Gemini Flash-Lite Latest |

---

## 2. Perguntas e medidas

| Pergunta | Medida | Unidade | Fórmula e denominador | Limitação |
| :--- | :--- | :--- | :--- | :--- |
| **Q1.** A versão B atende melhor à tarefa? | **M2.** Taxa de aprovação humana, por versão | Proporção (x/6) | Saídas aprovadas ÷ 6. Aprovada = notas 2, 2, 2 em correção, relevância e suporte, e nenhuma falha crítica | Só seis casos. R1 decide sozinho 8 das 12 saídas. O cegamento é imperfeito. CT06 depende de CT01 |
| **Q2.** O sinal automático representa a adequação? | **M1.** F1 lexical, por saída e por versão (média e mediana) | Número de 0 a 1 | P = tokens em comum ÷ tokens da resposta. R = tokens em comum ÷ tokens da referência. F1 = 2 × P × R ÷ (P + R). Sem sobreposição ou resposta vazia, F1 = 0. Média e mediana por versão sobre 6 saídas | Mede só vocabulário, não verdade. Uma paráfrase correta pode ter F1 baixo, e trocar um número por outro mantém muitas palavras e muda o fato |
| **Q2.** O sinal automático representa a adequação? | **M3.** Concordância auto-humano | Proporção (x/12) | Saídas em que (F1 ≥ tau) coincide com a decisão humana final ÷ 12 | Depende do tau. As 12 saídas não são independentes (CT06 varia CT01, e A e B respondem às mesmas perguntas) |

---

## 3. Regras fixadas antes de rodar

### 3.1 Limiar tau

**tau = 0,5.** O sinal automático aprova a saída quando F1 ≥ 0,5. Valor didático previsto no enunciado, fixo e sem ajuste posterior.

**Justificativa:** o valor 0,5 foi mantido por ser o limiar didático indicado no enunciado e por ter leitura simples, a metade da sobreposição possível. Um limiar de 1,0 exigiria as mesmas palavras da referência, nem uma a mais, e reprovaria respostas corretas que apenas acrescentam palavras, o que impediria avaliar se o sinal representa a adequação. Sem conjunto de calibração próprio, e para evitar ajustar o limiar depois de ver os resultados, o valor foi fixado antes das execuções.

### 3.2 Cálculo do F1

Normalização Unicode NFC, `casefold`, tokens de palavras e interseção de multiconjuntos, como no código fornecido (`f1_lexical.py`). Resposta vazia ou falha de execução: F1 = 0, a saída é registrada e entra na conta, sem ser descartada. Referência sem tokens: o caso é corrigido antes de rodar.

### 3.3 Rubrica da avaliação humana

Cada saída recebe três notas de 0 a 2, e uma marca de falha crítica de 0 ou 1, com justificativa curta e evidência.

| Dimensão | 0 | 1 | 2 |
| :--- | :--- | :--- | :--- |
| Correção | Erro substantivo | Parcial ou erro menor | Sem erro identificado na referência |
| Relevância | Não atende | Atende parcialmente | Atende, inclusive abstenção correta |
| Suporte | Sem suporte | Suporte parcial | Afirmações sustentadas ou abstenção justificada |

### 3.4 Regra de falha crítica

A falha crítica vale 1 quando a saída:
1. afirma um número, prazo, valor ou condição que contradiz a fonte, de modo que mudaria a decisão de um cliente;
2. apresenta como vigente uma informação de documento desatualizado; ou
3. responde com conteúdo inventado onde a referência pede abstenção (CT05).

### 3.5 Critério de avanço e condição de bloqueio

- **Condição de bloqueio:** se a versão B tiver **uma ou mais falhas críticas**, B não avança, e a decisão é manter A ou revisar B.
- **Critério de avanço:** B é levada à próxima etapa se a aprovação humana de B for **maior** que a de A (x/6) e B não tiver nenhuma falha crítica.
- **Empate ou piora:** com aprovação igual ou menor e sem bloqueio, a decisão é manter A.
- A decisão é experimental. Não autoriza produção, e seis casos não demonstram risco zero.

### 3.6 Denominadores

Aprovação humana por versão: 6. Concordância auto-humano: 12. Concordância R1-R2: 4 (CT01 e CT05, nas duas versões), calculada antes do consenso.

---

## 4. Versões e ambiente

| Item | Valor |
| :--- | :--- |
| Versão A (baseline) | Prompt direto, `P-CIT-01` (`prompts/P1-direto.md`) |
| Versão B | Prompt estruturado com regras de uso de fonte e de abstenção, `P-CIT-02` (`prompts/P2-estruturado.md`). **É a única mudança.** |
| Aplicativo | Cherry Studio 2.0.13 |
| Modelo | Gemini Flash-Lite Latest, mesma chave e mesma configuração nas 12 execuções |
| Base de conhecimento | `DOC-01`, `DOC-03` e `DOC-04`. Ficam de fora o `DOC-02` (desatualizado, conflitaria com as referências) e o `DOC-05` (documento de teste de injeção) |
| Execução | Conversa nova a cada execução, uma execução por caso e versão |
