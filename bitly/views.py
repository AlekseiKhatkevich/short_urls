from rest_framework import generics

from bitly import serializers as bitly_serializers


class UrlCreateView(generics.CreateAPIView):
    """
    
    """
    serializer_class = bitly_serializers.CreateUrlSerializer
