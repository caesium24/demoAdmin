from django.contrib import admin
from .models import ticket
from .models import admins

class ticketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'site', 'name', 'date')
    list_display_links = ('id', 'title')
    list_filter = ('name', 'site')

admin.site.register(ticket, ticketAdmin)
admin.site.register(admins)

