from django import forms
from .models import Lead, User
from django.contrib.auth.forms import UserCreationForm, UsernameField

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead 
        fields = (
            'first_name',
            'last_name',
            'age',
            'phoned',
            'source',
            'agent',
        )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}



# class LeadForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     age = forms.IntegerField(min_value=0)
