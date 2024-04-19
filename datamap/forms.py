from django import forms
from datamap.models import DatamapLine


class SubmitAPIForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV file')
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)


class DatamapLineEditForm(forms.ModelForm):
    class Meta:
        model = DatamapLine
        fields = ["key", "sheet", "cellref"]

