from django.shortcuts import render

# Create your views here.

def login_detail(request):

    return render(request, 'login/login_detail.html')