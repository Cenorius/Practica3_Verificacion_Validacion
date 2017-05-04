init:
	pip install -r requirements.txt

test:
	lettuce app/tests/features

