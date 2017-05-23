FROM python:latest

COPY . .

RUN pip install --no-cache-dir -r requirements/prd.txt

EXPOSE 8000

ENTRYPOINT [ "gunicorn", "--config", "gunicorn.conf", "-b", ":8000", "Case.case:app" ]
