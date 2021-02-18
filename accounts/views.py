from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm

#from . import forms
#from django.contrib.auth import login,authenticate


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

           # messages.success(request,f'Account created for {username}!')
           # user = authenticate(username=username, password=password)
            #login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request,'accounts/register.html', {'form': form})


