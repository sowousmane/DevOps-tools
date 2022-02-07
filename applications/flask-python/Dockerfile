FROM python:3.9.10-alpine3.15

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV DEBUG_METRICS=false
#RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
#COPY . .
#CMD flask run
