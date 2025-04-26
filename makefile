dc:=docker-compose.yaml
dc-debug:=docker-compose-debug.yaml


build:
	docker compose -f $(dc) build

build-no-cache:
	docker compose -f $(dc) build --no-cache

up:
	docker compose -f $(dc) up -d 

down:
	docker compose -f $(dc) down

debug-up:
	docker compose -f $(dc-debug) up

debug-down:
	docker compose -f $(dc-debug) down

debug-user-up: user-down
	docker compose -f $(dc-debug) up -d msvc-user

debug-product-up: product-down
	docker compose -f $(dc-debug) up -d msvc-product

product-down:
	docker compose -f $(dc-debug) down msvc-product

user-down:
	docker compose -f $(dc-debug) down msvc-user