from django.db import models


class Sensor(models.Model):
    name = models.TextField()
    description = models.CharField(max_length=50)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements',)
    temperature = models.FloatField()
    date = models.DateField(auto_now_add=True)


