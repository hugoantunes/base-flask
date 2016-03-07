help:
	@echo "Uso: make tests     		  -- Run all python tests"
	@echo "Uso: make run     		  -- Run flask app"

tests:
	@python -m unittest discover

run:
	@python run.py