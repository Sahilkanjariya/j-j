from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.signinemp),
    path("empindex/",views.empindex),
    path("empprofile/",views.empprofile),
    path("logout/",views.empsignout),
    path("orderlist/",views.employee_orders),
]