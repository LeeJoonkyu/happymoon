from django.shortcuts import render, redirect
from .models import Information
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import (authenticate, get_user_model, login, logout, )


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
            if information.name and information.birth_year and information.birth_month and information.birth_day and\
                    information.channel is not None:
                user = User.objects.create_user(username=information.email, password=request.POST.get('password'))
                information.user = user
                information.save()
                return redirect('accounts:join_success')
    else:
        return render(request, "accounts/information_create.html")


def join_success(request):
    return render(request, "accounts/join_success.html")


def signin(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('store_pad:pad_list')
            else:
                num = 0
                for person in User.objects.all():
                    if person.username == username:
                        num = num + 1
                if num != 1:
                    login_form.add_error(None, '해당 이메일로 가입된 정보가 없습니다.')
                else:
                    login_form.add_error(None, '비밀번호가 일치하지 않습니다.')
    else:
        login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'accounts/login.html', context)