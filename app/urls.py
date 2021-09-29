from app.views import Tenis_List, Tenis_Details

from django.urls import path


urlpatterns = [
    path('', Tenis_List.as_view()),
    path('<int:pk>/', Tenis_Details.as_view())
]