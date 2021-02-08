from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=200)

    class Meta:
        fields = ('username','email','password1','password2',)
        model = get_user_model()

    #def __init__(self, *args, **kwargs):
        #super.__init__(*args,**kwargs)
      #  self.fields['username'].label = 'Your Name'
       # self.fields['email'].label = 'Your email'


