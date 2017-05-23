# Case microservice

This flask webservice provides a REST api to uppercase or lowercase strings.

# Usage

## Lowercase
curl -X POST -H "Content-Type: application/json" -d '{"text":"Foo"}' 127.0.0.1:5001/v1/lower

## Uppercase
curl -X POST -H "Content-Type: application/json" -d '{"text":"Foo"}' 127.0.0.1:5001/v1/upper
