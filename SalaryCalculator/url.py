from django.urls import path
from .views import Home, Calculate
urlpatterns = [
    path('', Home, name="Home"),
    path('results', Calculate)
]
