from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'amount', 'buyer_name', 'buyer_email', 'buyer_tel',
                    'recipient_name', 'recipient_tel', 'recipient_postcode', 'recipient_add',
                    'recipient_add_detail', 'recipient_memo',)
        widgets = {
            'name': forms.HiddenInput,
            'amount': forms.HiddenInput,
            'buyer_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'buyer_email': forms.TextInput(attrs={'class': 'email', 'readonly': 'readonly'}),
            'buyer_tel': forms.TextInput(attrs={'placeholder': '휴대폰 번호'}),
            'recipient_name': forms.TextInput(attrs={'placeholder': '이름'}),
            'recipient_tel': forms.TextInput(attrs={'placeholder': '휴대폰 번호'}),
            'recipient_postcode': forms.TextInput(attrs={'placeholder': '우편번호'}),
            'recipient_add': forms.TextInput(attrs={'placeholder': '주소'}),
            'recipient_add_detail': forms.TextInput(attrs={'placeholder': '상세주소'}),
            'recipient_memo': forms.TextInput(attrs={'placeholder': '배송메시지'}),
        }