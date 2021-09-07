#!/bin/bash
echo "Разворачиваем контейнеры"
docker-compose up -d --build
echo "Контейнеры запущены"
echo "Делаем миграции"
docker-compose exec web python3 manage.py migrate auth
docker-compose exec web python3 manage.py migrate --run-syncdb
echo "Собираем статику"
docker-compose exec web python manage.py collectstatic --no-input
