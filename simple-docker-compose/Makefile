.PHONY: up test

build-image:
	docker build -t my_nginx .

up:
	docker-compose up

test:
	open "http://localhost:80"   
