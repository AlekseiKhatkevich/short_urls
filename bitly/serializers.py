from collections import defaultdict

from rest_framework import serializers

from bitly import models as bitly_models


class CreateUrlSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = bitly_models.UrlModel
        fields = ('user_id', 'full_url', 'url_code',)
        extra_kwargs = dict(
            user_id={'write_only': True},
            full_url={'write_only': True},
        )

        model_error_messages = {
            field: bitly_models.UrlModel._meta.get_field(field).error_messages for field in fields
        }
        for field, messages in model_error_messages.items():
            extra_kwargs = defaultdict(dict, extra_kwargs)
            extra_kwargs[field]['error_messages'] = messages


class UrlRedirectDetailSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = bitly_models.UrlModel
        fields = ('full_url',)
        read_only_fields = fields


class UserShortUrlsListSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = bitly_models.UrlModel
        fields = ('user_id', 'url_code',)
        read_only_fields = fields
