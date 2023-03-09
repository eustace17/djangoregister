from __future__ import unicode_literals
from django_daraja.mpesa import utils
from django.http import HttpResponse, JsonResponse
from django.views import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product ,Supp



def register(request,) :
    if  request.method == "POST" :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('register')
    else:
        form = UserRegistrationForm()

    return render (request, 'register.html', {'form':form})

@login_required
def home (request) :
    return render (request,'home.html')

@login_required
def add_product (request) :
    #check if form submitted has a method post
    if request.method == 'POST' :
        #start receiving data from the form
        p_name = request.POST.get('jina')
        p_quantity = request.POST.get('kiasi')
        p_price = request.POST. get ('bei')

        #finally save data in our table called products
        product = Product(prod_name = p_name, prod_quantity=p_quantity,prod_price=p_price)

        product.save()

        #Redirect back with a success message
        messages.success(request, 'Product Saved Successfully')
        return redirect('add-product')
    return render(request,'addproducts.html')

@login_required
def view_products(request) :
    #select all the products to be displayed
    products = Product.objects.all()
    return render (request, 'products.html',{'products' : products})

@login_required
def delete_product(request, id) :
    #Fetch the product to be deleted
    product = Product.objects.get(id = id)
    # delete the product
    product.delete()
    #redirect back to products page with a success messages
    messages.success(request, 'Product deleted successfully')
    return redirect ('products')


@login_required
def Supp(request) :
    #check if form submitted has a method post
    if request.method == 'POST' :
        #start receiving data from the form
        s_name = request.POST.get('jina')
        s_item = request.POST.get('bidhaa')
        s_phone = request.POST. get ('nambari')
        s_email = request.POST.get ('emali')


        #finally save data in our table called products
        supp = Supp (supp_name = s_name, supp_item=s_item,supp_phone=s_phone,supp_email = s_email)

        supp.save()

        #Redirect back with a success message
        messages.success(request, 'Supplier Saved Successfully')
        return redirect('supplier')
    return render(request,'supplier.html')

@login_required
def update_product (request, id) :
    #Fetch the product be updated
    product = Product.objects.get(id = id)
    #check if the form submitted has a method POST
    if request.method == "POST" :
        #Receive data from the form
        updated_name = request.POST.get('jina')
        updated_quantity = request.POST.get('kiasi')
        updated_price = request.POST.get('bei')

       #Update the product with the received updated data
        product.prod_name = updated_name
        product.prod_quantity = updated_quantity
        product.prod_price = updated_price

        #Return the data back to the database and redirect back to products page with a success message

        product.save()
        messages.success(request, 'Product updated successfully')
        return redirect ('products')
    return render (request, 'update.html',{'product' : product})

# Instantiate the MpesaClient
cl = MpesaClient()
#Set up callbacks
stk_callback_url = "https://api.darajambili.com/express-payment"
btc_callback_url = "https://api.darajambili.com/b2c/result"

#Generate the transaction auth_token
def auth_success(request) :
    token = cl.access_token
    return JsonResponse (token,safe = False)

@login_required
def payment (request,id) :
    #select the product to be paid
    product = Product.objects.get(id = id)
    if request.method == "POST" :
        phone_number = request.POST.get ('nambari')
        amount = request.POST.get('bei')
        #Convert the amount to be an Integer
        amount = int(amount)
        account_ref = 'Whiskers'
        transaction_desc = 'Paying for a product'
        transaction = cl.stk_push(phone_number,amount,account_ref,transaction_desc,stk_callback_url)
        return JsonResponse (transaction.response_description, safe = False)
    return render (request,'payment.html',{'product': product})



