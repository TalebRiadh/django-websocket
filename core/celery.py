from __future__ import absolute_import, unicode_literals
import os 
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "core.settings")

app = Celery("core")

app.config_from_object('django.conf:settings', namespace="CELERY")

app.conf.beat_schedule = {
    'get_news_3s': {
        'task': 'news.tasks.get_news',
        'schedule': 5.0
    }
}
app.autodiscover_tasks()