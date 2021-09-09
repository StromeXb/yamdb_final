#!/bin/bash
echo "Разворачиваем контейнеры"
docker-compose up -d
echo "Контейнеры запущены"
echo "Делаем миграции"
docker-compose exec web python3 manage.py migrate auth
docker-compose exec web python3 manage.py migrate --run-syncdb
echo "Собираем статику"
docker-compose exec web python manage.py collectstatic --no-input
echo "Создаём суперпользователя. Пожалуйста, следуйте инструкциям:"
docker-compose exec web python manage.py createsuperuser
echo "Настройка завершена. Пройдите по адресу http://127.0.0.1/admin/"
