FROM python:3.9

RUN pip install Flask gunicorn PyMuPDF PyPDF2 flask_wtf wtforms python-dotenv

COPY src/ ./app/

WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app