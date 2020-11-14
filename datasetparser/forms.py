from django import forms

class ParseForm(forms.Form):
    dataset = forms.FileField()
    datetime_format = forms.CharField()