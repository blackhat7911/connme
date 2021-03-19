from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm
from django.contrib import messages

def registration_view(request):
    form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.add_message(request, messages.ERROR, "Couldnot register")
    context = {'form': form}
    return render(request, 'accounts/registration_form.html', context)

def login_view(request):
    form = LoginForm
    context = {'form': form}
    return render(request, 'accounts/login_form.html', context)