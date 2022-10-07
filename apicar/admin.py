from email.mime import image
from django.contrib import admin
from .models import Auto
from django.utils.html import format_html
# Register your models here.


class AutoAdmin(admin.ModelAdmin):
    
    list_display = (
                    'id',
                    'brand',
                    'model',
                    'year',
                    'price',
                    'image',
                    )

admin.site.register(Auto,AutoAdmin)