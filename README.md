# Case microservice

This flask webservice provides a REST api to uppercase or lowercase strings.

# Installation

## Build docker image:
```bash
docker build -t apeyrard/case .
```

## Run image
```bash
docker run -e GUNICORN_WORKERS=4 -p 8000:8000 apeyrard/case
```

# Usage

## Lowercase
curl -X POST -H "Content-Type: application/json" -d '{"text":"Foo"}' 127.0.0.1:5001/v1/lower

## Uppercase
curl -X POST -H "Content-Type: application/json" -d '{"text":"Foo"}' 127.0.0.1:5001/v1/upper
