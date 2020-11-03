from django.urls import path
from bitly import views


urlpatterns = [
    path('create/', views.UrlCreateView.as_view(), name='create_url',),
]