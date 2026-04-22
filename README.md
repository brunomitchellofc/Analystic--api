# Analystics API

A time-series analytics API built with FastAPI and TimescaleDB, containerized with Docker and deployed on Railway.

The goal was simple: build something that actually runs in production with a real time-series database, not SQLite.

## Stack

- **FastAPI** - REST API
- **TimescaleDB** - time-series PostgreSQL
- **Docker + Docker Compose** - containerization
- **Railway** - deployment

## Deployed on Railway + TimescaleDB Cloud

The API was deployed on Railway connected to a TimescaleDB Cloud instance (West Europe).  
No longer running to avoid costs, but here's proof it worked:

### Infrastructure

<img width="1920" height="815" alt="Image" src="https://github.com/user-attachments/assets/a93dadc0-0e5a-49d7-9bd4-bcb55b6af152" />

### Database — TimescaleDB Cloud

<img width="1920" height="745" alt="Image" src="https://github.com/user-attachments/assets/ce02f81d-4788-4805-829e-56b45338d257" />

### API live on Railway

<img width="1920" height="775" alt="Image" src="https://github.com/user-attachments/assets/d0d5513d-7918-4e05-a160-4f8796b4b38e" />

## Running locally

Prerequisites: Docker installed.

```bash
docker compose up
```

Docs at `http://localhost:8002/docs`

## Development

```bash
docker compose up --watch       # hot reload
docker compose down -v          # remove containers and volumes
docker compose run app /bin/bash  # shell access
```

[LinkedIn](https://www.linkedin.com/in/bruno-mitchell-246b4a2a6/) 
