from django import forms


class SubmitAPIForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV file')

