import os
import sys
sys.path.insert(0, 'libs')
sys.path.append('/home/tim/google_appengine/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
