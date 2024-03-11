from django.db import models
from cliente.models import ClCliente




class BaRegistroPago(models.Model):
    fecha_pago = models.DateTimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    deudor = models.ForeignKey(ClCliente, on_delete=models.CASCADE, related_name='pagos_adeudor')
    detalle_pago = models.TextField(max_length=500)
    acreedor = models.ForeignKey(ClCliente, on_delete=models.CASCADE, related_name='pagos_acreedor',null=True)
    pago_realizado = models.BooleanField(default=False)

    class Meta:
        db_table = 'ba_registro_pago' 
        verbose_name = 'Registro de Pago'
        verbose_name_plural = 'Registros de Pagos'


class BaCtaInterna(models.Model):
    nombre_cta = models.CharField(max_length=150)
    monto_cta = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ba_cta_interna' 
        verbose_name = 'Cuenta Interna'
        verbose_name_plural = 'Cuentas Internas'