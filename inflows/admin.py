from django.contrib import admin
from inflows.models import Inflow

# Register your models here.


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ("buyer", "value", "created_on")
    search_fields = ("buyer__name",)
    exclude = ('user',)
