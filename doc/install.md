# Install with Docker

Install [Docker](https://docs.docker.com/installation/#installation)

### On Mac OS X

- Install [Bower](http://bower.io)
- Install [Homebrew](http://brew.sh)
- Install Docker Compose `$ brew install docker-compose`

### On Ubuntu

- Install Python's PIP and npm/nodejs `$ sudo apt-get install python-pip npm nodejs-legacy`
- Install Bower `$ sudo npm install -g bower`
- Install Docker Compose `$ sudo pip install -U docker-compose`

After you have all the tool dependencies installed for your respective OS, move onto install the app.

## In tab 1

    $ git clone <thisrepo>
    $ cd <thisrepo>

Make your `/amsel/local_settings.py` file with at least `DEBUG=True` in it

## In tab 2 start the db
NOTE: when this session is stopped, the data will be lose.

    $ sudo docker-compose run db

## In tab 1 again start the webserver

    $ sudo docker-compose run web bash

Now within the docker container as root

    # createdb -h localhost -U postgres tag
    # /opt/tag/manage.py migrate
    # /opt/tag/manage.py runserver 0.0.0.0:8000

