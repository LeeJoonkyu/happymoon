from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from store.models import Cart_for_Pad


def cart(request):
    if (request.method == 'POST') and (request.POST.get('post_type') == 'order'):
        if request.user.is_authenticated:
            return redirect(reverse("cart:payment"))
        else:
            # TODO : 익명user 장바구니 사용
            return redirect(reverse("accounts:login"))

    cart_products = Cart_for_Pad.objects.filter(user=request.user)
    ctx = {
       'cart_products': cart_products,
    }
    return render(request, "cart.html", ctx)


def payment(request):
    cart_products = Cart_for_Pad.objects.filter(user=request.user)
    ctx = {
        'cart_products': cart_products,
    }
    return render(request, 'payment.html', ctx)



# @login_required
# def order_new(request, item_id):
#     item = get_object_or_404(Item, pk=item_id)
#     order = Order.objects.create(user=request.user, item=item, name=item.name, amount=item.amount)
#     return redirect('shop:order_pay', item_id, str(order.merchant_uid)) #결제페이지로...