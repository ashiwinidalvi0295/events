from django import forms
from first_app.models import events

class Addeventsform(forms.ModelForm):
    class Meta:
        model=events
        fields="__all__"
