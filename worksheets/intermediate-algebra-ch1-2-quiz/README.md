# Intermediate Algebra — Chapters 1 & 2 Quiz

A 10-question quiz (100 points) and a full solutions key, built in LaTeX.
**Every problem is taken verbatim from the textbook** — Richard Rusczyk, David Patrick,
and Ravi Boppana, *Art of Problem Solving: Intermediate Algebra* — five from Chapter 1
(Basic Techniques for Solving Equations) and five from Chapter 2 (Functions Review).
All are drawn from the chapters' Review Problems.

| File | What it is |
|---|---|
| `quiz.tex` → `quiz.pdf` | Student copy, 4 pp., name/date/score line, work space sized to fill each page |
| `solutions.tex` → `solutions.pdf` | Instructor copy, 4 pp., full worked solutions with the source problem cited and grading notes |
| `preamble.tex` | Shared LaTeX preamble (page style, headings, solution environment) |
| `Makefile` | `make` builds both PDFs |

## Problems used

| Q | Source | Section | Skill | Answer |
|---|---|---|---|---|
| 1 | Review 1.23(b) | §1.1 Isolation | Compound inequality, interval notation | `[-3/2, 4]` |
| 2 | Review 1.19(a) | §1.3 Elimination | 2×2 linear system | `(7, 3)` |
| 3 | Review 1.20 | §1.2 Substitution | Age word problem | daughter is 8 |
| 4 | Review 1.24 | §1.2 Substitution | System that is linear in √x, √y | `(4, 25)` |
| 5 | Review 1.21(a) | §1.4 Larger Systems | 3×3 linear system | `(5, 0, -6)` |
| 6 | Review 2.23(d) | §2.1 Function Basics | Domain and range of a rational function | domain `x ≠ 2/3`, range `y ≠ -4/3` |
| 7 | Review 2.24(a) | §2.1 Function Basics | Domain with two competing restrictions | `(5/2, 3]` |
| 8 | Review 2.35 | §2.2 Graphing | Graph of `y = \|f(x)\|` from the graph of `f` | reflect the part below the x-axis |
| 9 | Review 2.25 | §2.3 Composition | Composition of two rational functions | `2x/(x+2)` |
| 10 | Review 2.37 | §2.4 Inverse Functions | Find `c` so that `f` is its own inverse | `c = -3` |

Question 10 is attributed to the AHSME in the textbook; the citation is carried through to
the solutions key.

Problems requiring the textbook's own figures (Review 2.27 and 2.29, which supply graphs)
were deliberately left out so the quiz is self-contained. Question 8 covers §2.2 without
needing a figure.

Every answer was verified symbolically with SymPy before the key was written.

## Building

Needs a LaTeX distribution with `amsmath`, `enumitem`, `fancyhdr`, `titlesec`, `lastpage`,
and the `newpx` fonts (on Debian/Ubuntu: `texlive-latex-recommended`, `texlive-latex-extra`,
`texlive-fonts-extra`, `texlive-plain-generic`).

```sh
make            # builds quiz.pdf and solutions.pdf
make clean      # removes .aux/.log, keeps the PDFs
```

Each document is built twice so the `Page n of m` footer resolves.

## Editing

- Work space on the quiz is `\work`, which expands to `\vfill`. Space is distributed to
  fill each page, so it is never silently lost at a page break — control pagination with
  `\newpage` and let the questions space themselves.
- Solutions use the `solution` environment; `\answer{...}` boxes a math answer and
  `\answertext{...}` boxes a prose one.
- `\source{...}` sets the small italic citation line above each solution.
