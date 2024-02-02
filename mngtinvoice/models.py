from django.db import models
from django.contrib.auth.models import AbstractUser


class Invoicemngt(models.Model):
    invoice_number = models.IntegerField(blank=True, null=True)
    invoice_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    name = models.CharField('Customer Name', max_length=120, default='', blank=True, null=True)

    product_one = models.CharField('Product 1', max_length=120, default='', blank=True, null=True)
    quantity_of_product_one = models.IntegerField('Quantity', default=0, blank=True, null=True)
    unit_price_of_product_one = models.IntegerField('Unit Price', default=0, blank=True, null=True)
    total_price_of_product_one = models.IntegerField('Total', default=0, blank=True, null=True)

    product_two = models.CharField('Product 2', max_length=120, default='', blank=True, null=True)
    quantity_of_product_two = models.IntegerField('Quantity', default=0, blank=True, null=True)
    unit_price_of_product_two = models.IntegerField('Unit Price', default=0, blank=True, null=True)
    total_price_of_product_two = models.IntegerField('Total', default=0, blank=True, null=True)

    product_three = models.CharField('Product 3', max_length=120, default='', blank=True, null=True)
    quantity_of_product_three = models.IntegerField('Quantity', default=0, blank=True, null=True)
    unit_price_of_product_three = models.IntegerField('Unit Price', default=0, blank=True, null=True)
    total_price_of_product_three = models.IntegerField('Total', default=0, blank=True, null=True)

    product_four = models.CharField('Product 4', max_length=120, default='', blank=True, null=True)
    quantity_of_product_four = models.IntegerField('Quantity', default=0, blank=True, null=True)
    unit_price_of_product_four = models.IntegerField('Unit Price', default=0, blank=True, null=True)
    total_price_of_product_four = models.IntegerField('Total', default=0, blank=True, null=True)

    product_five = models.CharField('Product 5', max_length=120, default='', blank=True, null=True)
    quantity_of_product_five = models.IntegerField('Quantity', default=0, blank=True, null=True)
    unit_price_of_product_five = models.IntegerField('Unit Price', default=0, blank=True, null=True)
    total_price_of_product_five = models.IntegerField('Total', default=0, blank=True, null=True)

    product_six = models.CharField('Product 6', max_length=120, default='', blank=True, null=True)
    quantity_of_product_six = models.IntegerField('Quantity', default=0, blank=True, null=True)
    unit_price_of_product_six = models.IntegerField('Unit Price', default=0, blank=True, null=True)
    total_price_of_product_six = models.IntegerField('Total', default=0, blank=True, null=True)

    product_seven = models.CharField('Product 7', max_length=120, default='', blank=True, null=True)
    quantity_of_product_seven = models.IntegerField('Quantity', default=0, blank=True, null=True)
    unit_price_of_product_seven = models.IntegerField('Unit Price', default=0, blank=True, null=True)
    total_price_of_product_seven = models.IntegerField('Total', default=0, blank=True, null=True)

    product_eight = models.CharField('Product 8', max_length=120, default='', blank=True, null=True)
    quantity_of_product_eight = models.IntegerField('Quantity', default=0, blank=True, null=True)
    unit_price_of_product_eight = models.IntegerField('Unit Price', default=0, blank=True, null=True)
    total_price_of_product_eight = models.IntegerField('Total', default=0, blank=True, null=True)

    product_nine = models.CharField('Product 9', max_length=120, default='', blank=True, null=True)
    quantity_of_product_nine = models.IntegerField('Quantity', default=0, blank=True, null=True)
    unit_price_of_product_nine = models.IntegerField('Unit Price', default=0, blank=True, null=True)
    total_price_of_product_nine = models.IntegerField('Total', default=0, blank=True, null=True)

    product_ten = models.CharField('Product 10', max_length=120, default='', blank=True, null=True)
    quantity_of_product_ten = models.IntegerField('Quantity', default=0, blank=True, null=True)
    unit_price_of_product_ten = models.IntegerField('Unit Price', default=0, blank=True, null=True)
    total_price_of_product_ten = models.IntegerField('Total', default=0, blank=True, null=True)

    phone_number = models.CharField(max_length=120, default='', blank=True, null=True)
    total = models.IntegerField(default='0', blank=True, null=True)
    balance = models.IntegerField(default='0', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
    comments = models.TextField(max_length=3000, default='', blank=True, null=True)
    paid = models.BooleanField(default=False)
    invoice_type_choice = (
        ('Receipt', 'Receipt'),
        ('Invoice', 'Invoice'),
    )
    invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)


    def __str__(self):
        return self.name


class Information(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField('Customer Name', max_length=120, default='', blank=True, null=True)
    customer_address = models.CharField('Address', max_length=120, default='', blank=True, null=True)
    landmark = models.CharField('Landmark', max_length=120, default='', blank=True, null=True)
    phone = models.CharField(max_length=120, default='', blank=True, null=True)
    email = models.EmailField(blank=True)
    comment_order = models.TextField('Comment', max_length=3000, default='', blank=True, null=True)
    media_file = models.FileField(upload_to='PDF/', blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name
