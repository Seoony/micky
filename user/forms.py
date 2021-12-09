from django import forms
from django.forms import fields
from .models import UserMicky

class UserMickyForm(forms.ModelForm):
    class Meta:
        model = UserMicky
        fields = [
            'email',
            'password',
            ]