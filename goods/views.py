from django.shortcuts import render
from .models import Goods


# Create your views here.
def goods_list(request):
  goods = Goods.objects.all()
  ctx={
    'goods':goods,
  }
  return render(request,'goods/goods_list.html', ctx)


def goods_detail(request, pk):
  goods = Goods.objects.get(pk=pk)
  ctx={
    'goods':goods,
  }
  return render(request,'goods/goods_detail.html', ctx)