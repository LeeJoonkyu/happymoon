from django.shortcuts import render
from .models import Article
# Create your views here.


def notice_list(request):
    articles = Article.objects.all().order_by('-created_at')
    ctx = {
        'articles': articles
    }
    return render(request, 'notice_list/notice_list.html', ctx)


def notice_detail(request, pk):
    ctx = {
        'article': Article.objects.get(pk=pk)
    }
    return render(request, 'notice_list/notice_detail.html', ctx)


def notice_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article()
        article.title = title
        article.content = content
        article.save()

    return render(request, 'notice_create.html')

# def listing(request):
#     article_list = Article.objects.all()
#     paginator = Paginator(page_list, 10)
#     page = request.GET.get('page')
#     articles = paginator.get_page(page)
#     return render(request, '')