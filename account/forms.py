from django import forms


class UserLogin(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'login', 'name': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'id': 'password', 'name': 'password'}))


class RegisterForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username', 'name': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'id': 'password', 'name': 'password'}))