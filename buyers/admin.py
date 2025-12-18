from django.contrib import admin
from buyers.models import Buyer
# Register your models here.


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ("name", "cnpj")
    search_fields = ("name", )
