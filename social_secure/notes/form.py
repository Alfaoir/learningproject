from django import forms


class UserRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=20, required=True)
    
    
    
    



class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)