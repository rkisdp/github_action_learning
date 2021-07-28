FROM python:3.8.2-alpine
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip install -r base.txt
EXPOSE 8000
CMD python manage.py runserver 0:8000
