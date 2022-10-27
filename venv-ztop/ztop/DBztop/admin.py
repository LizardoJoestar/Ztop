from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Consumables)
admin.site.register(ItemType)
admin.site.register(History)
admin.site.register(Inventory)
admin.site.register(Request)
admin.site.register(UserRegular)
admin.site.register(UserTech)
admin.site.register(Ticket)