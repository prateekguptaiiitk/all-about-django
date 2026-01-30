from django.contrib import admin

from .models import Message, MessageBoard

# Register your models here.
admin.site.register(MessageBoard)
admin.site.register(Message)
