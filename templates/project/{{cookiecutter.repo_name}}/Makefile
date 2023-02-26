# download and install conda environment
# setup:
#   conda remove -n ENV_NAME --all
# 	conda create -n core.3.7 python=3.7
# 	conda activate core.3.7
#   conda update
# 	python -m virtualenv ~/.venv

VENV_PATH={{cookiecutter.venv_path}}
PACKAGE_NAME={{cookiecutter.pkg_name}}
PACKAGE_INSTALL_NAME={{cookiecutter.pkg_install_name}}

CONDA_ENV_NAME={{cookiecutter.conda_env_name}}
PYTHON_VERSION={{cookiecutter.python_version}}
ENV_DEP_PATH={{cookiecutter.env_dep_path}}

.PHONY: clean

git_configure:
	git init

vm:
	python -m venv $(VENV_PATH)
	. $(VENV_PATH)/bin/activate
	echo "$(VENV_PATH)/bin/activate" >> ~/.bashrc
	echo "$(VENV_PATH)/bin/activate" >> ~/.zshrc

doc:
	python -m venv $(VENV_PATH)-doc
	. $(VENV_PATH)-doc/bin/activate
	echo "$(VENV_PATH)-doc/bin/activate" >> ~/.bashrc
	echo "$(VENV_PATH)-doc/bin/activate" >> ~/.zshrc

conda_install:
	conda create -n $(CONDA_ENV_NAME) python=$(PYTHON_VERSION) && 			\
	source $$(conda info --base)/etc/profile.d/conda.sh && 					\
	conda activate $(CONDA_ENV_NAME)										\
	conda update

install:
# pre-commmit to git hooks on execution of 'git commit'
	pip install -U pip pip-tools setuptools wheel &&						\
	pip install -r $(ENV_DEP_PATH)/requirements.txt && 						\
	pre-commit install && 													\
	pre-commit autoupdate

clean:
	pip uninstall $(PACKAGE_INSTALL_NAME)
	find . -type f -name "*.DS_Store" -ls -delete
	find . -regex ".*/__pycache__" -exec rm -rf {} +
	find . -regex ".*\.egg-info" -exec rm -rf {} +
	rm -rf $(VENV_PATH)

build:
	python setup.py build

test:
	pip install -r  $(ENV_DEP_PATH)/requirements_test.txt
	python -m pytest -vvv  --cov=$(PACKAGE_NAME) tests
# 	python -m pytest -vvv  --cov=$(PACKAGE_NAME) examples tests
# 	python -m pytest -ravv --cov=$(PACKAGE_NAME) examples tests

quality:
	black --check *.py
	isort --check-only *.py

style:
	black   *.py
	isort   *.py
	flake8  --statistics *.py

lint:
	pylint *.py

setup: vm install
all: install quality style lint test
