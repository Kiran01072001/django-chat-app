# wsgi.py



import os
import sys

# Add your project directory to the sys.path
project_home = '/home/kiran01072001/django-chat-app/Chat Application/chat_project'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Activate your virtual env
activate_env = os.path.expanduser("/home/kiran01072001/.virtualenvs/myenv/bin/activate_this.py")
with open(activate_env) as f:
    exec(f.read(), dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')
application = get_wsgi_application()