#!/usr/bin/env python3
"""Junta F1, R1, R2 e consenso e gera a tabela consolidada, o resumo e o gráfico.

Uso, a partir da raiz do repositório, depois que R1 e R2 terminarem:

    python atividade3/metricas/consolidar.py

Lê:
- atividade3/resultados/f1-lexical.csv
- atividade3/avaliacao/chave-anonimizacao.csv
- atividade3/avaliacao/r1.csv  (12 linhas)
- atividade3/avaliacao/r2.csv  (4 linhas: CT01 e CT05 em A e B)
- atividade3/avaliacao/consenso.csv  (opcional; só para as saídas em que R1 e R2 divergiram)
  colunas: id_anonimo,correcao,relevancia,suporte,falha_critica,justificativa

Gera:
- atividade3/resultados/tabela-consolidada.csv
- atividade3/resultados/resumo-automatico.md
- atividade3/resultados/grafico-resultados.png (ou .svg se o matplotlib não estiver instalado)

Regras aplicadas (plano-gqm.md e rubrica.md): aprovada = três notas 2 e falha crítica 0.
Nas oito saídas sem R2, a decisão final é a de R1. Nas quatro com R2, se R1 e R2 têm a mesma
decisão e a mesma falha crítica, vale essa decisão; se não, vale o consenso.csv.
O critério de avanço é só calculado aqui. A decisão experimental é escrita pela equipe.
"""

from __future__ import annotations

import csv
import statistics
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # pasta atividade3
CASOS = [f"CT0{i}" for i in range(1, 7)]
VERSOES = ["A", "B"]
CASOS_R2 = {"CT01", "CT05"}
NOTAS = ["correcao", "relevancia", "suporte"]


class ErroDados(Exception):
    pass


def ler_csv(caminho: Path, obrigatorio: bool = True) -> list[dict[str, str]]:
    if not caminho.exists():
        if obrigatorio:
            raise ErroDados(f"arquivo ausente: {caminho.relative_to(RAIZ.parent)}")
        return []
    with caminho.open(encoding="utf-8-sig", newline="") as arquivo:
        return [
            {chave.strip(): (valor or "").strip() for chave, valor in linha.items() if chave}
            for linha in csv.DictReader(arquivo)
        ]


def notas_validas(linha: dict[str, str], origem: str) -> dict[str, int]:
    resultado = {}
    for campo, maximo in [("correcao", 2), ("relevancia", 2), ("suporte", 2), ("falha_critica", 1)]:
        valor = linha.get(campo, "")
        if valor not in {str(n) for n in range(maximo + 1)}:
            raise ErroDados(f"{origem}, {linha.get('id_anonimo')}: '{campo}' inválido ({valor!r})")
        resultado[campo] = int(valor)
    resultado["aprovada"] = int(all(resultado[n] == 2 for n in NOTAS) and resultado["falha_critica"] == 0)
    informada = linha.get("aprovada", "")
    if informada not in ("", "0", "1"):
        raise ErroDados(f"{origem}, {linha.get('id_anonimo')}: 'aprovada' deve ser 0 ou 1")
    if informada != "" and int(informada) != resultado["aprovada"]:
        print(
            f"Aviso: {origem}, {linha.get('id_anonimo')}: 'aprovada' = {informada}, mas pela regra "
            f"seria {resultado['aprovada']}. Vale a regra; conferir com a pessoa avaliadora.",
            file=sys.stderr,
        )
    return resultado


def por_id(linhas: list[dict[str, str]], origem: str, esperados: set[str]) -> dict[str, dict[str, str]]:
    mapa = {}
    for linha in linhas:
        ident = linha.get("id_anonimo", "")
        if ident in mapa:
            raise ErroDados(f"{origem}: ID repetido {ident}")
        mapa[ident] = linha
    if set(mapa) != esperados:
        faltam = sorted(esperados - set(mapa))
        sobram = sorted(set(mapa) - esperados)
        raise ErroDados(f"{origem}: IDs esperados não batem (faltam {faltam}, sobram {sobram})")
    return mapa


def fmt(numero: float) -> str:
    return f"{numero:.3f}".replace(".", ",")


def resumo_notas(n: dict[str, int]) -> str:
    return f"C{n['correcao']} R{n['relevancia']} S{n['suporte']} FC{n['falha_critica']}"


