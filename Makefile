.PHONY: all lint type test test-cov

CMD:=poetry run
PYMODULE:=blockchain_exploration
TESTS:=tests

poetry_install:
	poetry install

all: lint type test 

lint:
	$(CMD) flake8 $(PYMODULE) $(TESTS) 

type:
	$(CMD) mypy $(PYMODULE)  $(TESTS)   

test:
	$(CMD) pytest --cov=$(PYMODULE) $(TESTS)

test-cov:
	$(CMD) pytest --cov=$(PYMODULE) $(TESTS) --cov-report html

isort:
	$(CMD) isort $(PYMODULE) $(TESTS)
