FROM python:3.13.0a3-alpine3.19

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /vehiculares
WORKDIR /vehiculares
COPY requirements.txt /vehiculares/

RUN pip install -r requirements.txt

COPY . /vehiculares/

#RUN python manage.py makemigrations --setting=vehiculares.settings.production

#RUN python manage.py migrate --setting=vehiculares.settings.production

CMD python manage.py runserver 0.0.0.0:8080