from rest_framework import serializers

from bitly import models as bitly_models


class CreateUrlSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = bitly_models.UrlModel
        fields = ('user_id', 'full_url', 'url_code', )
        extra_kwargs = {
            'user_id': {'write_only': True},
            'full_url': {'write_only': True},
        }