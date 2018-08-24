from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    def save(self):
        print('저장되었습니다.')
        return super(Article, self).save()


class Comment(models.Model):
    content = models.TextField(verbose_name = '댓글')
    author = models.CharField(max_length=10, verbose_name='글쓴이')
    article = models.ForeignKey(Article, on_delete= models.CASCADE)
