from django.contrib import admin
from .models import *

# Register your models here.
# Also include any admin panel modules you want, such as
# search function, list of columns to display, etc
# for each model


class InventoryAdmin(admin.ModelAdmin):
    list_filter = ('location', 'dept')
    list_display = ['location', 'dept', 'serial_num', 'inv_num']
    search_fields = ('location', 'dept', 'serial_num', 'inv_num')


class ConsumablesAdmin(admin.ModelAdmin):
    list_filter = ('ID_inv__inv_num', 'typeOf', 'brand')
    list_display = ('ID_inv', 'typeOf', 'brand')
    search_fields = ('ID_inv__inv_num', 'typeOf', 'brand')


class ItemTypeAdmin(admin.ModelAdmin):
    list_filter = ('typeOf', 'model', 'brand', 'color', 'vga', 'hdmi',
                   'display_port', 'screen_size', 'os', 'ram', 'cpu', 'driveType', 'driveSize')
    list_display = ['ID_inv', 'typeOf', 'model', 'brand', 'color', 'vga', 'hdmi',
                    'display_port', 'screen_size', 'os', 'ram', 'cpu', 'driveType', 'driveSize']
    # If you look up on foreign key fields, make sure to also reference the
    # other model field that it points to, with '__' notation
    # otherwise, you'll get a 'Related Field got invalid lookup: icontains'
    # because icontains search function only accepts CharField or TextField,
    # not classes referenced by foreign keys
    search_fields = ['ID_inv', 'typeOf', 'model', 'brand', 'color', 'vga', 'hdmi',
                     'display_port', 'screen_size', 'os', 'ram', 'cpu', 'driveType', 'driveSize']


class HistoryAdmin(admin.ModelAdmin):
    list_filter = ('date', 'location', 'user',
                   'os', 'ram', 'cpu', 'driveType', 'driveSize')
    list_display = ('ID_inv', 'date', 'location', 'user',
                    'job_notes', 'os', 'ram', 'cpu', 'driveType', 'driveSize')
    search_fields = ('ID_inv', 'date', 'location', 'user',
                     'job_notes', 'os', 'ram', 'cpu', 'driveType', 'driveSize')


class RequestAdmin(admin.ModelAdmin):
    # This filter shows all users with their related requests
    list_filter = ('ID_user__name',)
    list_display = ('ID_inv', 'ID_user', 'date', 'assignedTo')
    search_fields = ('ID_inv__inv_num', 'ID_user', 'date', 'assignedTo')


class UserRegularAdmin(admin.ModelAdmin):
    list_filter = ('dept', 'position')
    list_display = ('name', 'dept', 'position', 'email')
    search_fields = ('name', 'dept', 'position', 'email')


class UserTechAdmin(admin.ModelAdmin):
    list_filter = ('dept', 'position')
    list_display = ('name', 'dept', 'position', 'email', 'roles')
    search_fields = ('name', 'dept', 'position', 'email', 'roles')


class TicketAdmin(admin.ModelAdmin):
    # This filter shows all user names, and their related tickets
    # SELECT * FROM Ticket t
    # INNER JOIN Request req ON t.ID_req=req.ID_req
    # INNER JOIN UserRegular ur ON req.ID_user=ur.ID_user
    list_filter = ('ID_req__ID_user__name',)
    list_display = ('ID_req', 'ID_tech', 'assigned',
                    'dateCreation', 'dateAssign', 'dateFinish')
    search_fields = ('ID_req__date', 'ID_tech__name', 'assigned',
                     'dateCreation', 'dateAssign', 'dateFinish')


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Consumables, ConsumablesAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(UserRegular, UserRegularAdmin)
admin.site.register(UserTech, UserTechAdmin)
admin.site.register(Ticket, TicketAdmin)
