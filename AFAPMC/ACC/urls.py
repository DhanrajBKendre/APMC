from django.contrib import admin
from django.urls import path
from django.urls import include
from ACC import views

app_name = 'ACC'

urlpatterns = [
    path('',views.index),
    path('login',views.loginUser),
    path('logout',views.logoutUser),
    path('signup',views.signup),
    path('reports',views.reports),
    path('addproprietor',views.addproprietor),
    path('searchproprietor',views.searchproprietor),
    path('updateproprietor/<int:i_id>',views.updateproprietor,name="updprop"),
    path('deleteproprietor/<int:i_id>',views.deleteproprietor,name="delprop"),
    path('createinvoice/<int:i_id>',views.createinvoice,name="crin"),
    path('error',views.error),
    path('updateproprietor',views.upp),
    path('deleteproprietor',views.dpp),
    path('createinvoice',views.ci),
    path('reports/invoicerecords',views.invoicerecords,name="rirecords"),
    path('reports/proprietors',views.proprecords,name='precords'),
    path('reports/finance',views.financerecords,name='refinance'),
    path('reports/tally',views.tally,name="retally"),
]