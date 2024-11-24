from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib import auth, messages

from contact.forms import RegisterForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New user successfully registered!')
            return redirect('contact:index')
        messages.error(request, 'Error registering new user')
        
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )


def login_view(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
           user = form.get_user()
           auth.login(request, user)
           messages.success(request, f"Login successfully, welcome {user.first_name}!")
           return redirect('contact:index')
        messages.error(request, "Invalid username or password")

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )


def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')