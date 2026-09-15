#!/usr/bin/env python3
"""Render a Project Euler progress grid as a self-contained SVG.

Input is the "Problems Solved by ID" export from your Project Euler progress page
(https://projecteuler.net/progress — the small TXT icon next to the heading). Save it as
`solved.txt` in the repository root. Any file of integers separated by commas, spaces or
newlines works.

    python tools/make_progress.py                 # writes progress.svg
    python tools/make_progress.py --total 1009    # set the number of published problems

The SVG is plain markup with no external references, so GitHub renders it inline.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOLVED = ROOT / "solved.txt"
OUT = ROOT / "progress.svg"

COLS = 40
CELL = 11
GAP = 2
PAD = 14
HEADER = 34

SOLVED_FILL = "#f5a623"
UNSOLVED_FILL = "#e4e6eb"
TEXT = "#24292f"
MUTED = "#57606a"


def read_solved(path: Path) -> set[int]:
    if not path.exists():
        raise SystemExit(
            f"{path.name} not found.\n"
            "Download 'Problems Solved by ID' from https://projecteuler.net/progress "
            f"and save it as {path.name} in the repository root."
        )
    ids = {int(n) for n in re.findall(r"\d+", path.read_text(encoding="utf-8"))}
    if not ids:
        raise SystemExit(f"No problem numbers found in {path.name}.")
    return ids


def render(solved: set[int], total: int) -> str:
    rows = (total + COLS - 1) // COLS
    width = PAD * 2 + COLS * CELL + (COLS - 1) * GAP
    height = PAD * 2 + HEADER + rows * CELL + (rows - 1) * GAP
    pct = 100.0 * len(solved) / total

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="Project Euler progress: {len(solved)} of {total} problems solved">',
        '<style>text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}</style>',
        f'<rect width="{width}" height="{height}" fill="none"/>',
        f'<text x="{PAD}" y="{PAD + 12}" font-size="13" font-weight="600" fill="{TEXT}">'
        f"Project Euler</text>",
        f'<text x="{PAD}" y="{PAD + 27}" font-size="11" fill="{MUTED}">'
        f"{len(solved)} of {total} problems solved ({pct:.1f}%)</text>",
    ]

    for problem in range(1, total + 1):
        idx = problem - 1
        x = PAD + (idx % COLS) * (CELL + GAP)
        y = PAD + HEADER + (idx // COLS) * (CELL + GAP)
        fill = SOLVED_FILL if problem in solved else UNSOLVED_FILL
        parts.append(
            f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{fill}">'
            f"<title>Problem {problem}</title></rect>"
        )

    parts.append("</svg>")
    return "\n".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--total",
        type=int,
        default=1009,
        help="number of published problems (default: 1009)",
    )
    args = parser.parse_args()

    solved = read_solved(SOLVED)
    highest = max(solved)
    if highest > args.total:
        raise SystemExit(
            f"solved.txt contains problem {highest}, above --total {args.total}. "
            "Pass the current problem count with --total."
        )

    OUT.write_text(render(solved, args.total), encoding="utf-8")
    print(f"{OUT.name} written: {len(solved)} / {args.total} solved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
