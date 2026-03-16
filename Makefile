.PHONY: install test run clean

install:
	pip install -r requirements.txt

test:
	PYTHONPATH=. python -m pytest test_main.py -v

run:
	uvicorn main:app --reload

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
