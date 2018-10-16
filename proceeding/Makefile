PYTHON = python3
rta_predictions_protons = ../data/predictions_rta_protons_test_sample.csv
rta_predictions_gammas = ../data/predictions_rta_gammas_test_sample.csv


texoptions = -pdf \
	-output-directory=build \
	-interaction=nonstopmode \
	-halt-on-error

texinputs=TEXINPUTS=.:../../common:

all: build/P6-63_v3.zip

build/P6-63.pdf: FORCE P6-63_f1.eps P6-63_f2.eps P6-63_f3.eps P6-63_f4.eps P6-63_f5.eps
	$(texinputs) $(bibinputs) latexmk $(texoptions) P6-63.tex

# this compiles the proceeding, opens a pdf viewer and
# then constantly updates if the input files are changed
preview: FORCE
	$(texinputs) $(bibinputs) latexmk $(texoptions) -pvc P6-63.tex

build/P6-63_v3.zip: build/P6-63.pdf P6-63.bib P6-63.tex
	mkdir -p build/P6-63
	cp P6-63.tex build/P6-63.pdf copyrightform.pdf *.eps build/P6-63
	cd build && zip -r P6-63_v3.zip P6-63/

P6-63_f1.eps: adass_overview.pdf
	pdftops adass_overview.pdf P6-63_f1.eps

P6-63_f2.eps: ../data/predictions.hdf ../plots/plot_auc_type.py matplotlibrc
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_auc_type.py  ../data/predictions.hdf P6-63_f2.eps

P6-63_f3.eps:  $(rta_predictions_protons) $(rta_predictions_gammas) matplotlibrc ../plots/plot_multi_tel_auc.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_multi_tel_auc.py  $(rta_predictions_gammas) $(rta_predictions_protons) P6-63_f3.eps

P6-63_f4.eps: ../data/performance_flink.csv ../data/performance_storm.csv  ../plots/plot_eventrate_by_framework.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_eventrate_by_framework.py ../data/performance_flink.csv  ../data/performance_storm.csv P6-63_f4.eps -l flink-runtime  -l storm-runtime

P6-63_f5.eps:  matplotlibrc ../plots/plot_total_eventrate.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_total_eventrate.py  ../data/performance_csv/*.csv P6-63_f5.eps

FORCE:

build:
	mkdir -p build

clean:
	-rm -rf build
	-rm *.eps
	-rm *-eps-converted-to.pdf
