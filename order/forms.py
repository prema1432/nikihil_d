from django import forms
from django.contrib.auth.forms import AuthenticationForm

from order.models import my_places


class my_placesform(forms.ModelForm):
    class Meta:
        model = my_places
        fields = '__all__'
        # fields =["location_name","age"]



class MyLoginForm(AuthenticationForm):
    username = forms.CharField(label="username", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(label="password", max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
