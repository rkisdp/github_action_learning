# Use an official Python runtime as a parent image
FROM python:3.8.2-alpine

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Sets dumping log messages directly to stream instead of buffering
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk --update add \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    # pillow dependencies
    jpeg-dev \
    zlib-dev \
    supervisor \
    gdal-dev \
    geos-dev \
    proj-dev \
    wget \
    tar \
    make \
    nginx \
    nginx-mod-http-headers-more


# Creating folders and copy required content
RUN mkdir /app
RUN mkdir -p /etc/supervisord/conf.d
COPY ./deployments/supervisord.conf /etc/supervisord/supervisord.conf
WORKDIR /app
COPY . $app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip3 install --trusted-host pypi.python.org -r requirements/development.txt

# nginx conf
RUN mkdir -p /run/nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY ./deployments/nginx/nginx.conf /etc/nginx/nginx.conf

COPY ./deployments/migration_script.sh /usr/local/bin/migration_script.sh
COPY ./deployments/celery.sh /usr/local/bin/celery.sh
COPY ./deployments/gunicorn_start.sh /usr/local/bin/gunicorn_start.sh

# Application entrypoint
RUN chmod +x /usr/local/bin/migration_script.sh
RUN chmod +x /usr/local/bin/celery.sh
RUN chmod +x /usr/local/bin/gunicorn_start.sh
CMD ["supervisord", "-n", "-c", "/etc/supervisord/supervisord.conf"]
