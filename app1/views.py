import razorpay
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from adminapp.models import Category

from vendorapp.models import Product


from pro1.settings import REZORPAY_API_KEY, RAZORPAY_API_SECRETKEY



# Create your views here.
def base(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')


def contact(request):
    return render (request,'contact.html')

def faq(request):
    return render(request,'faq.html')
def index_2(request):
    cat=Category.objects.all()
    p=Product.objects.filter(Tag="trendding").order_by('-Tag')[10:17:2]
    return render(request,'index-2.html',{'cat':cat,'p':p})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = authenticate(username=username, password=password)
        print(user,'uuuuuuuuuuuuuuuuuuuuuu')

        if user is not None:
            login(request,user)
            print('mfjknehsnhfndk')
            return redirect('/')
            # firstname = user.first_name
            # return render(request, 'index_2.html', {'firstname': firstname})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('/login/')
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        # contact=request.post['contact']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print(username, firstname, lastname, email, password,contact)

        if User.objects.filter(username=username):
            messages.error(request, "username already exists,Please try another username!!")
            return redirect('/signup/')

        if User.objects.filter(email=email):
            messages.error(request, 'Email is already registerd!!')
            return redirect('/signup/')

        if len(username) > 10:
            messages.error(request, 'username musbt be under 10 characters')

        if password != confirm_password:
            messages.error(request, 'password did not match')

        # if not username.isalnum():
        #     messages.error(request,'username must be alpha numeric ')
        #     return redirect('/')

        up = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                      password=password, )
        up.save()
        messages.success(request, "You are sucessfully signed up !!")
        return redirect('/login/')
    return render(request, 'signup.html')


def signout(request):
    logout(request)
    messages.error(request, "Logout Successfully!!")
    return redirect('/')

def order_tracking(request):
    return render(request,'order-tracking.html')

def product_details(request,id):
    p = Product.objects.get(id=id)
    related_products = Product.objects.filter(sid=p.sid).exclude(id=id)[:4]
    for i in related_products:
        print(i.image.url)

    return render(request,'product-details.html',{'p':p,'rp':related_products})

def product_details2(request):
    return render(request,'product-details-2.html')

def product_details3(request):
    return render(request,'product-details-3.html')

def search(request):
    if request .method=='GET':
        s=request.GET.get('search')
        p=Product.objects.filter(name__icontains=s)
        return render(request,'shop.html',{"p":p})
    else:
        return HttpResponse("No Data Found!!")

def shop(request,sid=None):
    sid = request.GET.get('sid')
    print(sid)
    cat=Category.objects.all()
    dp=0

    if sid:
        p = Product.objects.filter(sid=sid)

    else:
        p = Product.objects.all()
        # discounts = {discount.product_id: discount.discount_amount for discount in Discount.objects.all()}
        # print(p)
        #
        #
        # for i in p:
        #     print(i,'iiiiiiiiiiiiiiiiiiiiiiiiii')
        #     discount = Discount.objects.filter(product=i)
        #     print(discount,'dddddddddddddddddddddddd')
        #     for d in discount:
        #
        #         dp = int(i.price - (i.price * d.discount_amount / 100))
        #         print(dp,'ddddddddddddddddddddpppppppppppppppppppppppriiiiiiiiiiii')
    return render(request,'shop.html',{'cat':cat,'p':p,'dp':dp})
