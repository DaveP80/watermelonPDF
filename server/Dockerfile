FROM python:3.9

RUN pip install Flask gunicorn PyMuPDF PyPDF2 flask_wtf wtforms python-dotenv

COPY src/ /app/
RUN ls -la /app/*
/app/output:
/app/static/files:

WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app