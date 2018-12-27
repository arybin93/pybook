from django.urls import path, include
from . import views

from .router import api_urls

urlpatterns = [
    path('api/v1/', include(api_urls)),
    path('', views.index, name='index'),
]