def consolidar() -> tuple[list[dict], dict]:
    chave = ler_csv(RAIZ / "avaliacao" / "chave-anonimizacao.csv")
    id_de = {(l["caso"], l["versao"]): l["id_anonimo"] for l in chave}
    if set(id_de) != {(c, v) for c in CASOS for v in VERSOES}:
        raise ErroDados("chave-anonimizacao.csv não cobre exatamente CT01 a CT06 em A e B")
    ids_r2 = {id_de[(c, v)] for c in CASOS_R2 for v in VERSOES}

    f1 = {(l["caso"], l["versao"]): l for l in ler_csv(RAIZ / "resultados" / "f1-lexical.csv")}
    if set(f1) != set(id_de):
        raise ErroDados("f1-lexical.csv não tem as 12 saídas")
    r1 = por_id(ler_csv(RAIZ / "avaliacao" / "r1.csv"), "r1.csv", set(id_de.values()))
    r2 = por_id(ler_csv(RAIZ / "avaliacao" / "r2.csv"), "r2.csv", ids_r2)
    consenso_linhas = ler_csv(RAIZ / "avaliacao" / "consenso.csv", obrigatorio=False)
    consenso = {l["id_anonimo"]: l for l in consenso_linhas}

    tabela, iguais_r1_r2, faltando_consenso = [], 0, []
    for versao in VERSOES:
        for caso in CASOS:
            ident = id_de[(caso, versao)]
            n1 = notas_validas(r1[ident], "r1.csv")
            linha = {
                "caso": caso,
                "versao": versao,
                "id_anonimo": ident,
                "F1": f1[(caso, versao)]["F1"],
                "sinal_auto": f1[(caso, versao)]["sinal_auto"],
                "R1_correcao": n1["correcao"],
                "R1_relevancia": n1["relevancia"],
                "R1_suporte": n1["suporte"],
                "R1_falha_critica": n1["falha_critica"],
                "R1_aprovada": n1["aprovada"],
                "R2_correcao": "",
                "R2_relevancia": "",
                "R2_suporte": "",
                "R2_falha_critica": "",
                "R2_aprovada": "",
                "origem_decisao": "R1 (sem R2)",
                "falha_critica_final": n1["falha_critica"],
                "decisao_humana_final": n1["aprovada"],
                "justificativa": r1[ident].get("justificativa", ""),
            }
            if ident in ids_r2:
                n2 = notas_validas(r2[ident], "r2.csv")
                linha.update({f"R2_{k}": v for k, v in n2.items()})
                iguais_r1_r2 += int(n1["aprovada"] == n2["aprovada"])
                if n1["aprovada"] == n2["aprovada"] and n1["falha_critica"] == n2["falha_critica"]:
                    linha["origem_decisao"] = "R1 e R2 concordam"
                elif ident in consenso:
                    nc = notas_validas(consenso[ident], "consenso.csv")
                    linha.update(
                        {
                            "origem_decisao": "consenso",
                            "falha_critica_final": nc["falha_critica"],
                            "decisao_humana_final": nc["aprovada"],
                            "justificativa": consenso[ident].get("justificativa", ""),
                        }
                    )
                else:
                    faltando_consenso.append(f"{ident} ({caso}-{versao})")
            linha["auto_concorda_humano"] = int(int(linha["sinal_auto"]) == linha["decisao_humana_final"])
            tabela.append(linha)

    if faltando_consenso:
        raise ErroDados(
            "R1 e R2 divergiram (decisão ou falha crítica) e falta consenso em avaliacao/consenso.csv: "
            + ", ".join(faltando_consenso)
        )

    resumo = {"iguais_r1_r2": iguais_r1_r2}
    for versao in VERSOES:
        linhas_v = [l for l in tabela if l["versao"] == versao]
        valores_f1 = [float(l["F1"]) for l in linhas_v]
        resumo[versao] = {
            "f1_medio": statistics.mean(valores_f1),
            "f1_mediano": statistics.median(valores_f1),
            "aprovadas": sum(l["decisao_humana_final"] for l in linhas_v),
            "aprovadas_r1": sum(l["R1_aprovada"] for l in linhas_v),
            "sinais": sum(int(l["sinal_auto"]) for l in linhas_v),
            "falhas_criticas": sum(l["falha_critica_final"] for l in linhas_v),
        }
    resumo["concordancia_auto"] = sum(l["auto_concorda_humano"] for l in tabela)
    return tabela, resumo


