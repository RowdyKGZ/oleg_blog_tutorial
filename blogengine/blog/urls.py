from django.contrib import admin
from django.urls import path, include

from .views import posts_list

urlpatterns = [
    path('', posts_list),
]