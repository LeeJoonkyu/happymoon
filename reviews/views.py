from django.shortcuts import render
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
    paginator = Paginator(all_reviews, 5)

    page = request.GET.get('page')
    reviews = paginator.get_page(page)
    ctx = {
        'reviews': reviews,
    }
    return render(request, 'reviews/review_list.html', ctx)