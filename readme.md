Docker Usage
This project can be run inside a Docker container, providing a consistent environment
for execution.
Prerequisites
●
Docker Desktop must be installed and running on your system.
Build the Image
To build the Docker image, run the following command from the project's root directory:sh
docker build -t hello-env:latest.
### Run the Container
To run the application inside a container, use the following command:
```
sh
docker run --rm hello-env:latest

This ensures the application runs in a clean environment.