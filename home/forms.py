# forms.py
from django import forms

class StudentDeleteConfirmationForm(forms.Form):
    confirm = forms.BooleanField(
        required=True,
        widget=forms.HiddenInput(),
        initial=True,  # This ensures the user must confirm by default
    )
