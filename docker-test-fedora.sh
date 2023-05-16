CONTAINER_ID="$(sudo docker ps -f "name=pizza_django_rest_python-web" --format "{{.ID}}" 2>&1; )"
CONTAINER_ID="$(tail -1 <<< "${CONTAINER_ID}" | xargs)"
sudo docker exec -it ${CONTAINER_ID}  sh -c "cd /app && python manage.py  test pizza_django/tests"