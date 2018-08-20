from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from store.models import Cart_for_Pad
from accounts.models import Information
from .forms import OrderForm
from .models import Order


def cart(request):
    if (request.method == 'POST') and (request.POST.get('post_type') == 'order'):
        if request.user.is_authenticated:
            return redirect(reverse("cart:payment"))
        else:
            # TODO : 익명user 장바구니 사용
            return redirect(reverse("accounts:login"))

    cart_products = Cart_for_Pad.objects.filter(user=request.user)
    ulti_total_price= 0
    for item in cart_products:
        ulti_total_price += item.total_price
    if ulti_total_price<20000:
        shipping_charge = 2500
    else:
        shipping_charge = 0
    amount = (ulti_total_price + shipping_charge)
    ctx = {
        'cart_products': cart_products,
        'ulti_total_price': ulti_total_price,
        'shipping_charge': shipping_charge,
        'amount': amount,
    }
    return render(request, "cart.html", ctx)


def payment(request): #TODO: 여기 이어서 하기
    items = Cart_for_Pad.objects.filter(user=request.user)
    buyer = get_object_or_404(Information, user=request.user)
    name = items[0].product.name+" 외 {}개".format(len(items)-1)
    ulti_total_price= 0
    for item in items:
        ulti_total_price += item.total_price
    if ulti_total_price<20000:
            shipping_charge = 2500
    else:
        shipping_charge = 0
    amount = (ulti_total_price + shipping_charge)
    buyer_name = buyer.name
    buyer_email = buyer.email
    initial = {'name':name, 'amount':amount, 'buyer_name':buyer_name, 'buyer_email':buyer_email}

    if request.method == 'POST':
        form = OrderForm(request.POST, initial=initial)
        if form.is_valid(): #TODO: 여기가 문제===================
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect(reverse('cart:pay_now'))
        else:
            print(form)
            return HttpResponse("실패")
    else:
        form = OrderForm(initial=initial)
    
    cart_products = Cart_for_Pad.objects.filter(user=request.user)
    ctx = {
        'form': form,
        'cart_products': cart_products,
        'ulti_total_price': ulti_total_price,
        'shipping_charge': shipping_charge,
        'amount': amount,

        'iamport_shop_id':'iamport', #FIXME: 각자의 shop_id를 지정하실 수 있습니다
    }
    return render(request, 'payment.html', ctx)



def pay_now(request):
    order = Order.objects.first()
    amount = int(order.amount)
    name = order.name
    ctx = {
        'iamport_shop_id': 'iamport',
        'name': name,
        'amount': amount,

    }
    return render(request, 'pay_now.html', ctx)

# @login_required
# def order_new(request, item_id):
#     item = get_object_or_404(Item, pk=item_id)
#     order = Order.objects.create(user=request.user, item=item, name=item.name, amount=item.amount)
#     return redirect('shop:order_pay', item_id, str(order.merchant_uid)) #결제페이지로...


