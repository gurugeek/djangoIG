import os
import channels.asgi
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_ig.settings")
channel_layer = channels.asgi.get_channel_layer()


