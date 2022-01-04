# Introduction to Docker

### What is Docker : [Here](https://docker.com/)

### Documentation : [Here](https://docs.docker.com/)

### Download and Installation : [Here](https://docs.docker.com/get-docker/)

### Docker Hub : [Here](https://hub.docker.com/search)

### Test Docker Installation (Using [hello-world](https://hub.docker.com/_/hello-world) image)

```shell
    $ docker run hello-world
```

### Please refer to Powerpoint Presentation and Individual Docker files for each project. Dockerfile is self-explanatory.

### Commonly used Docker commands

```shell
    # List Images
    $ docker images
    # List Running Containers
    $ docker ps
    # List All Containers
    $ docker ps -a
    # Delete any Container
    $ docker rm <container_id>
    # Delete all unused and exited containers
    $ docker container prune
    # Delete all unused images
    $ docker image prune
    # Delete all stopped Containers
    $ docker rm $(docker ps --filter status=exited -q)
    # Delete all Dangling Images
    $ docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
    # List Volumes
    $ docker volume ls
    # Inspect a Volume
    $ docker volume inspect <volume_name>
    # Gain Shell Access for a running Container (if supported by the image)
    $ docker exec -it <container_id> bash
```

### Advanced and Further Knowledge

- Docker Compose : [Here](https://docs.docker.com/compose/)

### For More Information Visit

- [DockerCheatSheet](https://github.com/wsargent/docker-cheat-sheet)
- [DockerOffiical](https://docs.docker.com/engine/reference/commandline/docker/)
