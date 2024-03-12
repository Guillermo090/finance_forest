from django.contrib import admin
from django.urls import path

from balance.views import PagosListView, PagosFormView, PaymentSearchListView

app_name = 'balance'

urlpatterns = [
    path('list_all_payments/',PagosListView.as_view()),
    path('form_balances/',PagosFormView.as_view()),
    path('list_search_payment/',PaymentSearchListView.as_view()),
]
