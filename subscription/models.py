from django.db import models

# Create your models here.


class Type(models.Model):
    img = models.ImageField()
    type = models.CharField(max_length=20)
    component = models.TextField()
    detail = models.TextField()
    # 여기 type이라는 게 실속파, 중형파 뭐 이런거지 앞에 붙는 A, B, C를 포함하는 게 아님
    price = models.IntegerField()
    price_before = models.IntegerField(null=True)



