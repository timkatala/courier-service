FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y python3.8 python3.8-dev python3-pip python3-virtualenv apt-utils curl wget mc cron

RUN apt-get install -y gdal-bin python3-gdal libpq-dev

RUN python3 -m virtualenv --python=/usr/bin/python3 /opt/venv
COPY requirements.txt /home
RUN /opt/venv/bin/pip install --no-cache-dir -r /home/requirements.txt

WORKDIR /var/www



CMD . /opt/venv/bin/activate && python manage.py migrate && python manage.py collectstatic --noinput && python manage.py loaddata fixtures/data.json && python manage.py runserver 0.0.0.0:8080
