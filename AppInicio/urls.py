from django.urls import path
from AppInicio.views import *

urlpatterns = [
    path('', inicio, name = "inicio"),
    path('login/', login, name = "login"),
    path('registro/', registro, name = "registro"),
]