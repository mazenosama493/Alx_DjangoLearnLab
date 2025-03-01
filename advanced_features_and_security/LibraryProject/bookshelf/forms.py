from django import forms
from .models import Book

class ExampleForm(forms.Form):
    title = forms.CharField(
        max_length=100, 
        required=False, 
        widget=forms.TextInput(attrs={"placeholder": "Search books..."})
    )
