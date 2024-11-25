from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib import auth, messages

from contact.forms import RegisterForm, RegisterUpdateForm

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


def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )
    
    form.save()
    messages.success(request, "Profile updated successfully!")
    return redirect('contact:login')

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

