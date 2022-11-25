from django import forms
from ..models import MetricData, WasteType


class PredictionForm(forms.ModelForm):

    class Meta:
        model = MetricData
        fields = ['waste_type', 'weight', 'amount']

