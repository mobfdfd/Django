from django.shortcuts import render
from .models import Product
# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
