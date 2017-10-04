PYTHON = python3

texoptions = -pdf \
	-output-directory=build \
	-interaction=nonstopmode \
	-halt-on-error

texinputs=TEXINPUTS=.:../../common:

all: build/P6-19.tar

build/P6-19.pdf: FORCE P6-19_f1.eps
	$(texinputs) $(bibinputs) latexmk $(texoptions) P6-19.tex

# this compiles the proceeding, opens a pdf viewer and
# then constantly updates if the input files are changed
preview: FORCE
	$(texinputs) $(bibinputs) latexmk $(texoptions) -pvc P6-19.tex

build/P6-19.tar: build/P6-19.pdf P6-19.bib P6-19.tex
	mkdir -p build/P6-19
	cp P6-19.bib P6-19.tex build/P6-19.pdf build/P6-19
	cd build && tar -cf P6-19.tar P6-19


P6-19_f1.eps:  matplotlibrc ../plots/plot_total_eventrate.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_total_eventrate.py  ../data/performance_csv/*.csv P6-19_f1.eps



FORCE:

build:
	mkdir -p build

clean:
	rm -rf build
