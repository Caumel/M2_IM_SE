from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class report(forms.Form):
    report = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "report",
                "class": "form-control"
            }
        ))