from django.shortcuts import render
from  django.views import generic
from cliente.models import ClCliente

# Create your views here.
class ClientListView(generic.ListView):
    model = ClCliente
    template_name = 'cliente/list_all.html'
    context_object_name = 'clients'