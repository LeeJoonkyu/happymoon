from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Review, Review_Comment
from django.core.paginator import Paginator


# Create your views here.
# without-pagination Or digg-style
# def review_list(request):
#     reviews = Review.objects.all()
#     comments = Review_Comment.objects.all()
#
#     ctx = {
#         'reviews': reviews,
#         'comments': comments,
#     }
#     return render(request, 'reviews/review_list.html', ctx)


# django paginiatior
def review_list(request):
    all_reviews = Review.objects.all()
    all_reviews = all_reviews.order_by('-id')
    paginator = Paginator(all_reviews, 5)

    page = request.GET.get('page')
    reviews = paginator.get_page(page)
    ctx = {
        'reviews': reviews,
    }
    return render(request, 'reviews/review_list.html', ctx)


def review_create(request):
    if request.method == "POST":
        star = request.POST.get('star')
        title = request.POST.get('title')
        content = request.POST.get('content')
        review = Review()
        review.user = request.user
        review.star = star
        review.title = title
        review.content = content
        review.save()
        return redirect(reverse('reviews:review_list'))

    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login"))
    return render(request, 'reviews/review_create.html')