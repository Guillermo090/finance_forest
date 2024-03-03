from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from  django.views import generic
from cliente.models import ClCliente

# Create your views here.
class ClientListView(generic.ListView):
    model = ClCliente
    template_name = 'cliente/list_all.html'
    context_object_name = 'clients'
    paginate_by = 5

class ClientMinorListView(generic.ListView):
    template_name = 'cliente/list_minors_client.html'
    context_object_name = 'clients'
    queryset = ClCliente.objects.filter(fecha_nacimiento__gte='2006-03-03')


class ClientSearchListView(generic.ListView):
    template_name = 'cliente/list_search_client.html'
    context_object_name = 'clients'
    queryset = ClCliente.objects.filter(fecha_nacimiento__gte='2006-03-03')
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        name_to_filter = self.request.GET.get('name','')
        queryset = ClCliente.objects.filter(nombres__contains=name_to_filter)
        return queryset
    


class CreateClientCreateView(generic.CreateView):
    template_name = 'cliente/create_client.html'
    model = ClCliente
    fields = ('__all__')
    success_url = '.'