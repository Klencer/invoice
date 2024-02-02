from django.shortcuts import render , redirect , HttpResponse
from django.contrib import messages
from django.shortcuts import render , redirect
from .forms import InvoiceUpdateForm
from .forms import InvoiceSearchForm
from .forms import InvoiceForm
from .forms import Customer , CreateCustomerForm , Invoicemngt , Information
from .forms import CustomerUpdateForm
from .models import *
# For Report Lab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
# login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
# from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request , 'pages/home.html')

def update_invoice(request , pk):
    queryset = Invoicemngt.objects.get(id=pk)
    form = InvoiceUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InvoiceUpdateForm(request.POST , instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/invoice_list')

    context = {
        'form': form
    }
    return render(request , 'pages/invoice.html' , context)


def update_information(request , pk):
    queryset = Information.objects.get(id=pk)
    form = CustomerUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST , instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/information_list')

    context = {
        'form': form
    }
    return render(request , 'pages/information.html', context)


def invoice_delete(request , pk):
    queryset = Invoicemngt.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/invoice_list')
    return render(request, 'pages/invoice_delete.html')


def information_delete(request , pk):
    queryset = Information.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/information_list')
    return render(request, 'pages/information_delete.html')


def invoice(request):
    form = InvoiceForm(request.POST or None)
    total_invoices = Invoicemngt.objects.count()
    queryset = Invoicemngt.objects.order_by('-invoice_date')[:6]

    if form.is_valid():
        form.save()
        messages.success(request , 'Successfully Saved')
        return redirect('/invoice')
    context = {
        "form": form ,
        "title": "New Invoice" ,
        "total_invoices": total_invoices ,
        "queryset": queryset ,

    }
    return render(request , 'pages/invoice.html' , context)


def information(request):
    form = Customer(request.POST or None)
    customer = Information.objects.count()

    if form.is_valid():
        form.save()
        messages.success(request , 'Successfully Saved')
        return redirect('/information')
    context = {
        "form": form ,
        "title": "New Information" ,
    }
    return render(request , 'pages/information.html' , context)


def information_list(request):
    title = 'List of Information'
    queryset = Information.objects.all()
    form = Customer(request.POST or None)

    context = {
        "title": title ,
        "queryset": queryset ,
        "form": form ,
    }
    if request.method == 'POST':
        queryset = Information.objects.filter(customer_id__icontains=form['customer_id'].value() ,
                                              customer_name__icontains=form['customer_name'].value())
        context = {
            "form": form ,
            "title": title ,
            "queryset": queryset ,
        }
    return render(request , 'pages/information_list.html' , context)


def invoice_list(request):
    title = 'List of Invoices'
    queryset = Invoicemngt.objects.all()
    form = InvoiceSearchForm(request.POST or None)

    context = {
        "title": title ,
        "queryset": queryset ,
        "form": form ,
    }
    if request.method == 'POST':
        queryset = Invoicemngt.objects.filter(invoice_number__icontains=form['invoice_number'].value() ,
                                              name__icontains=form['name'].value())
        context = {
            "form": form ,
            "title": title ,
            "queryset": queryset ,
        }

        if form['generate_invoice'].value():
            instance = queryset
            data_file = instance
            num_of_invoices = len(queryset)
            message = str(num_of_invoices) + " invoices successfully generated."
            messages.success(request , message)

            def import_data(data_file):
                invoice_data = data_file
                for row in invoice_data:
                    invoice_type = row.invoice_type
                    invoice_number = row.invoice_number
                    invoice_date = row.invoice_date
                    name = row.name
                    phone_number = row.phone_number

                    product_one = row.product_one
                    quantity_of_product_one = row.quantity_of_product_one
                    unit_price_of_product_one = row.unit_price_of_product_one
                    total_price_of_product_one = row.total_price_of_product_one

                    product_two = row.product_two
                    quantity_of_product_two = row.quantity_of_product_two
                    unit_price_of_product_two = row.unit_price_of_product_two
                    total_price_of_product_two = row.total_price_of_product_two

                    product_three = row.product_three
                    quantity_of_product_three = row.quantity_of_product_three
                    unit_price_of_product_three = row.unit_price_of_product_three
                    total_price_of_product_three = row.total_price_of_product_three

                    product_four = row.product_four
                    quantity_of_product_four = row.quantity_of_product_four
                    unit_price_of_product_four = row.unit_price_of_product_four
                    total_price_of_product_four = row.total_price_of_product_four

                    product_five = row.product_five
                    quantity_of_product_five = row.quantity_of_product_five
                    unit_price_of_product_five = row.unit_price_of_product_five
                    total_price_of_product_five = row.total_price_of_product_five

                    product_six = row.product_six
                    quantity_of_product_six = row.quantity_of_product_six
                    unit_price_of_product_six = row.unit_price_of_product_six
                    total_price_of_product_six = row.total_price_of_product_six

                    product_seven = row.product_seven
                    quantity_of_product_seven = row.quantity_of_product_seven
                    unit_price_of_product_seven = row.unit_price_of_product_seven
                    total_price_of_product_seven = row.total_price_of_product_seven

                    product_eight = row.product_eight
                    quantity_of_product_eight = row.quantity_of_product_eight
                    unit_price_of_product_eight = row.unit_price_of_product_eight
                    total_price_of_product_eight = row.total_price_of_product_eight

                    product_nine = row.product_nine
                    quantity_of_product_nine = row.quantity_of_product_nine
                    unit_price_of_product_nine = row.unit_price_of_product_nine
                    total_price_of_product_nine = row.total_price_of_product_nine

                    product_ten = row.product_ten
                    quantity_of_product_ten = row.quantity_of_product_ten
                    unit_price_of_product_ten = row.unit_price_of_product_ten
                    total_price_of_product_ten = row.total_price_of_product_ten

                    total = row.total
                    pdf_file_name = str(invoice_number) + '_' + str(name) + '.pdf'
                    generate_invoice(str(name) , str(invoice_number) ,
                                     str(product_one) , str(quantity_of_product_one) ,
                                     str(unit_price_of_product_one) ,
                                     str(total_price_of_product_one) ,
                                     str(product_two) , str(quantity_of_product_two) ,
                                     str(unit_price_of_product_two) ,
                                     str(total_price_of_product_two) ,
                                     str(product_three) , str(quantity_of_product_three) ,
                                     str(unit_price_of_product_three) ,
                                     str(total_price_of_product_three) ,
                                     str(product_four) , str(quantity_of_product_four) ,
                                     str(unit_price_of_product_four) , str(total_price_of_product_four) ,
                                     str(product_five) , str(quantity_of_product_five) ,
                                     str(unit_price_of_product_five) ,
                                     str(total_price_of_product_five) ,
                                     str(product_six) , str(quantity_of_product_six) ,
                                     str(unit_price_of_product_six) ,
                                     str(total_price_of_product_six) ,
                                     str(product_seven) , str(quantity_of_product_seven) ,
                                     str(unit_price_of_product_seven) ,
                                     str(total_price_of_product_seven) ,
                                     str(product_eight) , str(quantity_of_product_eight) ,
                                     str(unit_price_of_product_eight) ,
                                     str(total_price_of_product_eight) ,
                                     str(product_nine) , str(quantity_of_product_nine) ,
                                     str(unit_price_of_product_nine) ,
                                     str(total_price_of_product_nine) ,
                                     str(product_ten) , str(quantity_of_product_ten) ,
                                     str(unit_price_of_product_ten) ,
                                     str(total_price_of_product_ten) ,
                                     str(total) , str(phone_number) , str(invoice_date) , str(invoice_type) ,
                                     pdf_file_name)

            def generate_invoice(name , invoice_number , product_one , quantity_of_product_one ,
                                 unit_price_of_product_one ,
                                 total_price_of_product_one , product_two , quantity_of_product_two ,
                                 unit_price_of_product_two ,
                                 total_price_of_product_two , product_three , quantity_of_product_three ,
                                 unit_price_of_product_three ,
                                 total_price_of_product_three , product_four , quantity_of_product_four ,
                                 unit_price_of_product_four ,
                                 total_price_of_product_four , product_five , quantity_of_product_five ,
                                 unit_price_of_product_five ,
                                 total_price_of_product_five , product_six , quantity_of_product_six ,
                                 unit_price_of_product_six ,
                                 total_price_of_product_six , product_seven , quantity_of_product_seven ,
                                 unit_price_of_product_seven ,
                                 total_price_of_product_seven , product_eight , quantity_of_product_eight ,
                                 unit_price_of_product_eight ,
                                 total_price_of_product_eight , product_nine , quantity_of_product_nine ,
                                 unit_price_of_product_nine ,
                                 total_price_of_product_nine , product_ten , quantity_of_product_ten ,
                                 unit_price_of_product_ten ,
                                 total_price_of_product_ten , total , phone_number , invoice_date , invoice_type ,
                                 pdf_file_name):
                c = canvas.Canvas(pdf_file_name)


                c.setFont('Helvetica' , 12 , leading=None)
                c.drawCentredString(400 , 660 , str(invoice_type) + ':')
                invoice_number_string = str('0000' + invoice_number)
                c.drawCentredString(490 , 660 , invoice_number_string)

                c.drawCentredString(409 , 640 , "Date:")
                c.drawCentredString(492 , 641 , invoice_date)

                c.setFont('Helvetica' , 12 , leading=None)
                c.drawCentredString(397 , 620 , "Amount:")
                c.setFont('Helvetica-Bold' , 12 , leading=None)
                c.drawCentredString(484 , 622 , '₱' + total)

                c.setFont('Helvetica' , 12 , leading=None)
                c.drawCentredString(80 , 660 , "To:")
                c.setFont('Helvetica' , 12 , leading=None)
                c.drawCentredString(150 , 660 , name)

                c.setFont('Helvetica' , 12 , leading=None)
                c.drawCentredString(98 , 640 , "Phone #:")
                c.setFont('Helvetica' , 12 , leading=None)
                c.drawCentredString(150 , 640 , phone_number)

                c.setFont('Helvetica-Bold' , 14 , leading=None)
                c.drawCentredString(310 , 580 , str(invoice_type))
                c.drawCentredString(110 , 560 , "Particulars:")

                c.setFont('Helvetica-Bold' , 12 , leading=None)
                c.drawCentredString(110 , 520 , 'ITEMS')
                c.drawCentredString(220 , 520 , 'QUANTITY')
                c.drawCentredString(330 , 520 , 'UNIT PRICE')
                c.drawCentredString(450 , 520 , 'TOTAL')

                if product_one != '':
                    c.setFont('Helvetica' , 12 , leading=None)
                    c.drawCentredString(110 , 490 , product_one)
                    c.drawCentredString(220 , 490 , quantity_of_product_one)
                    c.drawCentredString(330 , 490 , unit_price_of_product_one)
                    c.drawCentredString(450 , 490 , total_price_of_product_one)

                if product_two != '':
                    c.setFont('Helvetica' , 12 , leading=None)
                    c.drawCentredString(110 , 430 , product_two)
                    c.drawCentredString(220 , 430 , quantity_of_product_two)
                    c.drawCentredString(330 , 430 , unit_price_of_product_two)
                    c.drawCentredString(450 , 430 , total_price_of_product_two)

                if product_three != '':
                    c.setFont('Helvetica' , 12 , leading=None)
                    c.drawCentredString(110 , 430 , product_three)
                    c.drawCentredString(220 , 430 , quantity_of_product_three)
                    c.drawCentredString(330 , 430 , unit_price_of_product_three)
                    c.drawCentredString(450 , 430 , total_price_of_product_three)

                if product_four != '':
                    c.setFont('Helvetica' , 12 , leading=None)
                    c.drawCentredString(110 , 400 , product_four)
                    c.drawCentredString(220 , 400 , quantity_of_product_four)
                    c.drawCentredString(330 , 400 , unit_price_of_product_four)
                    c.drawCentredString(450 , 400 , total_price_of_product_four)

                if product_five != '':
                    c.setFont('Helvetica' , 12 , leading=None)
                    c.drawCentredString(110 , 370 , product_five)
                    c.drawCentredString(220 , 370 , quantity_of_product_five)
                    c.drawCentredString(330 , 370 , unit_price_of_product_five)
                    c.drawCentredString(450 , 370 , total_price_of_product_five)

                if product_six != '':
                    c.setFont('Helvetica' , 12 , leading=None)
                    c.drawCentredString(110 , 340 , product_six)
                    c.drawCentredString(220 , 340 , quantity_of_product_six)
                    c.drawCentredString(330 , 340 , unit_price_of_product_six)
                    c.drawCentredString(450 , 340 , total_price_of_product_six)

                if product_seven != '':
                    c.setFont('Helvetica' , 12 , leading=None)
                    c.drawCentredString(110 , 310 , product_seven)
                    c.drawCentredString(220 , 310 , quantity_of_product_seven)
                    c.drawCentredString(330 , 310 , unit_price_of_product_seven)
                    c.drawCentredString(450 , 310 , total_price_of_product_seven)

                if product_eight != '':
                    c.setFont('Helvetica' , 12 , leading=None)
                    c.drawCentredString(110 , 280 , product_eight)
                    c.drawCentredString(220 , 280 , quantity_of_product_eight)
                    c.drawCentredString(330 , 280 , unit_price_of_product_eight)
                    c.drawCentredString(450 , 280 , total_price_of_product_eight)

                if product_nine != '':
                    c.setFont('Helvetica' , 12 , leading=None)
                    c.drawCentredString(110 , 250 , product_nine)
                    c.drawCentredString(220 , 250 , quantity_of_product_nine)
                    c.drawCentredString(330 , 250 , unit_price_of_product_nine)
                    c.drawCentredString(450 , 250 , total_price_of_product_nine)

                if product_ten != '':
                    c.setFont('Helvetica' , 12 , leading=None)
                    c.drawCentredString(110 , 220 , product_ten)
                    c.drawCentredString(220 , 220 , quantity_of_product_ten)
                    c.drawCentredString(330 , 220 , unit_price_of_product_ten)
                    c.drawCentredString(450 , 220 , total_price_of_product_ten)

                # TOTAL
                c.setFont('Helvetica-Bold' , 20 , leading=None)
                c.drawCentredString(400 , 140 , "TOTAL:")
                c.setFont('Helvetica-Bold' , 20 , leading=None)
                c.drawCentredString(484 , 140 , '₱' + total)

                # SIGN
                c.setFont('Helvetica-Bold' , 12 , leading=None)
                c.drawCentredString(150 , 140 , "Signed:__________________")
                c.setFont('Helvetica-Bold' , 12 , leading=None)
                c.drawCentredString(170 , 120 , 'Manager')

                c.showPage()
                c.save()

            import_data(data_file)

    return render(request , 'pages/invoice_list.html' , context)
