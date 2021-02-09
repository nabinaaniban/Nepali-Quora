from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = get_user_model()
        fields = ('username','email','password1','password2',)



