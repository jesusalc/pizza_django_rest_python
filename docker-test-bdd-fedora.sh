CONTAINER_ID="$(sudo docker ps -f "name=pizza_django_rest_python-web" --format "{{.ID}}" 2>&1; )"
CONTAINER_ID="$(tail -1 <<< "${CONTAINER_ID}" | xargs)"
sudo docker exec -it $CONTAINER_ID sh -c "cd /app && behave"

Linnbenton Community College

Ami Bradburn
1541 917 4816
bradbua@linnbenton.edu

Felicia Suttstrom
1541 917 4820
sodersf@linnbenton.edu


