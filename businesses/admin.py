from django.contrib import admin
from .models import Business

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'zip_code')
    search_fields = ('name', 'city', 'state', 'zip_code')
