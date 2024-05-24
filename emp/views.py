from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect,HttpResponse
from adminapp.models import emp

from app1.models import Order


# Create your views here.
def signinemp(request, emp=None):
    if request.method =='POST':
        uname = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, 'empindex.html', {'firstname': firstname})

        else:
            messages.warning(request, "E-mail or Password Incorrect!!!")
            return render(request, 'signinemp.html', )


    return  render(request,"signinemp.html")

def empindex(request):
    return render(request,'empindex.html')

def empprofile(request):
    return render(request,'empprofile.html')

def empsignout(request):
    logout(request)
    messages.error(request,'Logout Successfully')
    return redirect("/emp/")

def employee_orders(request):
    if request.user.is_authenticated :
        orders=Order.objects.all()
        return render(request,'employee_orders.html',{'orders':orders})
    else:
        return HttpResponse('Unauthorized access')