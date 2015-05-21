FROM ubuntu:14.04

RUN apt-get update && apt-get -y upgrade && apt-get install -y \
  git \
  wget \
  python-psycopg2 \
  python-dev \
  python-virtualenv \
  postgresql-server-dev-all

ADD ./requirements.txt /opt/tag/requirements.txt
RUN pip install -r /opt/tag/requirements.txt
ADD . /opt/tag
RUN python /opt/tag/manage.py collectstatic --noinput
CMD supervisord -c /opt/tag/config/supervisord.conf
