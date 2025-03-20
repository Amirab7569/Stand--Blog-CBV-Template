from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class" : "input100"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"input100"}))
    
    
    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get("username"),password=self.cleaned_data.get("password"))
        if user is not None:
            return self.cleaned_data.get("password")
        else:
            raise ValidationError("username or password was wrong", code="invalid_pass_or_user") 
        
        
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name" ,"last_name", "email",)