"""
WSGI config for schoolAdminSystem project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolAdminSystem.settings')
wsgi_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.dirname(wsgi_dir)
sys.path.append(project_dir)
sys.path.append('/home/testone/testone')
project_settings = os.path.join(project_dir,'settings')
os.environ['PYTHON_EGG_CACHE'] = '/home/testone/testone/.python-egg'

application = get_wsgi_application()
