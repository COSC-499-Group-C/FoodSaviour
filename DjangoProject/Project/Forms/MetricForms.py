from django import forms


class PredictionForm(forms.Form):
    waste_type = forms.CharField()
    weight = forms.FloatField()
    amount = forms.IntegerField()

