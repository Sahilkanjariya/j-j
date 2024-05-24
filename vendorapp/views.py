import random
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import global_settings, settings

from adminapp.models import Subcategory

from adminapp.models import Category

from vendorapp.models import Product

from adminapp.models import Vendor

from app1.models import OrderItem


# Create your views here.
def editvendorprofile(request):
    return render(request,'editvendorprofile.html')

def indexvendor(request):
    uid = int(request.user.id)
    vid = Vendor.objects.get(user=uid)
    print(vid)
    pid = Product.objects.filter(vid=vid.id)
    print(pid)
    order = []
    for i in pid:
        oid = OrderItem.objects.filter(prod_id=i.id).order_by('-id')[:5]
        order.append(oid)
    print(order, 'oooooooooooooooooooooooooooooooooooooooooorrrrrrrrrrrrrrrrder')
    for j in pid:
        if j.availability == 'out of stock':
            print(j.availability)
    return render(request,'indexvendor.html',{'order':order,'pid':pid})

def forgotpwvendor(request):
    if request.method == 'POST':

        otp1 = random.randint(10000, 99999)
        e = request.POST.get('email')
        print("---------------", e)
        request.session['email'] = e
        print(otp1)
        if User.objects.filter(email=e).exists():
            u = User.objects.get(email=e)

            obj = Vendor.objects.filter(user=u.id).count()
            if obj == 1:
                data = Vendor.objects.filter(user=u.id).update(otp=otp1)
                request.session['email'] = e
                subject = ' Verification code'
                message = str(otp1)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [e, ]
                send_mail(subject, message, email_from, recipient_list, data)
                return redirect('/vendorapp/resetpwvendor/')

            else:
                messages.error(request, 'Invalid emailaddress')
    return render (request,'forgotpwvendor.html')

def headervendor(request):
    return render(request,'headervendor.html')



def resetpwvendor(request):
    if request.method == 'POST':

        otp = request.POST.get('otp')
        password = request.POST['password']
        c_password = request.POST['c_password']
        print(otp, password, c_password)
        u = Vendor.objects.filter(otp=otp)
        print(u)
        if u is not None:
            print('hiiiiiiiiiiiiiiiiiiiiiii')

            if password == c_password:
                print('ggggggggggggg')
                for i in u:
                    print(i.user)

                    if u:
                        u1 = User.objects.get(id=i.user.id)
                        u1.set_password(password)
                        u1.save()
                        print("success")
                        # user = Register.objects.filter(otp=otp)
                        # for l1 in user:
                        #     request.session['otp'] = l1.otp
                        #     request.session['id'] = l1.id
                        #     print(l1.otp)
                        #     request.session['id'] = l1.id
                        return redirect('/vendorapp/')
                    else:
                        messages.error(request, 'OTP does not match')
                        return render(request, 'resetpwvendor.html')
            else:
                messages.error(request, 'password does not match')
                return render(request, 'resetpwvendor.html')
        else:
            messages.error(request, 'OTP does not match')
            return render(request, 'resetpwvendor.html')

    else:
        pass

    return render(request,'resetpwvendor.html')

def signinvendor(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)

        user=authenticate(username=username,password=password)
        print(user)

        if user is not None:
            login(request,user)
            firstname=user.first_name
            return render(request,'headervendor.html',{'firstname':firstname})

        else:
            messages.error(request,"Bad Credentials")
            return redirect('/vendorapp/')
    return render (request,'signinvendor.html')


def signoutvendor(request):
    logout(request)
    messages.error(request,"Logout Successfully!!")
    return redirect("/vendorapp/")

def load_sub(request):
    country_id = request.GET.get('Category_id')
    print(country_id,'country_id')
    s_id = request.GET.get('sub_id')
    print(s_id, 's_id')
    subcat = Subcategory.objects.filter(category=country_id).order_by('name')
    print(subcat)
    return render(request,'loadsubcat.html',{'subcat':subcat})


def vendoraddproduct(request):
    sub=Subcategory.objects.all()
    cat = Category.objects.all()
    uid = int(request.user.id)
    vid = Vendor.objects.get(user=uid)
    print('---------------vid', vid)

    if request.method == 'POST':
        name = request.POST['name']
        cid = request.POST['cid']
        sid = request.POST['sid']
        price = request.POST['price']
        description = request.POST['description']
        availability = request.POST['availability']
        sku = request.POST['sku']
        pieces = request.POST['pieces']
        image = request.FILES.get('image')
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        tag = request.POST['Tag']
        print('---------------------------------------------product', vid, cid, sid, name, price, availability,
              description, sku, pieces, image, image1, image2, tag)
        p = Product(vid_id=vid.id, cid_id=cid, sid_id=sid, name=name, price=price, availability=availability,
                    sku=sku, pieces=pieces, image=image, image1=image1, image2=image2, Tag=tag)
        p.save()
        return redirect('/vendorapp/productlistvendor/')

    return render(request,'vendoraddproduct.html',{'cat':cat,'sub':sub})

def productlistvendor(request):
    uid = int(request.user.id)
    vid = Vendor.objects.get(user=uid)
    p = Product.objects.filter(vid=vid.id)
    return render(request,'productslistvendor.html',{'p':p})

def vendoreditproduct(request,id):
    sub = Subcategory.objects.all()
    cat = Category.objects.all()
    uid = int(request.user.id)
    vid = Vendor.objects.get(user=uid)
    print('---------------vid', vid)
    p = Product.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST['name']
        cid = request.POST['cid']
        sid = request.POST['sid']
        price = request.POST['price']
        description = request.POST['description']
        availability = request.POST['availability']
        sku = request.POST['sku']
        pieces = request.POST['pieces']
        image = request.FILES.get('image')
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        tag = request.POST['Tag']
        print('---------------------------------------------product', vid, cid, sid, name, price, availability,
              description, sku, pieces, image, image1, image2, tag)
        # p = Product(vid_id=vid.id, cid_id=cid, sid_id=sid, name=name, price=price, availability=availability,
        #             sku=sku, pieces=pieces, image=image, image1=image1, image2=image2, Tag=tag)

        p.name=name
        p.cid=cid
        p.sid=sid
        p.price=price
        p.description=description
        p.availability=availability
        p.sku=sku
        p.pieces=pieces
        p.image=image
        p.image1=image1
        p.image2=image2
        p.Tag=tag

        p.save()
        return redirect("vendorapp/productlistvendor/")
    return render(request,'vendoreditproduct.html',{'p':p})

def vendordeleteproduct(request,id):
    p=Product.objects.get(id=id)
    p.delete()
    return redirect('/vendorapp/productlistvendor/')

def vendorprofile(request):
    uid = int(request.user.id)
    vid = Vendor.objects.get(user=uid)
    print(vid)
    pid = Product.objects.filter(vid=vid.id)
    print(pid)
    for i in pid:
        if i.availability == 'out of stock':
            print(i.availability)
    p = Product.objects.filter(vid=vid.id).order_by("-id")[:4]
    return render(request,'vendorprofile.html',{'pid':pid,'p':p})