from django import forms
from django.forms import formset_factory
from .models import Invoice
class InvoiceForm(forms.Form):
    
        # fields = ['customer', 'message']
    customer = forms.CharField(
        label='Cliente',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Cliente',
            'rows':1
        })
    )
    customer_email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'cliente@compania.com',
            'rows':1
        })
    )
    billing_address = forms.CharField(
        label='Direccion',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'rows':1
        })
    )
    message = forms.CharField(
        label='Observacion',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'observacion',
            'rows':1
        })
    )

class LineItemForm(forms.Form):
    
    service = forms.CharField(
        label='Servicio/Producto',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Servicio - Producto'
        })
    )
    description = forms.CharField(
        label='Descripcion',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'descripcion',
            "rows":1
        })
    )
    quantity = forms.IntegerField(
        label='Cantidad',
        widget=forms.TextInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Cantidad'
        }) #quantity should not be less than one
    )
    rate = forms.DecimalField(
        label='Precio $',
        widget=forms.TextInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Precio'
        })
    )
    # amount = forms.DecimalField(
    #     disabled = True,
    #     label='Amount $',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control input',
    #     })
    # )
    
LineItemFormset = formset_factory(LineItemForm, extra=1)