import functools

from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CharField
from django.db.models.functions import Length
from django.utils.crypto import get_random_string

from bitly import validators
from short_urls import constants, error_messages

CharField.register_lookup(Length)


class UrlModel(models.Model):
    """
    Модель представляет одну запись пары полный урл: код сокращенного урла + метаинформацию.

    user_id - уникальный идентификатор юзера пересылаемый фронтэндом.
        формат - UUID4 (возвращает функция uuid.uuid4())
        примеры:
            0ad98760-3558-4295-9d15-4b28870b0490
            dce83a95-ebfb-44aa-b826-05195040a59b
            1a9c276a-e671-4308-8ce3-d5c2f34e121a

    full_url - полный url, который будет храниться в паре с url_code.

    url_code - код урла, который отправляется фронту и там конкатенируется с урлом
        домена.
        Пример:
           http://domen.com +  XJye11v = http://domen.com/XJye11v
        Полный урл в формате домен + код не хранится, чтобы сделать данные в базе
        независимыми при возможной смене домена.
        - формат(автогенерация): 7 символов (цифры + строчные и заглавные буквы англ.
        алфавита). Пользователю разрешается вводить кастомный код длинной 7 символов содержащий
        любые возможные символы в тч и спецсимволы.
        -примеры:
            UB1k7aF
            UpADYct
            Wz60fKd

    creation_datetime - время создания записи в БД (автогенерация)
    """
    user_id = models.UUIDField(
        verbose_name='user unique identifier',
        db_index=True,
        validators=[
            validators.UUIDValidator(4)
        ],
        error_messages={
            'invalid': error_messages.WRONG_UUID.message,
        },
    )
    full_url = models.URLField(
        verbose_name='full url',
        error_messages={
            'invalid': error_messages.WRONG_FULL_URL.message,
        },
    )
    url_code = models.CharField(
        verbose_name='url_code',
        db_index=True,
        unique=True,
        max_length=7,
        default=functools.partial(get_random_string, 7),
        validators=[MinLengthValidator(7), ],
        error_messages={
            'unique': error_messages.UNIQUE_URL_CODE.message,
            **dict.fromkeys(
                     ('min_length', 'max_length',),
                     error_messages.WRONG_URL_CODE_LEN.message,
                 )}
    )
    creation_datetime = models.DateTimeField(
        verbose_name='creation datetime',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'url'
        verbose_name_plural = 'urls'
        constraints = (
            # Длинна url_code должна равняться 7-ми символам.
            models.CheckConstraint(
                name='url_code_length_check',
                check=models.Q(url_code__length=7)
            ),
            # Данные сохраняемые в user_id должны быть валидной строкой UUID4.
            models.CheckConstraint(
                name='user_id_uuid_check',
                check=models.Q(user_id__regex=constants.UUID4_REGEX),
            ),
            # Проверка full_url на соответсвию формату URL.
            models.CheckConstraint(
                name='full_url_check',
                check=models.Q(full_url__regex=constants.URL_REGEX),
            ),
        )

    def __repr__(self):
        return f'{self.pk=} ~ {self.user_id=} ~ {self.url_code=}'

    def __str__(self):
        return f'{self.pk}, user - {self.user_id}, url_code - {self.url_code}'

    def save(self, fc=True, *args, **kwargs):
        """
        Метод 'full_clean' по дефолту включен для валидации на уровне модели.
        """
        if fc:
            self.full_clean()
        super().save(*args, **kwargs)
