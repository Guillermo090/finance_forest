from django import forms
from cliente.models import ClCliente
from .models import BaRegistroPago

class PagosForm(forms.Form):

    fecha_pago = forms.DateTimeField(required=False)
    date_created = forms.DateTimeField(required=False, widget=forms.HiddenInput())
    date_updated = forms.DateTimeField(required=False, widget=forms.HiddenInput())
    deudor = forms.ModelChoiceField(queryset=ClCliente.objects.all(),label="Nombres")
    detalle_pago = forms.CharField(
        max_length=500, 
        widget=forms.Textarea(
            attrs={'rows': 5, 'cols': 5, 'class': 'w-96'}))
    acreedor = forms.ModelChoiceField(queryset=ClCliente.objects.all(), required=False)  # Selecciona tus propias opciones
    pago_realizado = forms.BooleanField(initial=False, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deudor'].label_from_instance = self.label_from_instance_custom


    def label_from_instance_custom(self, obj):
        return f'{obj.nombres}'