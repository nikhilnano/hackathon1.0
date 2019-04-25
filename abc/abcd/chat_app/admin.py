from django.contrib import admin

# Register y1our models here.
from .models import chat
from .models import username
admin.site.register(chat)
admin.site.register(username)