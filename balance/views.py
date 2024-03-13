from django.views import generic
from django.db.models import Q
from .models import BaRegistroPago
from django.db.models.query import QuerySet
from typing import Any
from .forms import PagosForm
import datetime
from zoneinfo import ZoneInfo

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


class PagosFormView(generic.FormView):
    model = BaRegistroPago
    template_name = 'balance/form_balances.html'
    context_object_name = 'pagos'
    paginate_by = 10

    form_class = PagosForm
    success_url = 'balance/list_all_balances.html'


class PaymentSearchListView(generic.ListView):
    template_name = 'balance/list_search_payment.html'
    context_object_name = 'payments'
    queryset = BaRegistroPago.objects.all()
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        acreedor_to_filter = self.request.GET.get('acreedor','')
        deudor_to_filter = self.request.GET.get('deudor','')
        date_from = self.request.GET.get('date_from','')
        date_from = '2000-01-01' if date_from == '' else date_from
        date_from_datetime = datetime.datetime.strptime(date_from, '%Y-%m-%d').replace(tzinfo=ZoneInfo("America/Santiago"))
        date_to = self.request.GET.get('date_to','')
        date_to = '2100-01-01' if date_to == '' else date_to
        date_to_datetime = datetime.datetime.strptime(date_to, '%Y-%m-%d').replace(tzinfo=ZoneInfo("America/Santiago"))
        is_pay = False if  self.request.GET.get('is_pay') == 'False' else self.request.GET.get('is_pay')
        queryset = BaRegistroPago.objects.filter(
            Q(acreedor__nombres__contains=acreedor_to_filter) 
            | Q(acreedor__apellidos__contains=acreedor_to_filter),
            Q(deudor__nombres__contains=deudor_to_filter) 
            | Q(deudor__apellidos__contains=deudor_to_filter),
            Q(date_created__gte=date_from_datetime),Q(date_created__lte=date_to_datetime)
        )
        if is_pay != 'all':
            is_pay = bool(is_pay)
            queryset = queryset.filter(
                Q(pago_realizado=is_pay)
            )
        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        acreedor_to_filter = self.request.GET.get('acreedor','')
        deudor_to_filter = self.request.GET.get('deudor','')
        date_from = self.request.GET.get('date_from','')
        date_to = self.request.GET.get('date_to','')
        is_pay = self.request.GET.get('is_pay',False)

        context.update({
            "acreedor" : acreedor_to_filter,
            "deudor" : deudor_to_filter,
            "date_from" : date_from,
            "date_to" : date_to,
            "is_pay" : is_pay,
        })

        return context