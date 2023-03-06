from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product

def register(request) :
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
def supplier (request) :
    #check if form submitted has a method post
    if request.method == 'POST' :
        #start receiving data from the form
        s_name = request.POST.get('jina')
        s_item = request.POST.get('bidhaa')
        s_phone = request.POST. get ('namabari')


        #finally save data in our table called products
        supp = supplier (supp_name = s_name, supp_item=s_item,supp_phone=s_phone)

        supplier.save()

        #Redirect back with a success message
        messages.success(request, 'Supplier Saved Successfully')
        return redirect('supplier')
    return render(request,'supplier.html')
