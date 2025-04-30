# SICEI API - Final project

Final project for distributed systems. API for managing students, courses, and grades.

## Create a virtual environment
You can follow the [FastAPI official doc](https://fastapi.tiangolo.com/virtual-environments/) for setting the environment

```
python -m venv .venv
```

## Activate the environment
For Linux
```
source .venv/bin/activate
```

For Windows
```
.venv\Scripts\Activate.ps1
```

## Upgrade pip
```
python -m pip install --upgrade pip
```

## Install  FastAPI from requirements.txt
```
pip install -r requirements.txt
```

## Set the ENV file
Create a .env file with the following attributes for the production database
```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
POSTGRES_HOST=
POSTGRES_PORT=
```

## Run the Sicei API using Dockerfile
Build the image for the container using the provided Dockerfile

```
docker build -t sicei-api .
```

Start a new container based on the image you just created

```
docker run -d -p 8000:8000 --name sicei-api-container sicei-api
```

## Run dev mode with Docker Compose
Use the following command to start the docker compose

```
docker compose up -d
```

Use the following command to turn off the container

```
docker compose down
```
