from django.contrib import admin
from django.urls import path

from balance.views import PagosListView


urlpatterns = [
    path('list_all_payments/',PagosListView.as_view()),
]
