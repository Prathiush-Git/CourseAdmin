from django import forms
from modelapp.models import customer

class customerform(forms.ModelForm):
    class meta:
        model=customer
        fields="__all__"