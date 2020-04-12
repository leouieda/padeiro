# Build, package, test, and clean
PROJECT=padeiro
PYTEST_ARGS=--cov-report=term-missing --cov=$(PROJECT) --doctest-modules -v --pyargs
FORMAT_FILES=setup.py $(PROJECT) tests

help:
	@echo "Commands:"
	@echo ""
	@echo "  install   install in editable mode"
	@echo "  test      run the test suite (including doctests) and report coverage"
	@echo "  format    run black to automatically format the code"
	@echo "  check     run code style and quality checks (black and flake8)"
	@echo "  clean     clean up build and generated files"
	@echo ""

install:
	pip install --no-deps -e .

test:
	pytest $(PYTEST_ARGS) $(PROJECT) tests

format:
	black $(FORMAT_FILES)

check:
	black --check $(FORMAT_FILES)
	flake8 $(FORMAT_FILES)

clean:
	find . -name "*.pyc" -exec rm -v {} \;
	find . -name ".coverage.*" -exec rm -v {} \;
	rm -rvf build dist MANIFEST *.egg-info __pycache__ .coverage .cache .pytest_cache
