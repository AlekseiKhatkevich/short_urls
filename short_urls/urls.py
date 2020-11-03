from django.urls import path, include

urlpatterns = [
    path('short_urls/', include('bitly.urls')),
]
