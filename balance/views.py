from django.views import generic
from .models import BaRegistroPago
from django.db.models.query import QuerySet
from typing import Any
# Create your views here.
 

class PagosListView(generic.ListView):
    model = BaRegistroPago
    template_name = 'balance/list_all_balances.html'
    context_object_name = 'pagos'
    paginate_by = 10

    # def get_queryset(self) -> QuerySet[Any]:
    #     name_to_filter = self.request.GET.get('name','')
    #     queryset = BaRegistroPago.objects.filter(acreedor__nombres__contains=name_to_filter)
    #     return queryset