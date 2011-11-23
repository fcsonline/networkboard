from django.contrib import admin
from nettools.networkboard.models import Node, Service

class NodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'ip')

admin.site.register(Node, NodeAdmin)
admin.site.register(Service)
