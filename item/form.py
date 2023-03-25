from django import forms
from .models import Item

class NewItemFormm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', )