PYTHON = python3
rta_predictions_protons = ../data/predictions_rta_protons_test_sample.csv
rta_predictions_gammas = ../data/predictions_rta_gammas_test_sample.csv


texoptions = -pdf \
	-output-directory=build \
	-interaction=nonstopmode \
	-halt-on-error

texinputs=TEXINPUTS=.:../../common:

all: build/P6-42.tar

build/P6-42.pdf: FORCE P6-42_f1.eps P6-42_f2.eps P6-42_f3.eps P6-42_f4.eps P6-42_f5.eps P6-42_f6.eps
	$(texinputs) $(bibinputs) latexmk $(texoptions) P6-42.tex

# this compiles the proceeding, opens a pdf viewer and
# then constantly updates if the input files are changed
preview: FORCE
	$(texinputs) $(bibinputs) latexmk $(texoptions) -pvc P6-42.tex

build/P6-42.tar: build/P6-42.pdf P6-42.bib P6-42.tex
	mkdir -p build/P6-42
	cp ../poster/references.bib P6-42.bib
	cp P6-42.tex build/P6-42.pdf build/P6-42
	cd build && tar -cf P6-42.tar P6-42



P6-42_f1.eps:  matplotlibrc ../plots/plot_hillas.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_hillas.py  P6-42_f1.eps

P6-42_f2.eps:  $(rta_predictions_protons) $(rta_predictions_gammas) matplotlibrc ../plots/plot_trigger.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_trigger.py --no-fill  $(rta_predictions_gammas) $(rta_predictions_protons) P6-42_f2.eps

P6-42_f3.eps:  matplotlibrc ../plots/plot_total_eventrate.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_total_eventrate.py  ../data/performance_csv/*.csv P6-42_f3.eps

P6-42_f4.eps: ../data/performance_flink.csv ../data/performance_storm.csv ../data/performance_streams-runtime.csv ../plots/plot_eventrate_by_framework.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_eventrate_by_framework.py ../data/performance_flink.csv ../data/performance_streams-runtime.csv ../data/performance_storm.csv P6-42_f4.eps -l flink-runtime -l streams-runtime -l storm-runtime


P6-42_f5.eps: ../data/predictions.hdf ../plots/plot_auc_type.py matplotlibrc
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_auc_type.py  ../data/predictions.hdf P6-42_f5.eps

P6-42_f6.eps:  $(rta_predictions_protons) $(rta_predictions_gammas) matplotlibrc ../plots/plot_multi_tel_auc.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_multi_tel_auc.py  $(rta_predictions_gammas) $(rta_predictions_protons) P6-42_f6.eps


FORCE:

build:
	mkdir -p build

clean:
	rm -rf build
	rm *.eps
