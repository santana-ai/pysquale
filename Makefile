run_coverage:
	@echo "Starting coverage..."
	coverage run -m unittest discover -s tests/ --verbose
	coverage report -m
