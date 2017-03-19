import os
import sys

path = '/home/hvoking/Murruga'

if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE']= 'Murruga.settings'

from django.core.wgsi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application()) 
