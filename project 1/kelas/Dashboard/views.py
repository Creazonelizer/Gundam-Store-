from django.shortcuts import render
from Dashboard.post_forms import FormBarangku
from Dashboard.models import Barang,customer,produk
# Create your views here.


def Barang_View(request):
    barangs=Barang.objects.all()
    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def Barang_Transaksi(request):
    trans=Transaksi.objects.all()
    konteks={
        'trans':trans,
    }
    return render(request,'tampil_trans.html',konteks)

def tambah_barang(request):
    form=FormBarangku()
    konteks={
        'form':form,
    }
    return render(request,'tambah_barang.html',konteks)


def Customer(request):
    Customers=customer.objects.all()
    konteks={
        'Customers':Customers,
    }
    return render(request,'customer.html',konteks)


def Produk(request):
    Produks=produk.objects.all()
    konteks={
        'Produks':Produks,
    }
    return render(request,'produk1.html',konteks)