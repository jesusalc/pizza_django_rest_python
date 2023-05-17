CONTAINER_ID="$(sudo docker ps -f "name=pizza_django_rest_python-web" --format "{{.ID}}" 2>&1; )"
CONTAINER_ID="$(tail -1 <<< "${CONTAINER_ID}" | xargs)"
# sudo docker run -it "${CONTAINER_ID}"  /bin/bash
sudo docker run -it pizza_django_rest_python-web  /bin/bash
