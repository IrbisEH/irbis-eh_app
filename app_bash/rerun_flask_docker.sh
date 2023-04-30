#!/bin/bash

# Остановка и удаление контейнера, запущенного от образа `infra-lending_page_covid`
docker stop $(docker ps -aqf "ancestor=infra-lending_page_covid") || true
docker rm $(docker ps -aqf "ancestor=infra-lending_page_covid") || true

# Удаление образа `infra-lending_page_covid`
docker rmi infra-lending_page_covid

cd ../infra

docker compose up