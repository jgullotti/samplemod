init:
	pipenv install

test:
	pytest

docs:
	pdoc --html sample

.PHONY: init test docs
