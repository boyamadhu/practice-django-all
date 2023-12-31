from django import forms
from app1.models import *
class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['adress','Profile_pic']
        widgets={'adress':forms.Textarea({'cols':30,'row':10})}