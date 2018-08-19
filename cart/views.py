from django.shortcuts import render, redirect
from django.urls import reverse
from store.models import Cart_for_Pad

def cart(request):
    if request.method == 'POST':
        if (request.POST.get('post_type') == 'order') and (request.user.is_authenticated()):
            return redirect(reverse("cart:payment"))
        elif (request.POST.get('post_type') == 'order'):
            return redirect(reverse("accounts:login"))

    cart_products = Cart_for_Pad.objects.filter(user=request.user)
    ctx = {
       'cart_products': cart_products,
    }
    return render(request, "cart.html", ctx)


def payment(request):
    pass