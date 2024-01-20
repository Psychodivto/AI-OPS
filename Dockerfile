FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
<<<<<<< HEAD
RUN mkdir /core
WORKDIR /core
COPY requirements.txt /core/
RUN pip install -r requirements.txt
COPY . /core/
=======
RUN mkdir /sistema
WORKDIR /sistema
COPY requirements.txt /sistema/
RUN pip install -r requirements.txt
COPY . /sistema/
>>>>>>> master
#RUN python manage.py makemigrations --setting=settings.develop 
#RUN python manage.py migrate --setting=settings.develop 
CMD python manage.py runserver 0.0.0.0:8080
