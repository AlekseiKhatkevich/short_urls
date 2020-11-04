from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path('short_urls/', include('bitly.urls')),
]
# API схема в формате swagger, redoc а так же в чистом josn и yaml
schema_view = get_schema_view(
   openapi.Info(
      title='Short urls API',
      default_version='v1',
      description='Converts full url to short url',
      contact=openapi.Contact(email='hardcase@inbox.ru'),
      license=openapi.License(name='Free'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