@login_required(login_url='/login/')
def addtocart(request,id):
    url = request.META.get('HTTP_REFERER')


    print(id,'ppppppppppppppppiiiiiiiiiiiiddddddddd')
    proid = Product.objects.get(id=id)
    print(proid.pieces)
    uid = request.user.id
    cart = Cart.objects.filter(user_id=uid, pro_id=proid)

    if proid.pieces != 0:
        print('Trueeeeeeeeeeeeeeeeeeeeeeeeee')

        if request.method == 'POST':
            pid = request.POST['pro']
            proid = Product.objects.get(id=id)

            qty = int(request.POST['quantity'])
            print(qty,'qtyyyy _________________')
            if proid.pieces < qty:
                print('more than product quntity of prodetail page')
                messages.error(request, proid.name + f"have only {proid.pieces} items.")
            else:

            # Check if the same product already exists in the cart for the user


                if Cart.objects.filter(user_id=uid, pro_id=pid) :
                        price = proid.discounted_price() if proid.discount_percentage else proid.price
                        existing_item = Cart.objects.get(user_id=uid, pro_id=pid)
                        print(existing_item.quantity)

                        if proid.pieces <= existing_item.quantity:
                            print('more than product quntity of prodetail page')
                            messages.error(request, proid.name + f"have only {proid.pieces} items. {proid.pieces} have already in your cart. ")
                        else:
                        # If the same product is found, update the quantity instead of creating a new entry
                            existing_item.quantity = existing_item.quantity +qty
                            existing_item.total = existing_item.quantity * price
                            existing_item.save()
                            messages.success(request, proid.name + " added to the Cart.")

                    # return redirect('/cart/')
                else:
                    price=proid.discounted_price() if proid.discount_percentage else proid.price
                    # If the product doesn't exist in the cart, create a new entry
                    Cart(user_id=uid, pro_id=pid, quantity=qty, total=qty * price).save()
                    messages.success(request, proid.name + " added to the Cart.")

                # return redirect('/cart/')
        elif Cart.objects.filter(user_id=uid, pro_id=proid):
            print('cccc')
            price = proid.discounted_price() if proid.discount_percentage else proid.price
            existing_item = Cart.objects.get(user_id=uid, pro_id=proid)
            if proid.pieces <= existing_item.quantity:
                print('more than product quntity')
                messages.error(request,proid.name + f"have only {proid.pieces} items.")
            else:
                # If the same product is found, update the quantity instead of creating a new entry
                existing_item.quantity = existing_item.quantity + 1
                existing_item.total = existing_item.quantity * price
                existing_item.save()
                messages.success(request, proid.name + " added to the Cart.")

        else:
            price = proid.discounted_price() if proid.discount_percentage else proid.price
            print('fffffffffffffffffffff')
            Cart(user_id=uid, pro_id=proid.id, quantity=1, total=1*price).save()
            messages.success(request, proid.name + " added to the Cart.")
    else:
        messages.error(request,'product is out of stock')

        # return redirect('/cart/')

    return HttpResponseRedirect(url)

@login_required(login_url='/login/')
def change_qty(request, id):
    print('change qtyyyyyy')
    url = request.META.get('HTTP_REFERER')
    c_cart = Cart.objects.get(id=id)
    print(c_cart.quantity,'cccccccccccc')
    quantity = request.POST['quantity']
    print(quantity,'qqqqqqqqqqqq')
    qty=int(quantity)
    print(c_cart.pro.pieces,'ppppppppppppieeeeeeeeceeeeeeeeee')
    # print(type(quantity))
    if c_cart.pro.pieces == 0:
        messages.error(request,'product out of stock ')
    elif c_cart.pro.pieces < qty:
        # print('Trueeeeeeeeeeeeeeeeeeeeeeeeee')
        messages.error(request,  f" Remaining quantity of product is : {c_cart.pro.pieces} so you select {c_cart.pro.pieces} of product ")

    else:

        if quantity == '0':
            print('yes')
            c_cart.delete()
            return redirect("/cart/")

        else:
            price = c_cart.pro.discounted_price() if c_cart.pro.discount_percentage else c_cart.pro.price
            c_cart.quantity = quantity
            c_cart.total= price * int(quantity)
            c_cart.save()
            return redirect("/cart/")

    return HttpResponseRedirect(url)

@login_required(login_url='/login/')
def cart(request):
    cat = Category.objects.all()
    uid = request.user.id
    cart = Cart.objects.filter(user=uid)
    print(cart,'carttttttttttttttttt')
    subtotal = sum(i.total for i in cart)
    print(subtotal)
    if subtotal == 0:
        shipping=0
        total = shipping + subtotal
    else:
        shipping = 50
        total = shipping + subtotal
    c1 = Cart.objects.filter(user=uid).count()
    if c1 == 0:
        print('yessssss')
        messages.info(request, "Your cart is currently empty! Go to shopping page below and buy your favourite products.")
    # for i in c:
    #     print(i.total)

    # p=Product.objects.get(id=id)
    return render(request, 'cart.html', {'cat':cat,'cart': cart, 'total': total, 'subtotal': subtotal, 'shipping': shipping,'c1':c1})


