from collections import defaultdict

from rest_framework import serializers

from bitly import models as bitly_models


class CreateUrlSerializer(serializers.ModelSerializer,):
    """
    Сериалайзер для создания записи в модели 'UrlModel'.
    Пример POST запроса:
    {
        'user_id': '1a9c276a-e671-4308-8ce3-d5c2f34e121a',
        'full_url': 'https://docs.djangoproject.com/en/3.1/ref/request-response/',
        'url_code': 'rTg45Sd',
    }
    url_code - опционально. При отсутсвии происходит автогенерация.

    Пример ответа - {
    'url_code': 'Dmt7KgN'
    }
    """

    class Meta:
        model = bitly_models.UrlModel
        fields = ('user_id', 'full_url', 'url_code',)
        extra_kwargs = dict(
            user_id={'write_only': True},
            full_url={'write_only': True},
        )

        # Записываем error_messages из модели в сериалайзер. В дальнейшем можно сделать миксин если
        # будет использоваться более одного раза.
        model_error_messages = {
            field: bitly_models.UrlModel._meta.get_field(field).error_messages for field in fields
        }
        for field, messages in model_error_messages.items():
            extra_kwargs = defaultdict(dict, extra_kwargs)
            extra_kwargs[field]['error_messages'] = messages


class UrlRedirectDetailSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для отдачи полного урла по короткому коду урла.
    код урла передается через GET парамеиры.
    Пример - /short_urls/redirect/eFHvvOw/ GET:
    Пример респонса {
    "full_url": "http://127.0.0.1:8000/short_urls/create/"
    }
    """
    class Meta:
        model = bitly_models.UrlModel
        fields = ('full_url',)
        read_only_fields = fields


class UserShortUrlsListSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для отдачи пар полный урл: код урла принадлежащих одному юзеру.
    UUID юзура передается через GET параметры.
    Пример реквеста - short_urls/user_urls/e1b73a2847bc423fa53cd1935a2713ad/ GET
    Пример респонса -{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "full_url": "http://127.0.0.1:8000/short_urls/create/",
            "url_code": "2822888"
        },
        {
            "full_url": "http://127.0.0.1:8000/short_urls/create/",
            "url_code": "1111111"
        }
    ]
    }
    """
    class Meta:
        model = bitly_models.UrlModel
        fields = ('full_url', 'url_code',)
        read_only_fields = fields
