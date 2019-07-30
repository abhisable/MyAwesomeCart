from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import render
import math

# Create your views here.
def index(request):
    products=Product.objects.all()
    print(products)
    n=len(products)
    nSlides=n//4+math.ceil((n/4)-(n//4))
    param={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    return render(request,'shop/index.html',param)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return  HttpResponse("you are on contact page")
def tracker(request):
    return HttpResponse("you are on tracker page")
def search(request):
    return HttpResponse("you are on search page")
def productView(request):
    return HttpResponse("you are on prodView page")
def checkout(request):
    return HttpResponse("you are on checkout page")
def product(request):
    context={'product':Product.objects.all()}
    return render(request,'shop/product.html',context)

