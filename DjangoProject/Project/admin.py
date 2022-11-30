from django.contrib import admin
from .models import Organizations, OrgGroups, MetricData, WasteType

admin.site.register(Organizations)
admin.site.register(OrgGroups)
admin.site.register(MetricData)
admin.site.register(WasteType)
