# Website

[![CI build](https://github.com/tjh90/website/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/tjh90/website/actions/workflows/build.yml)

Simple website

## Building

Run the following commands from the repository root:

``` shell
# Compile the application.
mvn clean install -P prod

# Build docker images and run the application in a container.
docker-compose.exe --file .\build\compose.yml up --build
```
