from django.contrib import admin
from outflows.models import Outflow
# Register your models here.


@admin.register(Outflow)
class OutflowAdmin(admin.ModelAdmin):
    list_display = ("category", "value", "created_on")
    search_fields = ("category__name",)
    exclude = ('user',)
