from django.contrib import admin
from .models import Item
# Register your models here.


@admin.register(Item)
class UserAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_num', 'product_type', 'product_description', 'product_category', 'status',
                    'unit_measure', 'packing_type',
                    )
