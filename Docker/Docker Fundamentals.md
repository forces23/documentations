![1756310717330](image/DockerFundamentals/1756310717330.png)


Core Concepts

* What Docker is and why it’s used (containerization vs virtual machines)
* Images vs Containers vs Registries
* Container lifecycle: build → run → stop → remove
* Docker architecture: Docker Engine, Docker Daemon, Docker CLI

Docker Images

* **Dockerfile basics** :
  * `FROM`, `RUN`, `COPY`, `ADD`, `WORKDIR`, `ENV`, `EXPOSE`, `CMD`, `ENTRYPOINT`
* **Building images** : `docker build -t <image_name> .`
* **Managing images** :
  * `docker images`, `docker rmi <image>`
  * Tagging images (`<repo>:<tag>`)
* **Best practices** :
  * Use small base images (Alpine)
  * Layer caching optimization
  * Minimize image size

Docker Containers 

* Running containers: `docker run -it -p <host>:<container> <image>`
* Managing containers: `docker ps`, `docker stop`, `docker rm`, `docker logs`, `docker exec`
* Container networking basics (ports, bridging, host mode)
* Mounting volumes for persistent data (`-v <host_path>:<container_path>`)

Docker Compose

* Purpose: run **multi-container applications**
* `docker-compose.yml` structure: services, networks, volumes
* Common commands: `docker-compose up`, `docker-compose down`, `docker-compose logs`, `docker-compose build`
* Linking services (e.g., frontend → backend → database)

Networking & Volumes 

* Container networking modes: bridge, host, overlay
* Exposing ports to the host
* Named volumes vs bind mounts
* Sharing data between containers

Docker Registries

* Docker Hub (public registry) vs private registries
* Pushing and pulling images: `docker push`, `docker pull`
* Versioning/tagging images for deployments

Docker Swarm / Orchestration Basics

* Multi-node clusters
* Services and tasks
* Scaling containers (`docker service scale`)

Best Practices

* Keep containers  **stateless** ; persist data with volumes
* Minimize container size for faster builds and deployments
* Use **.dockerignore** to reduce build context
* Tag images clearly (versioning)
* Avoid running containers as root

Debugging & Monitoring

* Inspect container details: `docker inspect <container>`
* View logs: `docker logs -f <container>`
* Check resource usage: `docker stats`
* Remove unused images/containers: `docker system prune`
