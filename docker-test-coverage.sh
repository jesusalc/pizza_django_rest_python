CONTAINER_ID=$(docker ps -f "name=pizza_django_web" --format "{{.ID}}")
docker exec -it ${CONTAINER_ID}  sh -c "cd /app && coverage run manage.py test pizza_django/tests && coverage report"
# docker run -it   --rm -v $(pwd):/app -w /app python:3.8 bash -c "pip install -r requirements.txt && coverage run manage.py test && coverage report"
# docker run -it ${CONTAINER_ID}  --rm -v $(pwd):/app -w /app python:3.8 bash -c "pip install -r requirements.txt && coverage run manage.py test && coverage report"
