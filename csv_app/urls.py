from django.urls import path
from .views import CsvDataList, CsvDataDetail, CsvDataDetailByFilename

urlpatterns = [
    path('csv/', CsvDataList.as_view(), name='csv_list'),
    path('csv/<int:pk>/', CsvDataDetail.as_view(), name='csv_detail'),
    path('csv/filename/<str:filename>/', CsvDataDetailByFilename.as_view(), name='csv_detail_by_filename'),
    path('csv_files/<str:filename>', CsvDataDetailByFilename.as_view()),
]
