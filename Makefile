install:
    # install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt

post-install:
	python -m textblob.download_corpora

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
	docker build -t deploy-fastapi .

run:
	docker run -p 8080:8080 deploy-fastapi

deploy:
    # deploy
	sudo docker pull aminasa/deploy-fastapi:latest &&\
		sudo docker run -p 8080:8080 deploy-fastapi

all: install post-install format lint test deploy
