BASENAME=FrAtCEESD
TALKNAME=$(BASENAME)-2023-10-13-Campbell
LATEX = pdflatex --shell-escape
FIGURES := $(shell ls Figures/*/*.pdf Figures/*/*.png )
SUBTALKS := $(shell ls thetalk-*.tex)

.SUFFIXES: .pdf .tex

%.pdf: %.tex
	$(LATEX) $<
	$(LATEX) $<

.PHONY: debug

#.tex.pdf:
#	$(LATEX) $*
#	$(LATEX) $*	

all: $(TALKNAME).pdf

$(TALKNAME).pdf: $(BASENAME).tex $(SUBTALKS) $(FIGURES)
	$(LATEX) $(BASENAME)
	$(LATEX) $(BASENAME)
	mv $(BASENAME).pdf $(TALKNAME).pdf

clean:
	rm -fr _minted*  *.vrb *.tex~ *.toc *.aux *.log *.nav *.out *.snm *.flc $(BASENAME).pdf

realclean: clean
	rm -f $(TALKNAME).pdf *~

debug:
	@echo "BASENAME: $(BASENAME)"
	@echo "TALKNAME: $(TALKNAME)"
	@echo "FIGURES: $(FIGURES)"
	@echo "SUBTALKS: $(SUBTALKS)"
