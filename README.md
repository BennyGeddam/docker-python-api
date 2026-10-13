# docker-python-api

A small REST API built with **Flask**, packaged as a **Docker** container, and covered by an automated **pytest** test suite.

## Endpoints

| Method | Path | Response |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | `{"status": "healthy"}`, used to check the service is alive |
| GET | `/info` | Service name, version and status |

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python app.py
```

The API runs at http://localhost:5000.

## Run the tests

```bash
pytest -v
```

The tests use Flask's built-in test client to check every endpoint's status code and JSON response, plus a 404 case for unknown routes.

## Run with Docker

```bash
docker build -t docker-python-api .
docker run -p 5000:5000 docker-python-api
```

## Tech

Python · Flask · Docker · pytest · Git

## Continuous integration

GitHub Actions runs the pytest suite on Python 3.14, matching the Docker image, on every push and pull request. If the tests pass, a second job builds the Docker image. The workflow can also be started manually from the Actions tab.

The pipeline validates the project; it does not publish images or deploy the application.

## Roadmap

- Deploy to Kubernetes
