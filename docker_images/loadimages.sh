
#note that these have to be executed in the
#commandline without using sh .loadimages
#because of something to do with stdin
#im not sure 
docker load -i flaskdocker.tar 
docker load -i angulardocker.tar 
sudo docker images 