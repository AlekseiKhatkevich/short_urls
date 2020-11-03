from rest_framework import generics

from bitly import serializers as bitly_serializers


class UrlCreateView(generics.CreateAPIView):
    """
    
    """
    serializer_class = bitly_serializers.CreateUrlSerializer


class UrlRedirectDetailView(generics.RetrieveAPIView):
    """

    """
    serializer_class = bitly_serializers.UrlRedirectDetailSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    lookup_field = 'url_code'


class UserShortUrlsListView(generics.ListAPIView):
    """

    """
    serializer_class = bitly_serializers.UserShortUrlsListSerializer
    model = serializer_class.Meta.model
    lookup_field = 'user_id'

    def get_queryset(self):
        self.queryset = self.model.objects.filter(user_id=self.kwargs[self.lookup_field])

        return super().get_queryset()




