.PHONY: build up down restart nuke-it-all

docker_compose = docker-compose -f docker-compose.dev.yml

build:
	cp .env.example .env
	$(docker_compose) build

up:
	$(docker_compose) up

down:
	$(docker_compose) down

restart:
	$(MAKE) down
	$(MAKE) up

all:
	$(MAKE) build
	$(MAKE) up

#detached:
#	$(docker_compose) build

nuke-it-all:
	$(docker_compose) down --volumes --remove-orphans
	docker system prune -f
	rm .env
