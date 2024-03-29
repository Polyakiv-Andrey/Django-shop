import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_shop.settings')
app = Celery('django_shop', broker=settings.CELERY_BROKER_URL, broker_connection_retry_on_startup=True)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)