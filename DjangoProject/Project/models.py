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


# # This is just a snippet to remind myself to make text placeholders for the form
# class UserLogin(models.Model):
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#
#     class Meta:
#         verbose_name_plural = "User"
