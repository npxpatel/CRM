from django import forms
from leads.models import Agent
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm, if used have to specift pass1, pass2

'''By using get_user_model(), your code will always reference the currently active user model, 
              whether it’s the default User from Django or a custom user model specified in your project’s settings'''

User = get_user_model()

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name', 
        )