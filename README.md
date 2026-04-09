# Build an Analystics API using FastAPI + Time-series Postgres

Own your data pipeline!

## Docker

- `docker build -t analystic-api Dockerfile.web .`
- `docker run analystic-api`

becomes

- `docker compose up --watch`
- `docker compose down` or `docker compose down -v`(to remove volumes) 
- `docker compose run app /bin/bash` or `docker compose run app python`