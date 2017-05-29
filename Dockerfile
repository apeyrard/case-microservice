FROM python:latest

COPY . .

RUN pip install --no-cache-dir -r requirements/prd.txt

EXPOSE 8000

ENTRYPOINT [ "gunicorn", "--config", "gunicorn.conf", "-b", ":8000", "Case.case:app" ]

HEALTHCHECK --interval=30s --timeout=2s CMD curl -f http://localhost:8000/health-check || exit 1
