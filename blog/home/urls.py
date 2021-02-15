from django.urls import path


from .views import showpost, PostCreateView

urlpatterns = [
    path('add/', PostCreateView.as_view(), name='add'),
    path('', showpost, name='showpost'),
]