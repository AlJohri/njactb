.PHONY: test clean install build upload

test:
	pipenv run python -m pytest

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf .cache

install:
	pip install --upgrade -q pipenv
	pipenv install --dev

build:
	pipenv run python setup.py sdist bdist_wheel

upload:
	pipenv run twine upload dist/*
