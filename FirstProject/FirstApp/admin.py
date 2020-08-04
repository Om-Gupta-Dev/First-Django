from django.contrib import admin

from FirstApp.models import Message, upload

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','date' , 'name','mail']

# Register your models here.

admin.site.register(Message , MessageAdmin)
admin.site.register(upload )