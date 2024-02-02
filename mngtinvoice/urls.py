from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.aboutpage, name="aboutpage"),
    path('invoice', views.invoice, name="invoice"),
    path('information', views.information, name="information"),
    path('information_list', views.information_list, name="information_list"),
    path('invoice_list', views.invoice_list, name="invoice_list"),
    path('invoice', views.invoice, name="invoice"),
    path('invoice', views.invoice, name="invoice"),
    path('update_invoice/<str:pk>/' , views.update_invoice, name="update_invoice"),
    path('invoice_delete/<str:pk>/' , views.invoice_delete, name="invoice_delete"),
    path('update_information/<str:pk>/' , views.update_information, name="update_information"),
    path('information_delete/<str:pk>/' , views.information_delete, name="information_delete"),
]
