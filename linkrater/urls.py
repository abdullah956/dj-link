from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('links/', include('link.urls')),
    path('', include('core.urls')),
    path('', include('user.urls')),
]