def escrever_resumo(tabela: list[dict], resumo: dict, grafico: str) -> None:
    a, b = resumo["A"], resumo["B"]
    if b["falhas_criticas"] > 0:
        criterio = f"B tem {b['falhas_criticas']} falha(s) crítica(s). Pelo critério, B não avança."
    elif b["aprovadas"] > a["aprovadas"]:
        criterio = f"Aprovação de B ({b['aprovadas']}/6) maior que a de A ({a['aprovadas']}/6) e nenhuma falha crítica em B. Pelo critério, B avança para a próxima etapa."
    else:
        criterio = f"Aprovação de B ({b['aprovadas']}/6) igual ou menor que a de A ({a['aprovadas']}/6). Pelo critério, mantém-se A."

    divergentes = [l for l in tabela if not l["auto_concorda_humano"]]
    linhas = [
        "# Resumo automático dos resultados",
        "",
        "Gerado por `metricas/consolidar.py` a partir de `f1-lexical.csv`, `r1.csv`, `r2.csv` e do consenso. Não editar à mão: rodar o script de novo se algum dado mudar. A interpretação e a decisão ficam em `resultados/README.md`, `resultados/divergencia.md` e `decisao/decisao.md`.",
        "",
        "## Por versão (denominador 6)",
        "",
        "| Versão | F1 médio | F1 mediano | Sinais automáticos positivos | Aprovadas por R1 | Aprovadas (decisão final) | Falhas críticas (final) |",
        "| :--- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for versao in VERSOES:
        r = resumo[versao]
        linhas.append(
            f"| {versao} | {fmt(r['f1_medio'])} | {fmt(r['f1_mediano'])} | {r['sinais']}/6 | {r['aprovadas_r1']}/6 | {r['aprovadas']}/6 | {r['falhas_criticas']} |"
        )
    linhas += [
        "",
        "## Concordâncias",
        "",
        f"- Sinal automático e decisão humana final: **{resumo['concordancia_auto']}/12**.",
        f"- R1 e R2, decisão aprovada ou não, antes do consenso, nas quatro saídas revisadas: **{resumo['iguais_r1_r2']}/4**.",
        "",
        "## Aplicação do critério de avanço fixado no plano",
        "",
        criterio,
        "",
        "Isso é só a aplicação mecânica da regra. A decisão é experimental, não autoriza produção e é registrada pela equipe em `decisao/decisao.md`.",
        "",
        "## Divergências entre o sinal automático e a decisão humana",
        "",
    ]
    if divergentes:
        linhas += ["| Caso e versão | F1 | Sinal automático | Decisão humana final |", "| :--- | ---: | ---: | ---: |"]
        linhas += [
            f"| {l['caso']}-{l['versao']} | {fmt(float(l['F1']))} | {l['sinal_auto']} | {l['decisao_humana_final']} |"
            for l in divergentes
        ]
        linhas += ["", "Escolher ao menos uma para analisar em `divergencia.md`."]
    else:
        linhas.append("Não houve divergência. Discutir um caso-limite real em `divergencia.md`, sem inventar discordância.")
    linhas += ["", "## Tabela das 12 saídas", ""]
    linhas += [
        "| Caso e versão | F1 | Sinal | R1 | R2 | Origem da decisão | Decisão final |",
        "| :--- | ---: | ---: | :--- | :--- | :--- | ---: |",
    ]
    for l in tabela:
        r1 = resumo_notas({k: l[f"R1_{k}"] for k in NOTAS + ["falha_critica"]})
        r2 = resumo_notas({k: l[f"R2_{k}"] for k in NOTAS + ["falha_critica"]}) if l["R2_aprovada"] != "" else "não revisada"
        linhas.append(
            f"| {l['caso']}-{l['versao']} | {fmt(float(l['F1']))} | {l['sinal_auto']} | {r1} | {r2} | {l['origem_decisao']} | {l['decisao_humana_final']} |"
        )
    linhas += ["", "C = correção, R = relevância, S = suporte, FC = falha crítica.", "", f"Gráfico: `{grafico}`.", ""]
    (RAIZ / "resultados" / "resumo-automatico.md").write_text("\n".join(linhas), encoding="utf-8")


def grafico_png(tabela: list[dict], resumo: dict, caminho: Path) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, (esq, dir_) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"width_ratios": [1, 1.6]})
    x = range(len(VERSOES))
    largura = 0.36
    aprov = [resumo[v]["aprovadas"] for v in VERSOES]
    sinais = [resumo[v]["sinais"] for v in VERSOES]
    b1 = esq.bar([i - largura / 2 for i in x], aprov, largura, label="Aprovação humana", color="#3d8b5a")
    b2 = esq.bar([i + largura / 2 for i in x], sinais, largura, label="Sinal automático (F1 ≥ 0,5)", color="#9a9a9a")
    esq.bar_label(b1, labels=[f"{n}/6" for n in aprov])
    esq.bar_label(b2, labels=[f"{n}/6" for n in sinais])
    esq.set_xticks(list(x), [f"Versão {v}" for v in VERSOES])
    esq.set_ylim(0, 6.8)
    esq.set_ylabel("Saídas (de 6)")
    esq.set_title("Aprovação humana e sinal automático")
    esq.legend(loc="upper left", fontsize=8, frameon=False)

    f1 = {(l["caso"], l["versao"]): float(l["F1"]) for l in tabela}
    aprovada = {(l["caso"], l["versao"]): l["decisao_humana_final"] for l in tabela}
    xc = range(len(CASOS))
    for desloc, versao, cor in [(-largura / 2, "A", "#2f6f9f"), (largura / 2, "B", "#d08c3a")]:
        barras = dir_.bar([i + desloc for i in xc], [f1[(c, versao)] for c in CASOS], largura, label=f"Versão {versao}", color=cor)
        for barra, caso in zip(barras, CASOS):
            if aprovada[(caso, versao)]:
                dir_.text(barra.get_x() + barra.get_width() / 2, barra.get_height() + 0.02, "✓", ha="center", fontsize=9)
    dir_.axhline(0.5, color="#555555", linestyle="--", linewidth=1, label="τ = 0,5")
    dir_.set_xticks(list(xc), CASOS)
    dir_.set_ylim(0, 1.1)
    dir_.set_ylabel("F1 lexical")
    dir_.set_title("F1 por caso (✓ = aprovada na decisão humana final)")
    dir_.legend(loc="upper right", fontsize=8, frameon=False)
    fig.tight_layout()
    fig.savefig(caminho, dpi=200)
    plt.close(fig)


