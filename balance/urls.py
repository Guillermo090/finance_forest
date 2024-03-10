from django.contrib import admin
from django.urls import path

from balance.views import PagosListView, PagosFormView


urlpatterns = [
    path('list_all_payments/',PagosListView.as_view()),
    path('form_balances/',PagosFormView.as_view()),
]
