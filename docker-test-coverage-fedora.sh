CONTAINER_ID="$(sudo docker ps -f "name=pizza_django_rest_python-web" --format "{{.ID}}" 2>&1; )"
CONTAINER_ID="$(tail -1 <<< "${CONTAINER_ID}" | xargs)"
sudo docker exec -it ${CONTAINER_ID}  sh -c "cd /app && coverage run manage.py test && coverage report"
# docker run -it   --rm -v $(pwd):/app -w /app python:3.8 bash -c "pip install -r requirements.txt && coverage run manage.py test && coverage report"
# docker run -it ${CONTAINER_ID}  --rm -v $(pwd):/app -w /app python:3.8 bash -c "pip install -r requirements.txt && coverage run manage.py test && coverage report"