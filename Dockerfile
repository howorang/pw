FROM python:3.8.2 AS build
COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000/tcp
CMD gunicorn -b 0.0.0.0:8000 app:app