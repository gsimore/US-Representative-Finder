
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
	@echo 'Installing Node Dependencies...'
	npm install
	@echo 'Installing Python Dependencies...'
	make install_requirements

run:
	@echo 'Running app'
	python find_my_rep/app.py

run_tests:
	@echo 'Running pytest'
	pytest find_my_rep/tests.py
