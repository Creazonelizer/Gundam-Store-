from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from Dashboard.views import  tambah_barang, Barang_View, Customer,Produk

def coba1(request):
    return HttpResponse('Welcome')

def coba2(request):
    titelnya="Home"
    konteks = {
        'titel' : titelnya,
    }
    return render(request,'index.html',konteks)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',coba2), 
    path('addbrg/',tambah_barang),
    path('Vbrg/',Barang_View),
    path('customer/',Customer),
    path('produk1/',Produk),
]
