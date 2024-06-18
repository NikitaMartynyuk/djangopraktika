from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp1.urls')),
    path('', include('myapp3.urls')),
]
