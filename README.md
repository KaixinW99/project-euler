# Project Euler

My solutions to [Project Euler](https://projecteuler.net) — number theory, combinatorics and algorithm
problems with a performance budget attached — written in Python.

![Project Euler](https://projecteuler.net/profile/KaixinWang.png)

![Level](https://img.shields.io/badge/Project%20Euler-Level%209%20Dodecahedron-f5a623?style=flat-square)
![Solved](https://img.shields.io/badge/Solved-229%20%2F%201009%20%2822.7%25%29-4c9aff?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab?style=flat-square&logo=python&logoColor=white)

![Progress](progress.svg)

*Each square is one problem; orange squares are solved. Generated from my own solved list by
[`tools/make_progress.py`](tools/make_progress.py).*

---

## What is (and isn't) published

Project Euler asks that solutions beyond problem 100 not be shared, so other people get to have the same
insight. **This repository contains solutions to problems 1–100 only.** My other solutions stay private;
the progress grid is the only public trace of them.

## Contents

| Path | What it is |
| :--- | :--- |
| [`solutions/`](solutions/) | One file per problem, `p001.py` … `p100.py`. Each prints its answer. [Index with titles →](solutions/README.md) |
| [`data/`](data/) | Input files Project Euler provides for some problems (names, matrices, poker hands, …) |
| [`solved.txt`](solved.txt) | IDs of every problem I have solved |
| [`progress.svg`](progress.svg) | The grid above |
| [`tools/make_progress.py`](tools/make_progress.py) | Renders the grid from `solved.txt` — or directly from the export on the Project Euler progress page |
| [`requirements.txt`](requirements.txt) | Third-party packages used by the solutions |

## Techniques, with where to find them

| Technique | Problems |
| :--- | :--- |
| Prime sieves — Eratosthenes, Sundaram | [10](solutions/p010.py), [35](solutions/p035.py), [46](solutions/p046.py), [47](solutions/p047.py), [49](solutions/p049.py), [50](solutions/p050.py), [51](solutions/p051.py), [60](solutions/p060.py) |
| Euler's totient function | [69](solutions/p069.py), [70](solutions/p070.py), [72](solutions/p072.py) |
| Integer partitions / tree recursion | [15](solutions/p015.py), [18](solutions/p018.py), [31](solutions/p031.py), [67](solutions/p067.py), [76](solutions/p076.py), [78](solutions/p078.py) |
| Dynamic programming on grids | [81](solutions/p081.py), [82](solutions/p082.py) |
| Shortest paths — A\* search with a priority queue | [83](solutions/p083.py) |
| Continued fractions and Pell's equation | [64](solutions/p064.py), [65](solutions/p065.py), [66](solutions/p066.py), [100](solutions/p100.py) |
| Exact rational arithmetic (`fractions`) | [33](solutions/p033.py), [57](solutions/p057.py), [71](solutions/p071.py), [73](solutions/p073.py) |
| Monte Carlo simulation | [84](solutions/p084.py) — Monopoly square frequencies |
| Constraint solving / backtracking | [96](solutions/p096.py) — Sudoku |
| Simulation with careful rule encoding | [54](solutions/p054.py) — poker hands |
| Cryptanalysis (XOR key recovery) | [59](solutions/p059.py) |

## Running

```bash
python -m pip install -r requirements.txt
python solutions/p001.py          # run from the repository root
```

Solutions that read a file from `data/` locate it themselves, so they can be run from anywhere.

Regenerate the progress grid after solving more problems — download *Problems Solved by ID* from your
[progress page](https://projecteuler.net/progress) (TXT icon), save it as `solved.txt`, then:

```bash
python tools/make_progress.py                 # writes progress.svg
python tools/make_progress.py --total 1009    # if more problems have been published
```

Both export formats are accepted: `961##2026-03-25 20:28:26` (one per line, with solve time) and
`1, 2, 3, …`.

## Notes

Most problems have an obvious brute force that will not finish; the work is finding the structure that makes
them tractable — a sieve instead of trial division, a recurrence instead of enumeration, a closed form
instead of a loop. That habit of asking "will this scale?" before running anything is the same one I rely on
in scientific simulation.

The code is kept as I originally wrote it while solving, including comments on approaches that were too
slow, so it shows the reasoning rather than only the final answer.
