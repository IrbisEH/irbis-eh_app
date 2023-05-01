#!/bin/bash

# Путь до виртуального окружения
VENV_PATH="/home/irbis-eh/irbis-eh_app/venv"
# Путь до приложения Flask
APP_PATH="/home/irbis-eh/irbis-eh_app/irbis-eh_app/app:app"

# Активируем виртуальное окружение
. ${VENV_PATH}/bin/activate

# Запускаем gunicorn
gunicorn --bind 0.0.0.0:5000 ${APP_PATH}