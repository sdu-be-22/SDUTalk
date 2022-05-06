from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.apps import apps
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        data = self.cleaned_data['email']
        if "@stu.sdu.edu.kz" not in data:
            raise forms.ValidationError("Must be a sdu address")
        return data

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))