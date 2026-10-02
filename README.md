# Dockerized Web Application

A beginner-friendly web application built using Python Flask and Docker.

## Technologies

- Python
- Flask
- Docker
- Docker Compose

## Run with Docker

```bash
docker build -t dockerized-web-app .
docker run -d -p 5000:5000 --name dockerized-web-app dockerized-web-app
