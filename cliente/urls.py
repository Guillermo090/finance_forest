from django.contrib import admin
from django.urls import path

from cliente.views import ClientListView, ClientMinorListView, ClientSearchListView, CreateClientCreateView

app_name = 'cliente'

urlpatterns = [
    path('list_all/',ClientListView.as_view()),
    path('list_minors/',ClientMinorListView.as_view()),
    path('list_search_client/',ClientSearchListView.as_view()),
    path('create_client/',CreateClientCreateView.as_view())
]
