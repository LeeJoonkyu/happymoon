from django.shortcuts import render
from .models import Product
from django.db.models import Q
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