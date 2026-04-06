# Makefile for common Discord bot development tasks

.PHONY: setup fix troubleshoot run lint format install-hooks

setup:
	python -m venv venv
	venv/bin/python -m pip install --upgrade pip
	venv/bin/python -m pip install -r requirements.txt

fix:
	python setup_tools/fix.py

troubleshoot:
	python setup_tools/troubleshoot.py

run:
	python main.py

lint:
	python -m pip install black
	python -m black --check .

format:
	python -m pip install black
	python -m black .

install-hooks:
	python -m pip install pre-commit
	python -m pre_commit install
