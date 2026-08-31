# Intermediate Algebra — Chapters 1 & 2 Review

Three printable handouts covering **Chapter 1, Basic Techniques for Solving Equations**
(§1.1 Isolation, §1.2 Substitution, §1.3 Elimination, §1.4 Graphing) and
**Chapter 2, Functions Review** (§2.1 Function Basics, §2.2 Graphing Functions,
§2.3 Composition, §2.4 Inverse Functions).

| Handout | File | Length | Use it for |
|---|---|---|---|
| Review worksheet | `review-worksheet.html` | 6 pp. | 39 problems (35 required + 4 starred) in seven parts, with work space and grids |
| Solutions | `review-solutions.html` | 8 pp. | Fully worked solutions, boxed answers, and the reasoning students should show |
| Short quiz review | `quiz-review.html` | 3 pp. | Skills checklist, note-sheet outline, common-mistake list, 10-question practice quiz (~30 min) with a short answer key |

Print-ready PDFs are committed in [`pdf/`](pdf/).

## Problem coverage

| Part | Problems | Section | Skills |
|---|---|---|---|
| A | 1–6 | §1.1 | LCD clearing, radical equations + extraneous roots, rational equations, absolute value, literal equations |
| B | 7–12 | §1.2–1.3 | Substitution, elimination, 3×3 systems, inconsistent systems, line–circle intersection |
| C | 13–17 | §1.4 | Slope, intercepts, parallel/perpendicular lines, two word problems |
| D | 18–22 | §2.1 | Domain, evaluation at expressions, range by completing the square, difference quotient, vertical line test |
| E | 23–26 | §2.2 | Transformations, tracking points through them, sketching, even/odd |
| F | 27–30 | §2.3 | Both composition orders, domain of a composition, decomposing, iterated composition |
| G | 31–35 | §2.4 | Inverses of linear, cubic, and rational functions; restricted domains; conceptual questions |
| ★ | 36–39 | mixed | Nested radicals, an involution, a functional equation, range via inverse |

Every answer in the solutions handout and the quiz answer key was verified symbolically
with SymPy before publication.

## Rebuilding the PDFs

The handouts are plain HTML + CSS. Math is typeset with a small set of CSS classes
(`.frac`, `.rt`, `.fn`) rather than MathJax or LaTeX, so the files render identically
offline in any browser and print without a network connection.

```sh
pip install playwright
python3 build.py                 # renders all three into pdf/
python3 build.py quiz-review.html   # or just one
```

`build.py` reuses a Chromium already present under `/opt/pw-browsers`; set `CHROME_PATH`
to point it elsewhere.

## Editing

Open any of the three `.html` files in a browser to preview, edit the HTML directly, and
re-run `build.py`. A few conventions worth knowing:

- Problem numbers come from a CSS counter that runs continuously across all parts of a
  document — the HTML `start` attribute does **not** drive it. Adding or removing a
  `<li>` renumbers everything automatically. Add `class="restart"` to an `<ol
  class="problems">` to begin a fresh count.
- `<li class="star">` marks an optional starred problem.
- `<div class="work">` (also `.work sm` / `.work lg`) is blank work space;
  `<div class="grid">` is a graphing grid.
- `<div class="pagebreak"></div>` forces a new page in the PDF.
