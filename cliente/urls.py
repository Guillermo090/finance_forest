from django.contrib import admin
from django.urls import path

from cliente.views import ClientListView


urlpatterns = [
    path('list_all/',ClientListView.as_view())
]