from django.db import models
from buyers.models import Buyer
from django.contrib.auth.models import User

# Create your models here.


class Inflow(models.Model):
    TYPE_PAYMENTS_CHOICES = (
        ('PIX', 'PIX'),
        ('Diheiro', 'Dinheiro'),
        ('Cartão', 'Cartão'),
    )
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, 
        related_name="inflows",blank=True, null=True
    )
    value = models.FloatField()
    date = models.DateTimeField()
    type_payment = models.CharField(max_length=20, 
        choices=TYPE_PAYMENTS_CHOICES
        )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
        related_name="inflow_created_by", null=True
    )
    description = models.TextField(max_length=500, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.user} criou uma venda para {self.buyer} de R${self.value} no dia {self.date.strftime('Y%-%m-%d')}"
