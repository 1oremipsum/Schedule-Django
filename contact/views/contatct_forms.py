from typing import Any
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from contact.models import Contact

from django import forms

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email',)
    
    def clean(self) -> dict[str, Any]:
        cleaned_data = self.cleaned_data
        self.add_error('first_name', ValidationError('Error message', code='invalid'))
        return super().clean()


def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

        return render(request, 'contact/create.html', context)
    
    context = {
            'form': ContactForm()
        }
    
    return render(request, 'contact/create.html', context)
