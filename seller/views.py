from django.http import JsonResponse
from django.shortcuts import redirect, render


from eKart_admin.models import Category
from seller.models import Product,Seller

# Create your views here.
def seller_home(request):
    sellernew = Seller.objects.get(id = request.session['seller'])
    return render(request, 'seller/seller_home.html',{'seller_details':sellernew})

def add_product(request):
    category_list = Category.objects.all()
    msg = ''

    if request.method == 'POST':
        product_no = request.POST['product_no']
        product_name = request.POST['product_name']
        description = request.POST['description']
        category = request.POST['product_category']
        stock = request.POST['stock']
        price = request.POST['price']
        image = request.FILES['image']
        seller_p = request.session['seller']

        # product_exist = Product.objects.filter(product_no = )
        product,created = Product.objects.get_or_create(product_no = product_no,seller = seller_p,defaults= { 
            'product_no': product_no,
            'product_name': product_name,
            'description':description,
            'stock':stock,
            'price':price,
            'image':image,
            'product_category':Category.objects.get(id = category),
            'seller':Seller.objects.get(id = seller_p),
        })
        if created:
            msg = 'product added'
        else:
            msg = 'product already exist'
    context = {'category':category_list,
                   'message':msg}
    return render(request, 'seller/add_product.html',context)

def add_category(request):
    return render(request, 'seller/add_category.html')

def view_category(request):
    return render(request, 'seller/view_category.html')

def view_products(request):
    products = Product.objects.filter(seller_id = request.session['seller'])
    return render(request, 'seller/view_product.html',{'products':products})

def profile(request):
    return render(request,'seller/profile.html')

def view_orders(request):
    return render(request,'seller/view_orders.html')

def update_stock(request):
    msg = ''
    if request.method == 'POST':
        product_no = request.POST['product_no']
        new_stock = request.POST['new_stock']
        stock = request.POST['stock']

        product =Product.objects.get(product_no = product_no,seller_id = request.session ['seller'])
        product.stock = product.stock + int( new_stock)

        product.save()

        msg = 'Stock Updated'

    return render(request,'seller/update_stock.html',{'message':msg})

def get_current_stock(request):
    product_no = request.POST['product_no']
    product = Product.objects.get(product_no = product_no)

    return JsonResponse({
        'product_name':product.product_name,
        'product_stock':product.stock
    })

def order_history(request):
    return render(request,'seller/order_history.html')

def change_password(request):
    pwd_status = ''
    if request.method == "POST":
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        try:
            if len(new_password) > 8 :
                if new_password == confirm_password:
                    seller = Seller.objects.get(id = request.session['seller'])
                    if seller.password == old_password:
                        seller.password = new_password
                        seller.save()
                        pwd_status = 'password changed'
                    else:
                        pwd_status = 'incorrect password'
                else:
                    pwd_status = 'password does not match'
            else:
                pwd_status = ' password should have minimum 8 characters '
        except:
            pwd_status = 'invalid password'
        
    return render(request,'seller/change_password.html',{'pwd_status': pwd_status})

def seller_logout(request):
    del request.session['seller']
    request.session.flush()
    return redirect('customer:seller_login')