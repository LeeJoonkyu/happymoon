from django.shortcuts import render, redirect
from .models import Information
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def information_create_view(request):
    if request.method == "POST":
        if request.POST.get('post_type') == 'signup':
            information = Information()
            information.name = request.POST.get('name')
            information.email = request.POST.get('email')
            information.birth_year = request.POST.get('birth_year')
            information.birth_month = request.POST.get('birth_month')
            information.birth_day = request.POST.get('birth_day')
            information.channel = request.POST.get('channel')
            information.referral_code = request.POST.get('referral_code')
            if information.name and information.birth_year and information.birth_month and information.birth_day and information.channel is not None:
                information.save()
                User.objects.create_user(username=information.email, password=request.POST.get('password'))
                return redirect("join_success")

        elif request.POST.get('post_type') == 'login':
            username = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')
            else:
                return render(request, "login/information_create.html")
    else:
        return render(request, "login/information_create.html")


def join_success(request):
    return render(request, "login/join_success.html")


def signin(request):
        if request.method == "POST":
            username = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print()
                return redirect('login')
            else:
                for person in User.objects.all():
                    if person.username == username:
                        return HttpResponse('비밀번호가 다릅니다.')
                return HttpResponse('아이디가 다릅니다.')
        else:
            return render(request, 'login/login.html')


def loginsuccess(request):
    return render(request, "login/loginsuccess.html")

