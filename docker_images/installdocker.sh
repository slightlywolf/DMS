#installs docker, requires a connection
#to the internet
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

export PATH=/usr/bin:$PATH
export DOCKER_HOST=unix:///run/user/1000/docker.sock
#this part is highly sus, it allows the running
# of docker as a non privileged user

dockerd-rootless-setuptool.sh install

#if it doesnt work execute the commands it
#says to execute and then run the dockerd..
#line above again

#read about this to understand what this is
#doing docs.docker.ocm/go/daemon-access/

#this grants privileges equivalent to root user
#so be very suspicious what whats happening here

#creates the group
sudo groupadd docker
#adds the user to the group
sudo usermod -aG docker $USER



