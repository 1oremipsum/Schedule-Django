from django.shortcuts import redirect, render
from django.contrib import messages
from contact.forms import RegisterForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New user successfully registered!')
            return redirect('contact:index')
        else:
            messages.error(request, 'Error registering new user')
        
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )