CONTAINER_ID=$(docker ps -f "name=pizza_django_web" --format "{{.ID}}")
docker exec -it ${CONTAINER_ID}  sh -c "cd /app && python manage.py makemigrations pizza_django --empty"