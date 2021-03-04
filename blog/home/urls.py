from django.urls import path


from .views import showpost, PostCreateView, index

urlpatterns = [
    path('add/', PostCreateView.as_view(), name='add'),
    path('home/', showpost, name='showpost'),
    path('', index)
]