FROM python:latest

COPY . .

RUN pip install --no-cache-dir -r requirements/prd.txt

EXPOSE 8000

ENTRYPOINT [ "gunicorn", "--config", "gunicorn.conf", "-b", ":8000", "Case.case:app" ]

ARG CIRCLE_BRANCH
ARG CIRCLE_SHA1
ENV SERVICE_BRANCH=${CIRCLE_BRANCH}
ENV SERVICE_COMMIT=${CIRCLE_SHA1}
ENV SERVICE_CHECK_HTTP=/health-check
ENV SERVICE_CHECK_INTERVAL=15s

HEALTHCHECK --interval=30s --timeout=2s CMD curl -f http://localhost:8000/health-check || exit 1
