FROM python:3.10.0a6-slim-buster

ENV PYTHONUNBUFFERED 1
RUN mkdir /sistema
WORKDIR /sistema
COPY requirements.txt /sistema/
RUN pip install -r requirements.txt
COPY . /sistema/
#RUN python manage.py makemigrations --setting=settings.develop 
#RUN python manage.py migrate --setting=settings.develop 
CMD python manage.py runserver 0.0.0.0:8080
