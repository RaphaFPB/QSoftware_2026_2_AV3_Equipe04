#!/usr/bin/env python3
"""Calcula P, R e F1 lexical para respostas comparadas a referências."""

from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from typing import TextIO


REQUIRED_COLUMNS = {"caso", "versao", "resposta", "referencia"}
OUTPUT_COLUMNS = ["caso", "versao", "precisao", "revocacao", "F1", "sinal_auto"]


def tokens(text: str) -> list[str]:
    """Normaliza Unicode para NFC, aplica casefold e extrai tokens de palavra."""
    normalized = unicodedata.normalize("NFC", text).casefold()
    return re.findall(r"\w+", normalized, flags=re.UNICODE)


def lexical_scores(answer: str, reference: str) -> tuple[float, float, float]:
    """Retorna precisão, revocação e F1 usando interseção de multiconjuntos."""
    answer_counts = Counter(tokens(answer))
    reference_counts = Counter(tokens(reference))
    overlap = sum((answer_counts & reference_counts).values())

    answer_total = sum(answer_counts.values())
    reference_total = sum(reference_counts.values())
    precision = overlap / answer_total if answer_total else 0.0
    recall = overlap / reference_total if reference_total else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall
        else 0.0
    )
    return precision, recall, f1


def calculate(input_file: TextIO, output_file: TextIO, tau: float) -> None:
    reader = csv.DictReader(input_file)
    if reader.fieldnames is None:
        raise ValueError("O CSV de entrada não contém cabeçalho.")
    missing = REQUIRED_COLUMNS - set(reader.fieldnames)
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes: " + ", ".join(sorted(missing))
        )

    writer = csv.DictWriter(output_file, fieldnames=OUTPUT_COLUMNS)
    writer.writeheader()
    rows = 0
    for row_number, row in enumerate(reader, start=2):
        answer = row.get("resposta")
        reference = row.get("referencia")
        if answer is None or reference is None:
            raise ValueError(f"Campo vazio/inválido na linha {row_number}.")
        precision, recall, f1 = lexical_scores(answer, reference)
        writer.writerow(
            {
                "caso": row.get("caso", ""),
                "versao": row.get("versao", ""),
                "precisao": f"{precision:.6f}",
                "revocacao": f"{recall:.6f}",
                "F1": f"{f1:.6f}",
                "sinal_auto": int(f1 >= tau),
            }
        )
        rows += 1

    if rows == 0:
        raise ValueError("O CSV de entrada não contém respostas para calcular.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Calcula F1 lexical (NFC, casefold, tokens e multiconjuntos)."
    )
    parser.add_argument("entrada", type=Path, help="CSV com caso, versao, resposta, referencia")
    parser.add_argument(
        "--tau",
        type=float,
        required=True,
        help="Limiar de aprovação; sinal=1 quando F1 >= tau.",
    )
    parser.add_argument(
        "--saida",
        type=Path,
        help="Arquivo CSV de saída (padrão: stdout).",
    )
    args = parser.parse_args()

    if not 0.0 <= args.tau <= 1.0:
        parser.error("--tau deve estar entre 0 e 1.")

    try:
        with args.entrada.open("r", encoding="utf-8-sig", newline="") as input_file:
            if args.saida:
                with args.saida.open("w", encoding="utf-8", newline="") as output_file:
                    calculate(input_file, output_file, args.tau)
            else:
                calculate(input_file, sys.stdout, args.tau)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"Erro: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
