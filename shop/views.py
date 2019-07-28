from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'shop/index.html')
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