# def checkout(request):
#     cat = Category.objects.all()
#     t=100
#     if request.method=="POST":
#         user = request.user.id
#         # total_price = request.POST['total_price']
#         fname=request.POST['fname']
#         lname=request.POST['lname']
#         email = request.POST['email']
#         address = request.POST['address']
#         country = request.POST['country']
#         # city = request.POST['city']
#         state = request.POST['state']
#         phone = request.POST['phone']
#         # date = request.POST['date']
#         info = request.POST['info']
#         zip=request.POST['zip']
#         paymentmode=request.POST['paymentmode']
#         # orderstatus =request.POST['orderstatus']
#         # status = request.POST['status']
#         # print(user,fname,email,address,country,state,phone,info)
#         cart=Cart.objects.filter(user=user)
#         total=sum(i.total for i in cart)
#         # print(total,'tooooooooooooooooo')
#         # print(cart)
#
#         o=Order(user_id=user,fname=fname,lname=lname,email=email,address=address,country=country,state=state,zip=zip,phone=phone,info=info,total_price=total,paymentmode=paymentmode)
#         o.save()
#         for c in cart:
#             cart_item=OrderItem(
#                 user_id=user,
#                 order_id=o.id ,
#                 prod_id=c.pro,
#                 image=c.pro.image,
#                 quantity=c.quantity,
#                 price=c.pro.price,
#                 total_price=c.total
#             )
#             cart_item.save()
#             cart.delete()
# #
#         messages.success(request, 'Order successfully placed! Thanks for shopping, visit again.')
#         return redirect('/')
#     return render(request, 'checkout.html',{'cat':cat,'total':t} )
@login_required(login_url='/login/')
def add_to_wishlist(request, product_id):
    url = request.META.get('HTTP_REFERER')
    pro=Product.objects.get(id=product_id)
    uid=request.user.id
    print(uid,'uiddddddddddddddd')
    print(pro,'proooooidddddd')
    wishlist=Wishlist.objects.filter(product=pro.id,user=uid)
    print(wishlist)
    #
    if Wishlist.objects.filter(product=pro.id,user=uid):
        print('addddeeeeeeedddddd nnnnnnnnnnottt')
        messages.warning(request, 'Item is already present in the wishlist.')
        return HttpResponseRedirect(url)

    else:
        w=Wishlist.objects.create(user_id=uid,product_id=pro.id)
        w.save()
        messages.success(request, 'Item added to wishlist successfully.')
        return HttpResponseRedirect(url)

    return redirect('/wishlist/')
@login_required(login_url='/login/')
def checkout(request):
    user=request.user.id
    # Initialize Razorpay client with your API key and secret key
    cat = Category.objects.all()
    cart=Cart.objects.filter(user=user)
    shipping=50
    subtotal=sum(i.total for i in cart)
    total= subtotal + shipping
    print(total,'tttttttttttttttttttttttoooooooooooooooolllllllllll')



        # messages.success(request, 'Order successfully placed! Thanks for shopping, visit again.')
        # return redirect('/')

    # response = client.order.create({'amount': total, 'currency': 'INR', 'payment_capture': 1})

    return render(request, 'checkout.html',{'cat':cat,'subtotal':subtotal,'shipping':shipping,'total':total,'cart':cart})
