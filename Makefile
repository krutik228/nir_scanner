mypy:
	mypy app cli

pylint:
	pylint app cli

flake8:
	flake8 app cli tests

fmt: isort black

fmt_check:
	black app cli tests --check

black:
	black app cli tests

lint: black mypy pylint flake8