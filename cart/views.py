from django.shortcuts import render
from store.models import Cart_for_Pad

def cart(request):
    cart_products = Cart_for_Pad.objects.filter(user=request.user)
    ctx = {
       'cart_products': cart_products,
    }
    return render(request, "cart.html", ctx)