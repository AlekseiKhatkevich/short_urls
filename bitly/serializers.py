from rest_framework import serializers

from bitly import models as bitly_models
from short_urls import error_messages


class CreateUrlSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = bitly_models.UrlModel
        fields = ('user_id', 'full_url', 'url_code',)

        extra_kwargs = dict.fromkeys(
            ('user_id', 'full_url'),
            {'write_only': True},
        )

        model_error_messages = {
            field: bitly_models.UrlModel._meta.get_field(field).error_messages for field in fields
        }
        for field, messages in model_error_messages.items():
            extra_kwargs.setdefault(field, dict())['error_messages'] = messages
