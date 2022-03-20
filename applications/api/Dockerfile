# 
FROM python:3.9.10-alpine3.15

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install  --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"] 