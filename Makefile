

IMAGE_TAG="chesschessgo-db"
CONTAINER_NAME="app"
TAGGINGDB_PORT=3030
POSTGRES_SECRET="chesschessgo"
POSTGRES_PORT=5432
POSTGRES_CONTAINER_NAME="ChessDB-Postgres"
POSTGRES_USER="chessdb-client"
POSTGRES_DATABASE="chessdb_server"
.phony: build run exec clean
SOCAT_PID_FILE=".socat-display-pid"

up:
	export IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
	#socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$$DISPLAY\" & echo $$! > ${SOCAT_PID_FILE}
	docker compose -f docker/compose.yaml build
	docker compose -f docker/compose.yaml up -d
down:
	#cat ${SOCAT_PID_FILE} | xargs kill
	docker compose -f docker/compose.yaml down

build: clean
	docker build -t ${IMAGE_TAG} -f docker/Dockerfile .

run: build
	docker run -d -it \
				-v .:/app \
				--user dev \
				-p "${TAGGINGDB_PORT}:${TAGGINGDB_PORT}" \
				--name ${CONTAINER_NAME} ${IMAGE_TAG}

run-postgres:
	docker run  \
				--name ${POSTGRES_CONTAINER_NAME} \
				-e POSTGRES_USER=${POSTGRES_USER} \
				-e POSTGRES_PASSWORD=${POSTGRES_SECRET} \
				-e POSTGRES_DB=${POSTGRES_DATABASE} \
				-v ./database:/var/lib/postgresql/data \
				-p "${POSTGRES_PORT}:${POSTGRES_PORT}" \
				-d postgres

exec:
	docker exec -it ${CONTAINER_NAME} /bin/bash

clean:
	docker rm -f ${CONTAINER_NAME}
