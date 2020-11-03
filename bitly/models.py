import functools

from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CharField
from django.db.models.functions import Length
from django.utils.crypto import get_random_string
from short_urls import constants
from bitly import validators

CharField.register_lookup(Length)


class UrlModel(models.Model):
    """

    """

    user_id = models.UUIDField(
        verbose_name='user unique identifier',
        db_index=True,
        validators=[
            validators.UUIDValidator(4)
        ]
    )
    full_url = models.URLField(
        verbose_name='full url',
        db_index=True,
    )
    url_code = models.CharField(
        verbose_name='short_url',
        unique=True,
        max_length=7,
        default=functools.partial(get_random_string, 7),
        validators=[MinLengthValidator(7), ],
    )
    creation_datetime = models.DateTimeField(
        verbose_name='creation datetime',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'url'
        verbose_name_plural = 'urls'
        constraints = (
            models.CheckConstraint(
                name='url_code_length_check',
                check=models.Q(url_code__length=7)
            ),
            models.CheckConstraint(
                name='user_id_uuid_check',
                check=models.Q(user_id__regex=constants.UUID4_REGEX),
            ),
            models.CheckConstraint(
                name='full_url_check',
                check=models.Q(full_url__regex=constants.URL_REGEX),
            ),
        )

    def __repr__(self):
        return f'{self.pk=} ~ {self.user_id=} ~ {self.url_code=}'

    def __str__(self):
        return f'{self.pk}, user - {self.user_id}, short_url - {self.url_code}'

    def save(self, fc=True, *args, **kwargs):
        if fc:
            self.full_clean()
        super().save(*args, **kwargs)
