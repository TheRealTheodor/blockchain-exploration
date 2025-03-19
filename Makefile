precommit:
	ruff check
	ruff format
	mypy .
	pytest
