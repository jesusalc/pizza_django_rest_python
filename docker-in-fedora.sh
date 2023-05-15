CONTAINER_ID="$(sudo docker ps -f "name=pizza_django_rest_python-web" --format "{{.ID}}" 2>&1; )"
CONTAINER_ID="$(tail -1 <<< "${CONTAINER_ID}" | xargs)"
docker run -it "${CONTAINER_ID}"  /bin/bash
