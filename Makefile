instal:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py

format:
	black *.py

run:
	python app.py

run-aws:
	python3 app.py
