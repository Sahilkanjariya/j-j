from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
      path('adminheader/',views.adminheader),
      path('adminaddcat/',views.adminaddcat),
      path('adminaddsubcat/',views.adminaddsubcat),
      path('admincatlist/',views.admincatlist),
      path('admineditcat/',views.admineditcat),
      path('adminforgot/',views.adminforgot),
      path('adminhome/',views.adminhome),
      path('adminreset/',views.adminreset),
      path('',views.adminsignin),
      path('logout/',views.signout),
      path('adminsubcatlist/',views.adminsubcatlist),
      path('crispy/',views.crispy),
      path('menu/',views.menu),
      path('subcat/',views.subcat_load),
      path('adminprofile/',views.adminprofile),
      path('addemp/',views.addemp),
      path('viewemp/',views.viewemp),
      path('deleteemp/<int:id>/', views.deleteemp),
      path('addvendor/',views.addvendor),
      path('viewvendor/',views.viewvendor),
      path('deletevendor/<int:id>/', views.deletevendor),
      path('adminupdatecat/<int:id>/',views.adminupdatecat),
      path('admindeletecat/<int:id>/',views.admindeletecat),
      path('adminupdatesubcat/<int:id>/',views.adminupdatesubcat),
      path('admindeletesubcat/<int:id>/',views.admindeletesubcat),
      path('orderlist/',views.orderlist),path('productlist/',views.productlist),
      path('deleteproduct/<int:id>/',views.deleteproduct),

]