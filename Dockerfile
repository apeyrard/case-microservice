FROM python:latest

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "gunicorn", "--config", "gunicorn.conf", "-b", ":8000", "case:app" ]
