from django.db import models
from django.conf import settings

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='주문상품')
    amount = models.PositiveIntegerField(verbose_name='총 결제금액')

    buyer_name = models.CharField(max_length=50, verbose_name='주문자 이름')
    buyer_email = models.CharField(max_length=100, verbose_name='주문자 이메일')
    buyer_tel = models.CharField(max_length=11, verbose_name='휴대폰번호')
    
    recipient_name = models.CharField(max_length=50, verbose_name='수령인 이름')
    recipient_tel = models.CharField(max_length=11, verbose_name='휴대폰번호')

    recipient_postcode = models.CharField(max_length=10, verbose_name='우편번호')
    recipient_add = models.CharField(max_length=100, verbose_name='주소')
    recipient_add_detail = models.CharField(max_length=100, verbose_name='상세주소')
    recipient_memo = models.CharField(max_length=100, blank=True, null=True, verbose_name='배송메모(선택)')

    #status
    #created_at
    #updated_at