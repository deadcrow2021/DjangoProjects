from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]


# Connfigure Admin Titles
admin.site.site_header = 'My Administration Page'
admin.site.site_title = 'My Site Administration'
admin.site.index_title = 'My Admin Area'