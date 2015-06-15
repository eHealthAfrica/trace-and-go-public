Yo will need two screen/tmux/tabs sessions

In tab 1

    $ git clone <thisrepo>
    $ cd <thisrepo>

In tab 2 start the db

    $ sudo docker-compose run db

In tab 1 again start the webserver

    $ sudo docker-compose run web bash

Now within the docker container as root

    # /opt/tag/manage.py migrate
    # /opt/tag/manage.py runserver 0.0.0.0:8000

