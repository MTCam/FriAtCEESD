BASENAME=MixItUp
TALKNAME=mixitup-m2n
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

$(TALKNAME).pdf: $(BASENAME).tex $(SUBTALKS) $(FIGURES) ../ceesd-macros.tex ./mtc-macros.tex
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
