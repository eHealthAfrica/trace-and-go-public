import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amsel.settings")

import djcelery
djcelery.setup_loader()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
