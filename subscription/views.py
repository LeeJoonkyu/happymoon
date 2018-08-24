from django.shortcuts import render, redirect, reverse
from django.urls import reverse
from subscription.models import Type, Cart_for_Subscription

# Create your views here.


def subscription_list(request):
    types = Type.objects.all()
    ctx = {
        'types': types,
    }
    return render(request, 'subscription/subscription_list.html', ctx)


def subscription_detail(request, str):
    type = Type.objects.get(type_str=str)
    if request.method == 'POST' and request.POST.get('delivery_period') != None:
        user = request.user
        type_str = type.type_str
        # first_date = request.POST.get('first_date')
        delivery_period = request.POST.get('delivery_period')
        number = 'X 1'
        component = type.component
        price = type.price
        cart_subscription = Cart_for_Subscription.objects.create(
            user = user,
            type_str = type_str,
            type = type,
            # first_date = first_date,
            delivery_period = delivery_period,
            number = number,
            component = component,
            price = price,
         )
        ctx = {
            'cart_subscription': cart_subscription,
        }

        return render(request, 'cart_subscription.html', ctx)

    # elif request.POST.get('delivery_period') == None:
    #     return

    else:
        ctx = {
            'type': type,
        }

        return render(request, 'subscription/subscription_detail.html', ctx)