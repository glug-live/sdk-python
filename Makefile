.PHONY: install lint format test docs

SHELL := bash

BLACK := poetry run black
PYLINT := poetry run pylint
MYPY := poetry run mypy
PYTEST := poetry run pytest -v
PDOC := poetry run pdoc

install:
	@poetry install

lint:
	@echo -e "\nChecking python format\n"
	${BLACK} --check .
	@echo -e "\nChecking python typing\n"
	${MYPY} directus
	@echo -e "\nChecking python lint\n"
	${PYLINT} directus

format:
	${BLACK} .

test:
	${PYTEST}

docs:
	${PDOC} --force --html --template-dir docs-templates --output-dir docs directus
