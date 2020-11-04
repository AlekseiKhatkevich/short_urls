from celery.schedules import crontab


broker_url = 'redis://127.0.0.1:6379/3'
task_serializer = 'pickle'
accept_content = ['pickle']
timezone = 'Europe/Moscow'
broker_transport_options = {'visibility_timeout': 300}
enable_utc = True
