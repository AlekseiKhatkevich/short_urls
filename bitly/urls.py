from django.urls import path, register_converter

from bitly import views
from short_urls import converters

register_converter(converters.ShortUrlConverter, 'url_code')
register_converter(converters.CustomUUIDConverter, 'uuid')

urlpatterns = [
    path('create/', views.UrlCreateView.as_view(), name='create_url',),
    path('redirect/<url_code:url_code>/', views.UrlRedirectDetailView.as_view(), name='redirect_url',),
    path('user_urls/<uuid:user_id>/', views.UserShortUrlsListView.as_view(), name='user_urls',),
]
