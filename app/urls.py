from app.views import tenis_list

from django.urls import path


urlpatterns = [
    path('', tenis_list)
]