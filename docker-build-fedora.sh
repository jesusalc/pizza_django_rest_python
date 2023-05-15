# podman is better then docker-ce
# linux need sudo to docker becuase sockets are privileged in linux
sudo systemctl start podman.service
sudo docker-compose up --build

