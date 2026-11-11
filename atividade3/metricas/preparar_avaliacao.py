#!/usr/bin/env python3
"""Lê as 12 saídas brutas, calcula o F1 lexical e monta as planilhas cegas de R1 e R2.

Uso, a partir da raiz do repositório:

    python atividade3/metricas/preparar_avaliacao.py

Gera:
- atividade3/resultados/entrada-f1.csv     (caso, versao, resposta, referencia)
- atividade3/resultados/f1-lexical.csv     (saída de f1_lexical.py com tau = 0,5)
- atividade3/avaliacao/planilha-R1.csv     (12 saídas, só ID, pergunta, referência e resposta)
- atividade3/avaliacao/planilha-R2.csv     (CT01 e CT05 nas duas versões, mesmos IDs)
- atividade3/avaliacao/chave-anonimizacao.csv  (liga ID a caso e versão; está no .gitignore)

A chave não é recriada se já existir, para não embaralhar de novo os IDs depois que as
planilhas foram entregues. Use --nova-chave só se as planilhas ainda não foram entregues.
"""

from __future__ import annotations

import argparse
import csv
import re
import secrets
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from f1_lexical import calculate  # noqa: E402

TAU = 0.5
CASOS = [f"CT0{i}" for i in range(1, 7)]
VERSOES = ["A", "B"]
CASOS_R2 = {"CT01", "CT05"}
MARCACAO = "[COLAR A RESPOSTA LITERAL AQUI]"
COLUNAS_NOTAS = [
    "correcao",
    "relevancia",
    "suporte",
    "falha_critica",
    "aprovada",
    "justificativa",
    "evidencia_textual",
]

RAIZ = Path(__file__).resolve().parent.parent  # pasta atividade3


def ler_casos() -> dict[str, dict[str, str]]:
    with (RAIZ / "casos.csv").open(encoding="utf-8-sig", newline="") as arquivo:
        return {linha["caso"]: linha for linha in csv.DictReader(arquivo)}


def campo_tabela(texto: str, nome: str) -> str:
    achado = re.search(rf"^\|\s*{re.escape(nome)}\s*\|\s*(.*?)\s*\|\s*$", texto, re.M)
    return achado.group(1) if achado else ""


def ler_resposta(caminho: Path, caso: str, versao: str) -> tuple[str, list[str]]:
    """Retorna a resposta literal e uma lista de avisos. Levanta ValueError se não preenchida."""
    texto = caminho.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    avisos = []
    if campo_tabela(texto, "Caso") != caso or campo_tabela(texto, "Versão") != versao:
        raise ValueError(f"{caminho.name}: caso ou versão na tabela não batem com o nome do arquivo")
    if "[PREENCHER" in campo_tabela(texto, "Data e horário exibido"):
        avisos.append(f"{caminho.name}: data e horário exibido não preenchidos")
    partes = texto.split("## Resposta literal", 1)
    if len(partes) != 2:
        raise ValueError(f"{caminho.name}: seção 'Resposta literal' não encontrada")
    bloco = re.search(r"^(`{3,}|~{3,})[^\n]*\n(.*?)^\1\s*$", partes[1], re.S | re.M)
    if not bloco:
        raise ValueError(f"{caminho.name}: bloco da resposta não encontrado (cercas ```` ausentes)")
    resposta = bloco.group(2).rstrip("\n")
    if MARCACAO in resposta:
        raise ValueError(f"{caminho.name}: resposta ainda não colada")
    if not resposta.strip():
        avisos.append(f"{caminho.name}: resposta vazia (F1 = 0, entra na conta)")
    return resposta, avisos


