import os, sys

sys.path.append('/ndnp/public3/chronam')
sys.path.append('/ndnp/public3/chronam/chronam')
os.environ['DJANGO_SETTINGS_MODULE'] = 'chronam.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
