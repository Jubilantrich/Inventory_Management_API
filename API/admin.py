from django.contrib import admin

from .models import Inventory


# Register your models here.


class InventoryAdmin(admin.ModelAdmin):
    list_display = ("id","name", "quantity" , "price", "user_id")
    search_fields = ("name",)
    list_filter = ("price",) 


admin.site.register(Inventory, InventoryAdmin)

