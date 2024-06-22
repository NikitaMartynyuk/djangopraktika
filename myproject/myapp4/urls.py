from django.urls import path
from .views import user_form


urlpatterns = [
    path('user/', user_form, name='home'),
]
