from django.contrib import admin
from django.urls import path,include
from. import views

urlpatterns = [
     path('editvendorprofile/',views.editvendorprofile),
     path('indexvendor/',views.indexvendor),
     path('forgotpwvendor/',views.forgotpwvendor),
     path('headervendor/',views.headervendor),
     path('resetpwvendor/',views.resetpwvendor),
     path('',views.signinvendor),
     path('logout/',views.signoutvendor),
     # path('signupvendor/',views.signupvendor),
     # path('subcatload/',views.subcat_load),
     path('vendoraddproduct/',views.vendoraddproduct),
     path('productlistvendor/', views.productlistvendor),
     path('vendordeleteproduct/<int:id>/', views.vendordeleteproduct),
     path('vendoreditproduct/<int:id>/',views.vendoreditproduct),
     path('vendorprofile/',views.vendorprofile),
     path('ajax/load-sub/', views.load_sub, name='ajax_load_cities'),
]