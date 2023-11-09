
from django.shortcuts import redirect, render
from random import randint
from django.conf import settings
from django.core.mail import send_mail

from customer.models import Customer, Seller
from seller.models import Product
# Create your views here.


def customer_home(request):
    customer = Customer.objects.get(id = request.session['customer'])
    products = Product.objects.all()
    context = {
        'products':products,
        'customer_details':customer
    }
    return render(request, 'customer/customer_home.html',context)


def store(request):
    query = request.GET.get('query')
    if query == 'all':
        product = Product.objects.all()
    else:
        product = Product.objects.filter(product_category = query)
    return render(request, 'customer/store.html',{'product':product})


def product_detail(request,id):
    product = Product.objects.get(id = id)
    return render(request, 'customer/product_detail.html',{'product':product})


def cart(request):
    return render(request, 'customer/cart.html')


def place_order(request):
    return render(request, 'customer/place_order.html')


def order_complete(request):
    return render(request, 'customer/order_complete.html')


def dashboard(request):
    return render(request, 'customer/dashboard.html')


def seller_register(request):
    msg = ''
    status = False
    if request.method == 'POST':
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        company_name = request.POST['comp_name']
        bank_name = request.POST['bankname']
        bank_branch = request.POST['branch']
        account_number = request.POST['acct_number']
        ifsc = request.POST['ifsc']
        seller_image = request.FILES['picture']
       
        seller_exist = Seller.objects.filter(email = email).exists()
        if not seller_exist :
            seller = Seller(
                first_name = f_name,
                last_name = l_name,
                email = email,
                gender = gender,
                city = city,
                country = country,
                company_name = company_name,
                bank_name = bank_name,
                bank_branch = bank_branch,
                IFSC = ifsc,
                picture = seller_image,
                account_number = account_number
            )
            
            seller.save()
            msg = 'Account created successfully'
            status = True
        else:
            msg = 'Account already exists'
            
    return render(request, 'customer/seller_register.html',{'message':msg})
    

def seller_login(request):
    msg = ''
    if request.method == 'POST':
        s_username = request.POST['seller_id']
        s_password = request.POST['password']

        sellernew = Seller.objects.filter(loginid = s_username, password = s_password)

        if sellernew.exists():
                request.session['seller'] = sellernew[0].id
                request.session['seller_name'] = sellernew[0].first_name + ' ' + sellernew[0].last_name
                return redirect('Seller:seller_home')
        else: 
                msg = 'Incorrect password/Id'

    return render(request, 'customer/seller_login.html',{'message' : msg})


def customer_signup(request):
    msg = ''
    status = False
    if request.method == 'POST':
        f_name = request.POST['fname']
        l_name = request.POST['lastname']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        password = request.POST['password']

        customer_exist = Customer.objects.filter(email = email).exists()
        
        if not customer_exist:
            customer = Customer(
                first_name = f_name,
                last_name = l_name,
                email = email, 
                gender = gender,
                city = city,
                country = country, 
                password = password)
            customer.save()
            msg = 'Registration successfull'
            status = True
        else:
            msg = 'Already registered'
    return render(request, 'customer/customer_signup.html', {'message': msg,'status': status})


def customer_login(request):
    msg = ''
    if request.method == 'POST':
        c_email = request.POST['email']
        c_password = request.POST['password']

        customer = Customer.objects.filter(email = c_email, password = c_password)

        if customer.exists():
            request.session['customer'] = customer[0].id
            return redirect('customer:customer_home')
        else: 
            msg = 'Incorrect password/Username'
    return render(request, 'customer/customer_login.html',{'message' : msg})


def forgot_password_customer(request):
    return render(request, 'customer/forgot_password_customer.html')


def forgot_password_seller(request):
    return render(request, 'customer/forgot_password_seller.html')