from django.urls import path
from measurement.views import SensorList, SensorDetailList, MeasurementList

urlpatterns = [
    path('sensors/', SensorList.as_view()),
    path('sensors/<pk>/', SensorDetailList.as_view()),
    path('measurements/', MeasurementList.as_view()),
]
