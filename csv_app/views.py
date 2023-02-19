import os
import json
import csv
from django.http import HttpResponse, Http404
from django.views.generic import View
from rest_framework import generics
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CsvData


class CsvDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsvData
        fields = ('id', 'file', 'created_at')
        read_only_fields = ('id', 'created_at')


class CsvView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('CSV View')


class CsvDataList(generics.ListCreateAPIView):
    queryset = CsvData.objects.all()
    serializer_class = CsvDataSerializer


class CsvDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CsvData.objects.all()
    serializer_class = CsvDataSerializer


class CsvDataDetailByFilename(APIView):
    def get_object(self, filename):
        try:
            return CsvData.objects.get(file__endswith=filename)
        except CsvData.DoesNotExist:
            raise Http404

    def get(self, request, filename, format=None):
        instance = self.get_object(filename)
        csv_file_path = instance.file.path

        with open(csv_file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = [row for row in reader]

        data = {"header": reader.fieldnames, "rows": rows}

        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            csv_file_path = instance.file.path
            if not os.path.exists(csv_file_path):
                return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)
            with open(csv_file_path, 'r') as csv_file:
                lines = csv_file.readlines()
                header = [h.strip() for h in lines[0].split(",")]
                rows = []
                for line in lines[1:]:
                    row = [r.strip() for r in line.split(",")]
                    rows.append(dict(zip(header, row)))
                data = {"header": header, "rows": rows}
                return Response(data, status=status.HTTP_200_OK)
        except CsvData.DoesNotExist:
            return Response({"error": "CsvData not found."}, status=status.HTTP_404_NOT_FOUND)
