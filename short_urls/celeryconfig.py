from celery.schedules import crontab
from short_urls import constants

broker_url = 'redis://redis/3'
task_serializer = 'pickle'
accept_content = ['pickle']
timezone = 'Europe/Moscow'
broker_transport_options = {'visibility_timeout': 300}
enable_utc = True


beat_schedule = {
    # Удаление старых записей в ДБ модели UrlModel.
    'delete_old_db_entries': {
        'task': 'bitly.tasks.clean_old_urls',
        'schedule': crontab(hour=3, minute=9,),
        'args': (constants.DEFAULT_CLEANUP_INTERVAL,)
    },
}
