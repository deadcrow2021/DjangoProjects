from django.urls import path
from . import views

urlpatterns = [
    path('', views.fullList, name='todolist'),
    path('edit/<str:pk>', views.editList, name='edit'),
    path('delete/<str:pk>', views.deleteList, name='delete'),
]