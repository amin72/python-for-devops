install:
    # install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt&&\
        python -c "import nltk; nltk.download('punkt')"

format:
    # format code
	black *.py mylib/*.py

lint:
    # flake8 or pylint
	pylint --disable=R,C *.py mylib/*.py

test:
    # test
	pytest -vv --cov

build:
    # build container

deploy:
    # deploy

all: install format lint test deploy
