PYTHON := python

.PHONY: venv install sim plot all

venv:
	cd simulations/python && $(PYTHON) -m venv .venv

install:
	cd simulations/python && .venv/Scripts/activate && pip install -r requirements.txt

sim:
	cd simulations/python && .venv/Scripts/activate && $(PYTHON) run_simulations.py

plot:
	cd simulations/python && .venv/Scripts/activate && $(PYTHON) plot_chi.py ../../data/susceptibility.csv

all: sim plot

.PHONY: chi_test chi_T

chi_test:
	cd simulations/python && .venv/Scripts/activate && $(PYTHON) chi_significance_test.py  -0.000009 -0.0000092 -0.0000087 --sigma 1e-7 1e-7 1e-7

chi_T:
	cd simulations/python && .venv/Scripts/activate && $(PYTHON) chi_T_predictions.py --outdir ../../data
