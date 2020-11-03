from django.urls import path, register_converter
from bitly import views
from django.urls.converters import StringConverter, UUIDConverter


class ShortUrlConverter(StringConverter):
    """

    """
    regex = r'[^/]{7}'


class CustomUUIDConverter(UUIDConverter):
    """

    """
    regex = r'[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}'


register_converter(ShortUrlConverter, 'url_code')
register_converter(CustomUUIDConverter, 'uuid')

urlpatterns = [
    path('create/', views.UrlCreateView.as_view(), name='create_url',),
    path('redirect/<url_code:url_code>/', views.UrlRedirectDetailView.as_view(), name='redirect_url',),
    path('user_urls/<uuid:user_id>/', views.UserShortUrlsListView.as_view(), name='user_urls',),
]
