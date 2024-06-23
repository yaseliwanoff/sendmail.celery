import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_mail.settings')  # потому что в файле settings будут настройки для celery

app = Celery('send_mail')
app.config_from_object('django.conf:settings', namespace='CELERY')  # автоматическое подцепление переменных с namespace'ом
app.autodiscover_tasks()  # автоматически подцепляем таски

# celery beat tasks

app.conf.beat_schedule = {
    'send-spam-every-10-minute': {
        'task': 'main.tasks.send_beat_email',
        'schedule': crontab(minute='*/10'),
    },
}
