from django import forms
from .models import Invoicemngt
from .models import Information
#login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Customer(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['customer_id', 'customer_name', 'customer_address', 'landmark', 'phone', 'email', 'media_file']


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['customer_id', 'customer_name', 'customer_address', 'landmark', 'phone', 'email', 'media_file']


class CreateCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoicemngt
        fields = ['invoice_number', 'name', 'phone_number', 'invoice_date',
                  'product_one', 'quantity_of_product_one', 'unit_price_of_product_one',
                  'total_price_of_product_one', 'product_two', 'quantity_of_product_two',
                  'unit_price_of_product_two', 'total_price_of_product_two',
                  'product_three', 'quantity_of_product_three', 'unit_price_of_product_three',
                  'total_price_of_product_three', 'product_four', 'quantity_of_product_four',
                  'unit_price_of_product_four', 'total_price_of_product_four',
                  'product_five', 'quantity_of_product_five', 'quantity_of_product_five',
                  'unit_price_of_product_five', 'total_price_of_product_five',
                  'product_six', 'quantity_of_product_six', 'unit_price_of_product_six',
                  'total_price_of_product_six', 'product_seven', 'quantity_of_product_seven',
                  'unit_price_of_product_seven', 'total_price_of_product_seven', 'product_eight',
                  'quantity_of_product_eight', 'unit_price_of_product_eight',
                  'total_price_of_product_eight', 'product_nine', 'quantity_of_product_nine',
                  'unit_price_of_product_nine', 'total_price_of_product_nine', 'product_ten',
                  'quantity_of_product_ten', 'unit_price_of_product_ten',
                  'total_price_of_product_ten', 'total', 'paid', 'invoice_type',
                  ]


def clean_invoice_number(self):
    invoice_number = self.cleaned_data.get('invoice_number')
    if not invoice_number:
        raise forms.ValidationError(required)
    return invoice_number


def clean_name(self):
    name = self.cleaned_data.get('name')
    if not name:
        raise forms.ValidationError(required)
    return name


def clean_quantity_of_product_one(self):
    quantity_of_product_one = self.cleaned_data.get('quantity_of_product_one')
    if not quantity_of_product_one:
        raise forms.ValidationError(required)
    return quantity_of_product_one


class InvoiceSearchForm(forms.ModelForm):
    generate_invoice = forms.BooleanField(required=False)

    class Meta:
        model = Invoicemngt
        fields = ['invoice_number', 'name', 'generate_invoice']


class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoicemngt
        fields = ['invoice_number', 'name', 'phone_number', 'invoice_date',
                  'product_one', 'quantity_of_product_one', 'unit_price_of_product_one',
                  'total_price_of_product_one', 'product_two', 'quantity_of_product_two',
                  'unit_price_of_product_two', 'total_price_of_product_two',
                  'product_three', 'quantity_of_product_three', 'unit_price_of_product_three',
                  'total_price_of_product_three', 'product_four', 'quantity_of_product_four',
                  'unit_price_of_product_four', 'total_price_of_product_four',
                  'product_five', 'quantity_of_product_five', 'quantity_of_product_five',
                  'unit_price_of_product_five', 'total_price_of_product_five',
                  'product_six', 'quantity_of_product_six', 'unit_price_of_product_six',
                  'total_price_of_product_six', 'product_seven', 'quantity_of_product_seven',
                  'unit_price_of_product_seven', 'total_price_of_product_seven', 'product_eight',
                  'quantity_of_product_eight', 'unit_price_of_product_eight',
                  'total_price_of_product_eight', 'product_nine', 'quantity_of_product_nine',
                  'unit_price_of_product_nine', 'total_price_of_product_nine', 'product_ten',
                  'quantity_of_product_ten', 'unit_price_of_product_ten',
                  'total_price_of_product_ten', 'total', 'paid', 'invoice_type',
                  ]

    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError(required)
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError(required)
        return name

    def clean_quantity_of_product_one(self):
        quantity_of_product_one = self.cleaned_data.get('quantity_of_product_one')
        if not quantity_of_product_one:
            raise forms.ValidationError(required)
        return quantity_of_product_one