def grafico_svg(resumo: dict, caminho: Path) -> None:
    """Alternativa sem dependências: barras de aprovação humana e sinal automático."""
    partes = ['<svg xmlns="http://www.w3.org/2000/svg" width="420" height="260" font-family="sans-serif" font-size="12">',
              '<rect width="100%" height="100%" fill="white"/>',
              '<text x="210" y="20" text-anchor="middle" font-size="14">Aprovação humana e sinal automático (de 6)</text>']
    base, escala = 220, 30
    for i, versao in enumerate(VERSOES):
        x0 = 70 + i * 170
        for j, (rotulo, valor, cor) in enumerate(
            [("Humana", resumo[versao]["aprovadas"], "#3d8b5a"), ("Auto", resumo[versao]["sinais"], "#9a9a9a")]
        ):
            x = x0 + j * 60
            altura = valor * escala
            partes.append(f'<rect x="{x}" y="{base - altura}" width="50" height="{altura}" fill="{cor}"/>')
            partes.append(f'<text x="{x + 25}" y="{base - altura - 4}" text-anchor="middle">{valor}/6</text>')
            partes.append(f'<text x="{x + 25}" y="{base + 14}" text-anchor="middle">{rotulo}</text>')
        partes.append(f'<text x="{x0 + 55}" y="{base + 32}" text-anchor="middle">Versão {versao}</text>')
    partes.append("</svg>")
    caminho.write_text("\n".join(partes), encoding="utf-8")


def main() -> int:
    try:
        tabela, resumo = consolidar()
    except ErroDados as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        print("Nada foi gerado.", file=sys.stderr)
        return 2

    colunas = list(tabela[0].keys())
    with (RAIZ / "resultados" / "tabela-consolidada.csv").open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas, lineterminator="\n")
        escritor.writeheader()
        escritor.writerows(tabela)

    try:
        grafico = "grafico-resultados.png"
        grafico_png(tabela, resumo, RAIZ / "resultados" / grafico)
    except ImportError:
        grafico = "grafico-resultados.svg"
        grafico_svg(resumo, RAIZ / "resultados" / grafico)
        print("Aviso: matplotlib não instalado; gráfico gerado em SVG. Para PNG: pip install matplotlib", file=sys.stderr)

    escrever_resumo(tabela, resumo, grafico)
    a, b = resumo["A"], resumo["B"]
    print(f"A: aprovadas {a['aprovadas']}/6, F1 médio {fmt(a['f1_medio'])}. B: aprovadas {b['aprovadas']}/6, F1 médio {fmt(b['f1_medio'])}.")
    print(f"Concordância auto e humano {resumo['concordancia_auto']}/12. R1 e R2 {resumo['iguais_r1_r2']}/4.")
    print(f"Gerados: resultados/tabela-consolidada.csv, resultados/resumo-automatico.md, resultados/{grafico}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
