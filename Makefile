.PHONY: test test-cov

TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
PACKAGE=linked_list

test:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test tests

test-node:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test tests/test_node.py
	
test-list:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test tests/test_list.py

test-cov:
	@echo $(TAG)Running tests with coverage$(END)
	PYTHONPATH=. py.test --cov=$(PACKAGE) tests --cov-report term-missing

coverage:
	@echo $(TAG)Coverage report$(END)
	@PYTHONPATH=. coverage run --source=$(PACKAGE) $(shell which py.test) ./tests -q --tb=no >/dev/null; true
	@coverage report -m
