PYTHON = /usr/local/bin/python3

texoptions = -lualatex \
			 -output-directory=build \
			 -interaction=nonstopmode \
			 -halt-on-error

all: build/poster.pdf

build/poster.pdf: poster.tex beamerthemefact.sty figures/fermi.pdf figures/image.pdf | build
	latexmk $(texoptions) poster.tex


figures/fermi.pdf: ../plots/plot_fermi.py ../data/fermi_results.fits matplotlibrc
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_fermi.py ../data/fermi_results.fits figures/fermi.pdf


figures/image.pdf: ../plots/plot_hillas.py matplotlibrc
	MATPLOTLIBRC=./ $(PYTHON) ../plots/plot_hillas.py figures/image.pdf

# this compiles the poster, opens a pdf viewer and
# then constantly updates if the input files are changed
preview: poster.tex beamerthemefact.sty | build
	max_print_line=1048576 latexmk $(texoptions) -pvc poster.tex

build:
	mkdir -p build

clean:
	rm -rf build
