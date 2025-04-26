dc:=docker-compose.yaml
dc-debug:=docker-compose-debug.yaml

# build docker containers for the project.
build:
	docker compose -f $(dc) build

# build docker containers for the project with no cache
build-no-cache:
	docker compose -f $(dc) build --no-cache

# runs containers
up:
	docker compose -f $(dc) up -d 

#stops containers
down:
	docker compose -f $(dc) down

# run all containers in debug mode

debug-up:
	docker compose -f $(dc-debug) up

# stop msvc-user service and run only msvc-user in debug mode
debug-user-up: user-down
	docker compose -f $(dc-debug) up -d msvc-user

# stop msvc-product service and run only msvc-product in debug mode
debug-product-up: product-down
	docker compose -f $(dc-debug) up -d msvc-product

# stop msvc-product service 
product-down:
	docker compose -f $(dc-debug) down msvc-product

# stop msvc-user service 
user-down:
	docker compose -f $(dc-debug) down msvc-user