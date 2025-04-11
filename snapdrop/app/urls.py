from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('upload/',views.upload,name='upload'),
    path('login/',views.login,name='login'),
]