def gravar_csv(caminho: Path, colunas: list[str], linhas: list[dict]) -> None:
    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas, lineterminator="\n")
        escritor.writeheader()
        escritor.writerows(linhas)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--nova-chave", action="store_true", help="recria a chave de anonimização")
    args = parser.parse_args()

    casos = ler_casos()
    saidas, erros, avisos = [], [], []
    for versao in VERSOES:
        for caso in CASOS:
            caminho = RAIZ / "execucao" / "saidas-brutas" / f"{versao}-{caso}.md"
            if not caminho.exists():
                erros.append(f"{caminho.name}: arquivo ausente")
                continue
            try:
                resposta, avisos_saida = ler_resposta(caminho, caso, versao)
            except ValueError as erro:
                erros.append(str(erro))
                continue
            avisos += avisos_saida
            saidas.append({"caso": caso, "versao": versao, "resposta": resposta})

    for aviso in avisos:
        print(f"Aviso: {aviso}", file=sys.stderr)
    if erros:
        for erro in erros:
            print(f"Erro: {erro}", file=sys.stderr)
        print("Nada foi gerado. Corrija as saídas e rode de novo.", file=sys.stderr)
        return 2

    # F1 lexical, com o mesmo script descrito em metricas/README.md
    entrada = [
        {**s, "referencia": casos[s["caso"]]["referencia"]} for s in saidas
    ]
    pasta_resultados = RAIZ / "resultados"
    gravar_csv(pasta_resultados / "entrada-f1.csv", ["caso", "versao", "resposta", "referencia"], entrada)
    with (pasta_resultados / "entrada-f1.csv").open(encoding="utf-8", newline="") as ent, (
        pasta_resultados / "f1-lexical.csv"
    ).open("w", encoding="utf-8", newline="") as sai:
        calculate(ent, sai, TAU)

    # Chave de anonimização
    caminho_chave = RAIZ / "avaliacao" / "chave-anonimizacao.csv"
    if caminho_chave.exists() and not args.nova_chave:
        with caminho_chave.open(encoding="utf-8", newline="") as arquivo:
            chave = list(csv.DictReader(arquivo))
        print(f"Chave existente mantida: {caminho_chave}")
    else:
        ids = [f"S{i:02d}" for i in range(1, 13)]
        ordem = list(range(12))
        secrets.SystemRandom().shuffle(ordem)
        chave = [
            {"id_anonimo": ids[posicao], "caso": s["caso"], "versao": s["versao"]}
            for posicao, s in zip(ordem, saidas)
        ]
        chave.sort(key=lambda linha: linha["id_anonimo"])
        gravar_csv(caminho_chave, ["id_anonimo", "caso", "versao"], chave)
        print(f"Chave nova gravada (não publicar antes do fim das avaliações): {caminho_chave}")

    por_caso_versao = {(s["caso"], s["versao"]): s["resposta"] for s in saidas}
    colunas_planilha = ["id_anonimo", "pergunta", "referencia", "resposta"] + COLUNAS_NOTAS
    planilha_r1, planilha_r2 = [], []
    for linha in chave:  # já em ordem de ID, que é aleatória em relação a caso e versão
        caso = casos[linha["caso"]]
        registro = {
            "id_anonimo": linha["id_anonimo"],
            "pergunta": caso["pergunta"],
            "referencia": caso["referencia"],
            "resposta": por_caso_versao[(linha["caso"], linha["versao"])],
            **{coluna: "" for coluna in COLUNAS_NOTAS},
        }
        planilha_r1.append(registro)
        if linha["caso"] in CASOS_R2:
            planilha_r2.append(registro)
    gravar_csv(RAIZ / "avaliacao" / "planilha-R1.csv", colunas_planilha, planilha_r1)
    gravar_csv(RAIZ / "avaliacao" / "planilha-R2.csv", colunas_planilha, planilha_r2)

    print("Gerados: resultados/entrada-f1.csv, resultados/f1-lexical.csv,")
    print("         avaliacao/planilha-R1.csv (12 linhas), avaliacao/planilha-R2.csv (4 linhas)")
    print("Entregar a R1 e R2 só as planilhas. Não mostrar o F1 nem a chave.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
