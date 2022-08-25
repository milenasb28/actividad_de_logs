FROM python:3.8-slim-buster

RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "get_api_to_mysql.py"]
