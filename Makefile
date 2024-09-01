.PHONY: format_python
format_python: 
	python3 -m black .
	python3 -m isort .
