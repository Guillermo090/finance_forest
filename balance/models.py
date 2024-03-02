from django.db import models
from cliente.models import ClCliente




class BaRegistroPago(models.Model):
    fecha_pago = models.DateTimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    deudor = models.ForeignKey(ClCliente, on_delete=models.CASCADE, related_name='pagos_realizados')
    detalle_pago = models.TextField(max_length=500)

    class Meta:
        db_table = 'ba_registro_pago' 
        verbose_name = 'Registro de Pago'
        verbose_name_plural = 'Registros de Pagos'

