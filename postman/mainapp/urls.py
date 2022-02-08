from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('add_email/', views.add_email, name='add-email'),
    path('send/', views.add_email, name='send-to-emails'),
]
