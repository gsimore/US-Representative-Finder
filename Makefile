
update_requirements:
	@echo 'Installing pip-tools...'
	pip install -U -q pip-tools
	pip-compile --output-file=requirements/base.txt requirements/base.in

install_requirements:
	@echo 'Installing pip-tools...'
	export PIP_REQUIRE_VIRTUALENV=true; \
	pip install -U -q pip-tools
	@echo 'Installing requirements...'
	pip-sync requirements/base.txt

setup:
	@echo 'Setting up the environment...'
	make install_requirements

run:
	@echo 'Running app'
	export FLASK_APP=find_my_rep/app
	flask run

run-dev:
	@echo 'Running local development'
	export FLASK_ENVIRONMENT=development
	make run
