from django import forms
from .models import Presidents

class NameForm(forms.ModelForm):
    number = forms.IntegerField()

    class Meta:
        model = Presidents
        fields = ['number']
    