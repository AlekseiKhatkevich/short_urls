import django_redis
import redis.exceptions
from celery import shared_task
from celery.utils.log import get_task_logger
from django.utils import timezone

from bitly.models import UrlModel
from short_urls import constants

logger = get_task_logger(__name__)


@shared_task(
    autoretry_for=(redis.exceptions.RedisError,),
    retry_backoff=True,
    max_retries=30,
)
def clean_old_urls(interval: int = constants.DEFAULT_CLEANUP_INTERVAL) -> str:
    """
    :param interval: Интервал в днях. Записи имеющие дату создания старше текущего момента минус
    данный интервал будут удалены.
    :return: Кол-во удаленных записей.
    """
    now = timezone.now()
    time_threshold = now - timezone.timedelta(days=interval)
    entries_to_delete = UrlModel.objects.filter(creation_datetime__lt=time_threshold)
    deleted, _ = entries_to_delete.delete()

    # Удаляем закешированные респонсы редиректов во избежания показа удаленных урлов.
    if deleted:
        redis_client = django_redis.get_redis_connection()
        redis_client.flushdb()

    return f'Deleted {deleted} old entries'
