from django.core.exceptions import ValidationError
from contact.models import Contact
from django import forms
from typing import Any

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category')
    
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