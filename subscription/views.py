from django.shortcuts import render
from .models import Type

# Create your views here.


def subscription_list(request):
  types = Type.objects.all()
  ctx={
    'types':types,
  }
  return render(request,'subscription/subscription_list.html', ctx)


def subscription_detail(request, pk):
  type = Type.objects.get(pk=pk)
  ctx={
    'type':type,
  }
  return render(request,'subscription/subscription_detail.html', ctx)