.PHONY: install test run clean

install:
	pip install -r requirements.txt

test:
	PYTHONPATH=. python -m pytest test_app.py -v

run:
	gunicorn --bind 0.0.0.0:8080 app:app

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf src/core_engine/obfuscation/__pycache__
