#!/bin/bash

# Остановка и удаление контейнера, запущенного от образа `infra-lending_page_covid`
docker stop $(docker ps -aqf "ancestor=infra-lending_page_covid") || true
docker rm $(docker ps -aqf "ancestor=infra-lending_page_covid") || true

docker stop $(docker ps -q ancestor=nginx:1.21.3-alpine) || true
docker rm $(docker ps -q ancestor=nginx:1.21.3-alpine) || true

#docker stop $(docker ps -q ancestor=nginx:1.21.3-alpine) || true
#docker rm $(docker ps -q ancestor=nginx:1.21.3-alpine) || true

# Удаление образа `infra-lending_page_covid`
docker rmi infra-lending_page_covid

docker rmi nginx:1.21.3-alpine

cd ../infra

docker compose up