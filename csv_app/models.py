from django.db import models

class CsvData(models.Model):
    file = models.FileField(upload_to='csv_files/')
    created_at = models.DateTimeField(auto_now_add=True)
