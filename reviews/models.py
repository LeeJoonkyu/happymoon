from django.db import models
from django.conf import settings
from subscription.models import Type


# Create your models here.
class Review(models.Model):
    STAR_CHOICES = (
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    star = models.IntegerField(choices=STAR_CHOICES)
    #product = models.ForeignKey(Type, blank=True, null=True, on_delete=models.CASCADE) #TODO: 여기 __str__ 수정해야될까?
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        name = str(self.user)+"님의 후기 /"+str(self.created_at)
        return name


class Review_Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,) #related_name="comment_set"
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)