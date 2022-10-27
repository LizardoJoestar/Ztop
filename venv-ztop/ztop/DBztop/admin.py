from django.contrib import admin
from .models import *

# Register your models here.

class InventoryAdmin(admin.ModelAdmin):
    list_display = ['location', 'dept', 'serial_num', 'inv_num']
    search_fields = ('location', 'dept', 'serial_num', 'inv_num')

class ConsumablesAdmin(admin.ModelAdmin):
    list_display = ('ID_inv', 'typeOf', 'brand')
    search_fields = ('ID_inv', 'typeOf', 'brand')

class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('ID_inv', 'typeOf', 'model', 'brand', 'color')
    search_fields = ('ID_inv', 'typeOf', 'model', 'brand', 'color')

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('ID_inv', 'date', 'updated', 'user')
    search_fields = ('ID_inv', 'date', 'updated', 'user')

class RequestAdmin(admin.ModelAdmin):
    list_display = ('ID_inv', 'ID_user', 'date', 'assignedTo')
    search_fields = ('ID_inv', 'ID_user', 'date', 'assignedTo')
    
class UserRegularAdmin(admin.ModelAdmin):
    list_display = ('name', 'dept', 'position', 'email')
    search_fields = ('name', 'dept', 'position', 'email')

class UserTechAdmin(admin.ModelAdmin):
    list_display = ('name', 'dept', 'position', 'email', 'roles')
    search_fields = ('name', 'dept', 'position', 'email', 'roles')

class TicketAdmin(admin.ModelAdmin):
    list_display = ('ID_req', 'ID_tech', 'assigned', 'dateCreation', 'dateAssign', 'dateFinish')
    search_fields = ('ID_req', 'ID_tech', 'assigned', 'dateCreation', 'dateAssign', 'dateFinish')

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Consumables, ConsumablesAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(UserRegular, UserRegularAdmin)
admin.site.register(UserTech, UserTechAdmin)
admin.site.register(Ticket, TicketAdmin)