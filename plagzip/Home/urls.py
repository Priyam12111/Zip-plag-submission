from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
    path('', views.Index,name='home'),
    path('upload_file', views.upload_file,name='fileup'),
    path('download_file', views.download_file,name='filedn'),
    path('update_text/', views.update_text, name='update_text'),
]
