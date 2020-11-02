from django.db import models
from django.db.models import Q


class UrlModel(models.Model):
    """

    """
    user_id = models.UUIDField(
        verbose_name='user unique identifier',
        db_index=True,
    )
    full_url = models.URLField(
        verbose_name='full url',
    )
    short_url = models.URLField(
        verbose_name='short_url',
        unique=True,
    )
    creation_datetime = models.DateTimeField(
        verbose_name='creation datetime',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'url'
        verbose_name_plural = 'urls'
        # constraints = [
        #     models.CheckConstraint(
        #         name='full_url_check',
        #         check=Q(full_url__regex=r'^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?', ),
        #     ),
        # ]

    def __repr__(self):
        return f'{self.pk=} ~ {self.user_id=} ~ {self.short_url=}'

    def __str__(self):
        return f'{self.pk}, user - {self.user_id}, short_url - {self.short_url}'

    def save(self, fc=True, *args, **kwargs):
        if fc:
            self.full_clean()
        super().save(*args, **kwargs)

