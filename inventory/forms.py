from django import forms
from .models import Item

class ItemRegistration(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['product_name', 'product_num', 'product_type', 'product_description', 'product_category',
                  'status', 'unit_measure', 'packing_type']
        widgets = {

            'product_name': forms.TextInput(attrs={'class':'form-control'}),
            'product_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_type': forms.TextInput(attrs={'class': 'form-control'}),
            'product_description': forms.TextInput(attrs={'class': 'form-control'}),
            'product_category': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_measure': forms.TextInput(attrs={'class': 'form-control'}),
            'packing_type': forms.TextInput(attrs={'class':'form-control'}),


        }
