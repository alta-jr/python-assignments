# Build the Chapter 1-2 quiz and its solutions.
#   make          build both PDFs
#   make quiz.pdf build one
#   make clean    remove LaTeX aux files (keeps the PDFs)

TEX := pdflatex -interaction=nonstopmode -halt-on-error
DOCS := quiz solutions

.PHONY: all clean distclean
all: $(addsuffix .pdf,$(DOCS))

# Two passes so \pageref{LastPage} in the page footer resolves.
%.pdf: %.tex preamble.tex
	$(TEX) $< >/dev/null
	$(TEX) $<

clean:
	rm -f *.aux *.log *.out *.toc

distclean: clean
	rm -f $(addsuffix .pdf,$(DOCS))
