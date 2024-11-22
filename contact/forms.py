from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms
from typing import Any

from contact.models import Contact


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta():
        model = Contact
        fields = ('first_name', 'last_name', 
                  'phone', 'email', 'description', 
                  'category', 'picture')
    
    # More than one field required for validation
    def clean(self) -> dict[str, Any]:
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error('last_name', ValidationError('First name and last name cannot be the same', code='invalid'))

        return super().clean()
    

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if len(first_name) < 2:
            self.add_error('first_name', ValidationError('First name must be at least 2 characters long', code='invalid'))

        return first_name
    

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=32,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=32,
    )
    email = forms.EmailField(
        required=True,
    )
    
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 
                  'email', 'username', 
                  'password1', 'password2',
                  )
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('Email already exists', code='invalid'))
        return email
