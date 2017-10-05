PYTHON = python3
rta_predictions_protons = ../data/predictions_rta_protons_test_sample.csv
rta_predictions_gammas = ../data/predictions_rta_gammas_test_sample.csv


texoptions = -pdf \
	-output-directory=build \
	-interaction=nonstopmode \
	-halt-on-error

texinputs=TEXINPUTS=.:../../common:

all: build/P6-19.tar

build/P6-19.pdf: FORCE P6-19_f1.eps P6-19_f2.eps P6-19_f3.eps
	$(texinputs) $(bibinputs) latexmk $(texoptions) P6-19.tex

# this compiles the proceeding, opens a pdf viewer and
# then constantly updates if the input files are changed
preview: FORCE
	$(texinputs) $(bibinputs) latexmk $(texoptions) -pvc P6-19.tex

build/P6-19.tar: build/P6-19.pdf P6-19.bib P6-19.tex
	mkdir -p build/P6-19
	cp P6-19.bib P6-19.tex build/P6-19.pdf build/P6-19
	cd build && tar -cf P6-19.tar P6-19



P6-19_f1.eps:  matplotlibrc ../plots/plot_hillas.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_hillas.py  P6-19_f1.eps

P6-19_f2.eps:  $(rta_predictions_protons) $(rta_predictions_gammas) matplotlibrc ../plots/plot_trigger.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_trigger.py --no-fill  $(rta_predictions_gammas) $(rta_predictions_protons) P6-19_f2.eps

P6-19_f3.eps:  matplotlibrc ../plots/plot_total_eventrate.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_total_eventrate.py  ../data/performance_csv/*.csv P6-19_f3.eps



FORCE:

build:
	mkdir -p build

clean:
	rm -rf build
	rm *.eps
