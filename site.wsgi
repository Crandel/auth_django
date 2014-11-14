import os
import sys
import os.path

sys.stdout = sys.stderr

# *** Code from http://code.google.com/p/modwsgi/wiki/VirtualEnvironments to enable virtualenv site-packages ***

ALLDIRS = ['/home/kuddevurl/virtual/lib/python2.6/site-packages']

#import sys
import site

# Remember original sys.path.
prev_sys_path = list(sys.path)

# Add each new site-packages directory.
for directory in ALLDIRS:
  site.addsitedir(directory)

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

sys.path.insert(0, '/home/kuddevurl')
sys.path.insert(0, '/home/kuddevurl/sitco')
os.environ['DJANGO_SETTINGS_MODULE'] = 'kud.server_settings'
os.environ['PYTHON_EGG_CACHE'] = '/home/kuddevurl/.python-eggs'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
import monitor
monitor.start(interval=1.0)
