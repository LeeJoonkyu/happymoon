from django.shortcuts import render,reverse, redirect
from .models import Product, Cart_for_Pad
from django.db.models import Q
# from django.contrib.auth import User
import random

# Create your views here.
def product_list(request):
  products = Product.objects.all()
  ctx={
    'products':products,
  }
  return render(request,'store/product_list.html', ctx)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':

        user = request.user
        order = request.POST.get('order')
        total_price = int(product.price) * int(order)
        print(total_price)
        cart = Cart_for_Pad.objects.create(
            user = user,
            product = product,
            order = order,
            total_price = total_price,
        )

        return  redirect(reverse('cart:cart'))

        if request.user.is_authenticated:
            user = request.user
            order = request.POST.get('order')
            total_price = int(product.price) * int(order)
            print(total_price)
            cart = Cart_for_Pad.objects.create(
                user = user,
                product = product,
                order = order,
                total_price = total_price,
                )
        else:
            user= None
            order = request.POST.get('order')
            total_price = int(product.price) * int(order)
            print(total_price)
            cart = Cart_for_Pad.objects.create(
                user=user,
                product=product,
                order=order,
                total_price=total_price,
            )

            return redirect(reverse('cart:cart'))


    else:
        random_num=[]
        for i in range(1,len(Product.objects.all())+1):
            random_num.append(i)
        del random_num[pk-1]
        random.shuffle(random_num)

        products = Product.objects.filter(Q(pk=random_num[0])|Q(pk=random_num[1])|Q(pk=random_num[2]))
        ctx={
            'product' : product,
            'products' : products,
        }
        return render(request,'store/product_detail.html', ctx)


def cart_for_pad(request):
    cart = Cart_for_Pad.objects.all()
    ctx = {
        'cart': cart,
    }
    return render(request, 'store/cart_for_pad.html', ctx)