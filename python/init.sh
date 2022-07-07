# Enables fast building
DOCKER_BUILDKIT=1 docker build .

#build flask docker image
docker build --tag flask-docker .

#run flask docker image with port 5010(host):5000(container) exposed
docker run -p 5010:5000 --name flask-docker flask-docker

docker rm $(docker ps -aqf status=exited)