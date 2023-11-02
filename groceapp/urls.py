from django.urls import path
from . import views



urlpatterns = [
    path('reg',views.userform),
    path('home',views.gg,name='home')
]
