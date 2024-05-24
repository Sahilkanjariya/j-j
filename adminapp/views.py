from django.conf import settings
import random
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from vendorapp.models import Product

from app1.models import Order


# Create your views here.
def adminprofile(request):
    return render(request,'adminprofile.html')

def adminheader(request):
    return render(request,'adminheader.html')

def adminaddcat(request):
    subcat=Subcategory.objects.all()
    if request.method == 'POST':
        name=request.POST['name']
        avatar=request.FILES.get('avatar')
        print(avatar,'asdfghjkvasdfghjkk')
        cat=Category.objects.create(name=name,image=avatar)
        cat.save()
        return redirect('/adminapp/admincatlist/')

    return render(request,'adminaddcat.html',{'subcat':subcat})

def adminaddsubcat(request):
    cat=Category.objects.all()
    if request.method == 'POST':
        name=request.POST['name']
        image=request.FILES.get('image')
        category_name=request.POST['category']
        scat=Subcategory.objects.create(name=name,image=image,category_id=category_name)
        scat.save()
        return redirect('/adminapp/adminsubcatlist/')

    return render(request,'adminaddsubcat.html',{'cat':cat})

def admincatlist(request):
    cl=Category.objects.all()
    return render(request,'admincatlist.html',{'cl':cl})
def admineditcat(request):
    return render(request,'admineditcat.html')
def adminforgot(request):
    if request.method == 'POST':

        otp1 = random.randint(10000, 99999)
        e = request.POST.get('email')
        print("---------------", e)
        request.session['email'] = e
        print(otp1)
        if User.objects.filter(email=e).exists():
            u = User.objects.get(email=e)

            obj = User.objects.filter(user=u.id).count()
            if obj == 1:
                data = Vendor.objects.filter(user=u.id).update(otp=otp1)
                request.session['email'] = e
                subject = ' Verification code'
                message = str(otp1)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [e, ]
                send_mail(subject, message, email_from, recipient_list, data)
                return redirect('/adminapp/adminreset/')

            else:
                messages.error(request, 'Invalid emailaddress')
    return render(request,'adminforgot.html')
def adminhome(request):
    st=Product.objects.all()
    for i in st:
        if i.availability == 'out of stock':
            print(i.availability)
    return render(request,'adminhome.html',{'st':st})
def adminreset(request):
    if request.method == 'POST':

        otp = request.POST.get('otp')
        password = request.POST['password']
        c_password = request.POST['c_password']
        print(otp, password, c_password)
        u =User.objects.filter(otp=otp)
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
                        return redirect('/adminapp/')
                    else:
                        messages.error(request, 'OTP does not match')
                        return render(request, 'adminreset.html')
            else:
                messages.error(request, 'password does not match')
                return render(request, 'adminreset.html')
        else:
            messages.error(request, 'OTP does not match')
    return render(request,'adminreset.html')
def adminsignin(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password ,is_superuser=True)
        print(user)
        if user is not None:
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/adminapp/adminheader/')
        else:
            if not User.objects.filter(username=username).exists():
                messages.error(request, "Username does not exist")
                return render(request, 'adminsignin.html')
            else:
                messages.error(request, "Password did not match")
            return render(request, 'adminsignin.html')
    return render(request,'adminsignin.html')
def adminsubcatlist(request):
    scl=Subcategory.objects.all()
    return render(request,'adminsubcatlist.html',{'scl':scl})
def crispy(request):
    return render(request,'crispy.html')

def menu(request):
    return render(request,'menu.html')

def subcat_load(request):
    return render(request,'subcat_load.html')

def addemp(request):
    if request.method == 'POST':
        uname=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        # profile=request.FILES['profile']
        if User.objects.filter(username=uname):
            messages.error(request,'Username already exists, Please try another one!!')
            return redirect('/adminapp/addemp/')

        u=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,
                                   password=password)
        u.save()
        e=emp(
             user=u
        )
        e.save()
           # return HttpResponse('data submited')
        return redirect('/adminapp/viewemp/')
    return render(request, 'addemp.html')

def viewemp(request):
    e=emp.objects.all()
    return render(request,'viewemp.html',{'e':e})

def signout(request):
    logout(request)
    messages.success(request,'Logout Succesfully')
    return redirect('/adminapp/')

def deleteemp(request,id):
    v=emp.objects.get(id=id)
    v.delete()
    return redirect('/adminapp/viewemp/')


def adminupdatecat(request,id):
    cat=Category.objects.get(id=id)
    print(cat)

    if request.method == 'POST':
        name = request.POST['name']
        avatar = request.POST['avatar']

        cat.name=name
        cat.avatar=avatar

        cat.save()
        return redirect('/adminapp/admincatlist/')
    return render(request,"adminupdatecat.html",{'cat':cat})

def admindeletecat(request,id):
    cat=Category.objects.get(id=id)
    cat.delete()
    return redirect('/adminapp/admincatlist/')

def adminupdatesubcat(request,id):
    scat=Subcategory.objects.get(id=id)
    print(scat)

    if request.method == 'POST':
        name = request.POST['name']
        avatar = request.POST['avatar']
        category_name=request.POST['category']

        scat.name=name
        scat.avatar=avatar
        scat.category=category_name

        scat.save()
        return redirect('/adminapp/adminsubcatlist/')
    return render(request,"adminupdatesubcat.html",{'scat':scat})

def admindeletesubcat(request,id):
    scat=Subcategory.objects.get(id=id)
    scat.delete()
    return redirect('/adminapp/adminsubcatlist')

def addvendor(request):
    if request.method == 'POST':
        uname = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        # profile=request.FILES['profile']
        if User.objects.filter(username=uname):
            messages.error(request, 'Username already exists, Please try another one!!')
            return redirect('/adminapp/addvendor/')

        u = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email,
                                     password=password)
        u.save()
        v = Vendor(
            user=u,
            is_vendor=True
        )
        v.save()
        # return HttpResponse('data submited')
        return redirect('/adminapp/viewvendor/')
    return render(request,'addvendor.html')


def viewvendor(request):
    v=Vendor.objects.all()
    return render(request,'viewvendor.html',{'v':v})

def deletevendor(request):
    v=Vendor.objects.get(id=id)
    v.delete()
    return redirect('/adminapp/viewvendor/')

def orderlist(request):
    o=Order.objects.all()
    return render(request,'orderlist.html',{'o':o})

def productlist(request):
    p=Product.objects.all()
    return render(request,'productlist.html',{'p':p})

def deleteproduct(request,id):
    pd=Product.objects.get(id=id)
    pd.delete()
    return redirect('/adminapp/productlist/')