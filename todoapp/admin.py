from django.contrib import admin
from .models import todo

admin.site.register(todo)

class todoAdmin(admin.ModelAdmin):
    list_display = ('topic','venue','slot')

# Register your models here.
