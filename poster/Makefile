PYTHON = python
rta_predictions_protons = ../data/predictions_rta_protons_test_sample.csv
rta_predictions_gammas = ../data/predictions_rta_gammas_test_sample.csv

texoptions = -lualatex \
			 -output-directory=build \
			 -interaction=nonstopmode \
			 -halt-on-error

all: build/poster.pdf

build/poster.pdf: poster.tex beamerthemefact.sty figures/fermi.pdf figures/runtime.pdf figures/image.pdf figures/auc_type.pdf figures/total_auc.pdf figures/resolution.pdf figures/trigger.pdf figures/skymap.pdf  | build
	latexmk $(texoptions) poster.tex


figures/fermi.pdf: ../plots/plot_fermi.py ../data/fermi_results.fits matplotlibrc
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_fermi.py ../data/fermi_results.fits figures/fermi.pdf

figures/image.pdf: ../plots/plot_hillas.py matplotlibrc
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_hillas.py figures/image.pdf

figures/auc_type.pdf: ../data/predictions.hdf ../plots/plot_auc_type.py matplotlibrc
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_auc_type.py  ../data/predictions.hdf figures/auc_type.pdf

figures/total_auc.pdf:  $(rta_predictions_protons) $(rta_predictions_gammas) matplotlibrc ../plots/plot_multi_tel_auc.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_multi_tel_auc.py  $(rta_predictions_gammas) $(rta_predictions_protons) figures/total_auc.pdf

figures/resolution.pdf: ../plots/plot_angular_resolution_vs_energy.py matplotlibrc
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_angular_resolution_vs_energy.py $(rta_predictions_gammas) figures/resolution.pdf

figures/skymap.pdf: ../plots/plot_sky.py matplotlibrc
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_sky.py $(rta_predictions_gammas) $(rta_predictions_protons) figures/skymap.pdf

figures/trigger.pdf:  $(rta_predictions_protons) $(rta_predictions_gammas) matplotlibrc ../plots/plot_trigger.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_trigger.py  $(rta_predictions_gammas) $(rta_predictions_protons) figures/trigger.pdf

figures/runtime.pdf:  matplotlibrc ../plots/plot_total_eventrate.py
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_total_eventrate.py  ../data/performance_csv/*.csv figures/runtime.pdf


preview: poster.tex beamerthemefact.sty | build
	max_print_line=1048576 latexmk $(texoptions) -pvc poster.tex

build:
	mkdir -p build

clean:
	rm -rf build
