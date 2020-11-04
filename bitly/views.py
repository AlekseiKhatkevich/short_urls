from rest_framework import generics

from bitly import serializers as bitly_serializers


class UrlCreateView(generics.CreateAPIView):
    """
    Вью для создания записи в БД содержащей пару полный урл и урл код, UUID
    юзера и дату создания записи. Примеры реквеста/ респонса в соотв. сериалайзере.
    """
    serializer_class = bitly_serializers.CreateUrlSerializer


class UrlRedirectDetailView(generics.RetrieveAPIView):
    """
    Вью для отдачи полного урла по урл коду.Примеры реквеста/ респонса в соотв. сериалайзере.
    """
    serializer_class = bitly_serializers.UrlRedirectDetailSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    lookup_field = 'url_code'


class UserShortUrlsListView(generics.ListAPIView):
    """
    Лист вью для отдачи пар полный урл / урл код принадлежащих одному юзеру.
    Примеры реквеста/ респонса в соотв. сериалайзере.
    Пагинация limit/offset по 50 записей.
    """
    serializer_class = bitly_serializers.UserShortUrlsListSerializer
    model = serializer_class.Meta.model
    lookup_field = 'user_id'

    def get_queryset(self):
        user_id = self.kwargs[self.lookup_field]
        self.queryset = self.model.objects.filter(user_id=user_id).order_by('creation_datetime')

        return super().get_queryset()




