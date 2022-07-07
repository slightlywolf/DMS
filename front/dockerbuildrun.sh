DOCKER_BUILDKIT=1 docker build -f Dockerfile --tag angular-docker .

docker run -p 5020:4200 --name angular-docker angular-docker

docker rm $(docker ps -aqf status=exited)