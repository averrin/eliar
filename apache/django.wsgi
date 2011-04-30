import os
import sys

sys.path.append('/home/averrin/django_projects')
os.environ['DJANGO_SETTINGS_MODULE'] = 'eliar.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
