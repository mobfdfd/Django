from django.shortcuts import render
from rest_framework import generics
from .models import Product, ShoppingCart
from .serializers import ShoppingCartSerializer
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
def cart_view(request, customer_id):
    cart_items = ShoppingCart.objects.filter(customer_id=customer_id)
    return render(request, 'cart.html', {'cart_items': cart_items})

# api
class ShoppingCartList(generics.ListAPIView):
    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return ShoppingCart.objects.filter(customer_id=customer_id)