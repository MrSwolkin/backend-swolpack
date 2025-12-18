from django.db import models



class Buyer(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
