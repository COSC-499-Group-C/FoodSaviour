from django.db import models
from django.contrib.auth.models import User


class Organizations(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Organizations"


class OrgGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Organizations, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "OrgGroups"
        unique_together = ["user", "group"]


class WasteType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Waste Type"


class MetricData(models.Model):
    waste_type = models.ForeignKey(WasteType, on_delete=models.CASCADE)
    weight = models.FloatField()
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Metric Form Data"

