from django.contrib import admin
from .models import CsvData

@admin.register(CsvData)
class CsvDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'created_at')
    readonly_fields = ('id', 'created_at')
