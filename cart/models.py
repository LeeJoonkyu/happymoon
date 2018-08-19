from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #item = models.ForeignKey(Item, on_delete=models.CASCADE)
    merchant_uid = models.UUIDField(default=uuid4, editable=False) #uuid4 ; 임의의 id부여해줌/ 수정불가능하게 editable False
    imp_uid = models.CharField(max_length=100, blank=True) #결제완료된 후 받아오는 값이므로 처음에는 blank
    name = models.CharField(max_length=100, verbose_name="상품명")
    amount = models.PositiveIntegerField(verbose_name="결제금액")
    status = models.CharField(
            max_length=9,
            choices=(
                    ('ready',       '미결제'),
                    ('paid',        '결제완료'), 
                    ('cancelled',   '결제취소'), 
                    ('failed',      '결제실패'),
                    ),
            default='ready',
            db_index=True)
    meta = JSONField(blank=True, default={})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    