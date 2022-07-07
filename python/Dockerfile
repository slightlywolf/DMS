# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /flask-docker
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5010/tcp
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]