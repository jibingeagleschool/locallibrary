from django import core
from django.contrib import admin
from django.urls import path, include
from django.urls import include



from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
]