@login_required(login_url='/login/')
def placeorder(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST' :
        print('--------------------------------yes post')
        user = request.user.id
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        address = request.POST['address']
        country = request.POST['country']
        # city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        # date = request.POST['date']
        info = request.POST['info']
        zip = request.POST['zip']
        paymentmode = request.POST['payment_method']
        selected_payment_method = request.POST.get('payment_method')

        if selected_payment_method == 'razorpay':
            print('razorpayyyyy')

        elif selected_payment_method == 'cod':
            print('codddddddd')
            # Handle Cash on Delivery payment

        # orderstatus =request.POST['orderstatus']
        # status = request.POST['status']
        # print(user,fname,email,address,country,state,phone,info)
        cart = Cart.objects.filter(user=user)
        subtotal = sum(i.total for i in cart)
        shipping = 50
        total=subtotal+shipping
        print(total,'tooooooooooooooooo')
        print(cart)

        o = Order(user_id=user, fname=fname, lname=lname, email=email, address=address, country=country, state=state,
                  zip=zip, phone=phone, info=info, total_price=total, paymentmode=paymentmode)
        o.save()
        print(o.id)
        for c in cart:
            print(c,'cartttttttttttttttttttttttttt')

            cart_item = OrderItem(
                user_id=user,
                order_id=o.id,
                prod_id=c.pro,
                image=c.pro.image,
                quantity=c.quantity,
                price=c.pro.price,
                total_price=c.total
            )
            cart_item.save()
            print(cart_item,'oooooooooooooooooooooooooooooiiitemmmmmmmmmmmmm')
            cart.delete()
            prod = Product.objects.filter(id=c.pro.id)
            print(prod, '--------------------------proooooooooooo----------')
            for pro in prod:
                print(pro.pieces, 'pppppppppieeeeeeeeeeeeeeceeeeeeeees')
                try:
                    quantity_ordered = int(c.quantity)
                    print(quantity_ordered, 'qqqqqqqqqqqqqqqqq')
                except ValueError:
                    return HttpResponse("Invalid quantity")

                if quantity_ordered <= 0:
                    return HttpResponse("Invalid quantity")
                #
                if pro.pieces >= quantity_ordered:
                    pro.pieces -= quantity_ordered
                    if pro.pieces == 0:
                        pro.availability = 'out of stock'
                    pro.save()
                    print(pro.pieces, 'pppppppppppppppppppupdateddddddddd')
                    client = razorpay.Client(auth=('rzp_test_ytoQRUzHn3jtXL', 'Sc3eDMyJEuNfGzcf5r5eWiLz'))
                    response = client.order.create({'amount':total*100, 'currency': 'INR', 'payment_capture': 1})
        return redirect('/')

                    # messages.success(request,'Order placed successfully.')
                    # return HttpResponseRedirect(url)
                #     # Additional order processing logic can be added here
                #     return HttpResponse(f"Order placed successfully. Remaining quantity: {pro.pieces}")
            # else:
            #     messages.success(request, 'Not enough stock available for this order')
            #     return HttpResponseRedirect(url)

        # client = razorpay.Client(auth=('rzp_test_ytoQRUzHn3jtXL', 'Sc3eDMyJEuNfGzcf5r5eWiLz'))
        # response = client.order.create({'amount':total*100, 'currency': 'INR', 'payment_capture': 1})
        # print(response, "****************************************")

        # return redirect('/')

    return render(request,'checkout.html')

@login_required(login_url='/login/')
def order(request):
    print('hi')
    o=Order.objects.filter(user=request.user.id).order_by('-id')
    o1=OrderItem.objects.filter(user=request.user.id)
    for i in o :
        print(i.id,'orderid')
        for v in o1:
            print(v.order.id,'oitem')
            print(v.prod_id,)
            if i.id ==v.order.id:
                print('hhhhhhhhhhhhhhhhhyeeeee')
    return render(request,'orderview.html',{'o':o,'o1':o1})

def shop_list(request,cid=None):
    # cat=Category.objects.all()
    cid = request.GET.get('cid')
    print(cid)
    cat = Category.objects.all()


    if cid:
        p = Product.objects.filter(cid=cid)
        print(p)
    if 'min_price' in request.GET:
        filter_price1 = request.GET.get('min_price')
        filter_price2 = request.GET.get('max_price')
        if filter_price1 == '':
            filter_price1 = 0

        p = Product.objects.filter(price__range=(filter_price1, filter_price2))
    else:
        p = Product.objects.filter(cid=cid)
    return render(request,'shop-list.html',{'cat':cat,'p':p})

@login_required(login_url='/login/')
def wishlist(request):
    cat=Category.objects.all()
    w=Wishlist.objects.filter(user=request.user.id)
    return render(request,'wishlist.html',{'w':w,'cat':cat})

def orderdelete(request,id):
    o = Order.objects.filter(user=request.user.id).order_by('-id')
    o1 = OrderItem.objects.filter(user=request.user.id)
    o1.delete()
    print("delete")
    return redirect("/order/")