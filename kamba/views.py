from django.shortcuts import render
from django.http import request,HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html",{})

def aboutus(request):
    return render(request,"AboutUs.html",{})

def products(request):
    return render(request,"product.html",{})

def checkout(request):
    return render(request,"checkout.html",{})

def ourteam(request):
    return render(request,"ourteam.html",{})