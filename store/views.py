from django.shortcuts import render
from .models import Product


# Create your views here.
def product_list(request):
  products = Product.objects.all()
  ctx={
    'products':products,
  }
  return render(request,'store/product_list.html', ctx)


def product_detail(request, pk):
  product = Product.objects.get(pk=pk)
  ctx={
    'product':product,
  }
  return render(request,'store/product_detail.html', ctx)