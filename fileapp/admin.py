from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import CustomUser

admin.site.register(CustomUser)
admin.site.register(LogEntry)