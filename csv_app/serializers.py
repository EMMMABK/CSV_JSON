from rest_framework import serializers
from .models import CsvData

class CsvDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsvData
        fields = ('id', 'file', 'created_at')
        read_only_fields = ('id', 'created_at')
