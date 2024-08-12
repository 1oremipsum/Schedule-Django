from django.shortcuts import redirect, render, get_object_or_404
from contact.models import Contact

from django import forms

class ContactForm(forms.ModelForm):
    ...


def create(request):
    context = {

    }

    return render(request, 'contact/create.html', context)
