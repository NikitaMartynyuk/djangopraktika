from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('class1/', include('myapp1.urls')),
    path('class2/', include('myapp2.urls')),
    path('order/', include('myapp3.urls')),
]

