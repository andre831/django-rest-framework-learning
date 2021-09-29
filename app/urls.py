from app.views import tenis_list, tenis_sett

from django.urls import path


urlpatterns = [
    path('', tenis_list),
    path('<int:pk>/', tenis_sett)
]