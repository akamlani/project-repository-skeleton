.PHONY: clean

VENV_PATH=".venv"
REPO_NAME={{cookiecutter.repo_name}}

vm:
	python -m venv $(VENV_PATH)
	. $(VENV_PATH)/bin/activate

install:
	pip install -U pip pip-tools setuptools wheel &&			\
	pip install -r requirements.txt

install_docs:
	pip install -U pip pip-tools setuptools wheel &&			\
	pip install -r project/$(REPO_NAME)/docs/requirements.txt

#build_docs:
#sphinx-quickstart
#	make html

clean:
	find . -type f -name "*.DS_Store" -ls -delete
	find . -regex ".*/__pycache__" -exec rm -rf {} +
	find . -regex ".*\.egg-info" -exec rm -rf {} +
	rm -rf $(VENV_PATH)

setup: vm install install_docs
