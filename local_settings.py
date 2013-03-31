import os
DEBUG = not (os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine') or os.getenv('SETTINGS_MODE') == 'prod')

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'google.appengine.ext.django.backends.rdbms',
            'INSTANCE': 'coconutrandom:dt-mezzanine',
            'NAME': 'mezzanine',
            #'OPTIONS': {
            #    'driver': 'google.storage.speckle.python.api.rdbms_googleapi',
            #}
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'google.appengine.ext.django.backends.rdbms',
            'INSTANCE': 'coconutrandom:dt-mezzanine',
            'NAME': 'mezzanine',
        }
    }
