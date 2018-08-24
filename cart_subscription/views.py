from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from subscription.models import Cart_for_Subscription
from accounts.models import Information
from cart_subscription.forms import OrderForm_Subscription
from cart_subscription.models import Order_Subscription
from iamport import Iamport

iamport = Iamport(imp_key=settings.DEFAULT_TEST_IMP_KEY,
                  imp_secret=settings.DEFAULT_TEST_IMP_SECRET)


def cart_subscription(request, str):
    cart_subscriptions = Cart_for_Subscription.objects.filter(type_str=str)
    buyer = get_object_or_404(Information, user=request.user)
    name = cart_subscriptions[2] # 상품이름
    amount = cart_subscriptions[6] # 상품개수
    buyer_name = buyer.name
    buyer_email = buyer.email
    initial = {'name': name, 'amount': amount, 'buyer_name': buyer_name, 'buyer_email': buyer_email}

    if (request.method == 'POST'):
        form = OrderForm_Subscription(request.POST, initial=initial)
        if request.user.is_authenticated and form.is_valid():
            order = form.save(commit=False)
            recipient_postcode = request.POST.get('recipient_postcode')
            recipient_add = request.POST.get('recipient_add')+' '+request.POST.get('recipient_adddetail')
            order.recipient_postcode = recipient_postcode
            order.recipient_add = recipient_add
            order.user = request.user
            order.save()

            return redirect(reverse('cart_subscription:payment', args=(str(order.merchant_uid), )))

        elif not (request.user.is_authenticated):
            return redirect(reverse("accounts:login"))

        elif not (form.is_valid):
            print(form)
            return HttpResponse('결제 실패')

    else:
        form = OrderForm_Subscription(initial=initial)

    ctx = {
        'form': form,
        'cart_subscriptions': cart_subscriptions,
    }
    return render(request, "cart_subscription.html", ctx)

def payment(request, merchant_uid):
    order = Order_Subscription.objects.get(user=request.user, merchant_uid=merchant_uid)
    ctx = {
        'iamport_shop_id': 'iamport',
        'order': order,
    }
    return render(request, 'payment.html', ctx)

def pay_success(request):
    imp_uid = request.GET.get("imp_uid")
    response = iamport.find_by_imp_uid(imp_uid)

    merchant_uid = response["merchant_uid"]
    myorder = get_object_or_404(Order_Subscription, merchant_uid=merchant_uid)
    myorder.imp_uid = imp_uid
    myorder.save()

    type_price = myorder.amount
    if not iamport.is_paid(type_price, imp_uid=imp_uid):
        # 결제실패
        return HttpResponse('실패')

    return render(request, 'pay_success.html')