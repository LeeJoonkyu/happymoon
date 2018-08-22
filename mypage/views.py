from django.shortcuts import render


def mypage(request):
    return render(request, "mypage/mypage.html")


def store_list(request):
    return render(request, "mypage/store_list.html")