from django.contrib import admin
from .models import Invoicemngt, Information
from .forms import InvoiceForm
from .forms import Customer


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'name', 'phone_number', 'invoice_date']
    form = InvoiceForm
    list_filter = ['name']
    search_fields = ['name', 'invoice_number']


class InfoCustomer(admin.ModelAdmin):
    list_display = ['customer_id', 'customer_name', 'phone', 'email']
    form = Customer
    list_filter = ['customer_name']
    search_fields = ['customer_id', 'customer_name']


admin.site.register(Invoicemngt, InvoiceAdmin)
admin.site.register(Information, InfoCustomer)
