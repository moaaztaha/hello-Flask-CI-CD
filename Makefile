install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv application.py

lint:
	pylint --disable=R,C application.py