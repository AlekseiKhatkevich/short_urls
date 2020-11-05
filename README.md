# short_urls
для корректной работы после запуска контейнеров нужно выполнить в контейнере или через docker-compose exec:

python manage.py migrate

python manage.py collectstatic --noinput
