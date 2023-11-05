from django import forms
from .models import Participant
from .models import User 


        
        


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User  # Specify the User model
        fields = ['username', 'password']

    password = forms.CharField(widget=forms.PasswordInput)

