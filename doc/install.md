Running the code currently requrires a few libraries and services.

First set up your local env.

    $ git clone <thisrepo>
    $ cd <thisrepo>
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ ./manage syncdb
    $ ./manage migratedb
    $ ./manage runserver
    
You might have to tunnel the requests to your local dev server through ssh. If you are using a formhub that is not local.

    $ ssh -R \*:8000:localhost:8000 yourserver.com
    
normally does the trick.

Then upload the form to formhub and set the webook to 

    https://yourserver.com/submit
    
once this is done you should be able to submit stuff through formhub and see the data under:

    127.0.0.1:8000/admin/
    
We will have to figure out how to share the flows in https://rapidpro.io/flow/

    
    
    
    
