from django.contrib import admin
from first.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active',)
    list_filter = ('is_active',)
    list_select_related = True
    search_fields = ('name',)

admin.site.register(Event, EventAdmin)
