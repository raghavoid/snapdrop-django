from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('upload/',views.upload,name='upload'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout'),
    path('cleanup-database/', views.cleanup_database,name='cleanup_database'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]