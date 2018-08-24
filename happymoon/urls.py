from django.contrib import admin
from django.urls import include, path
from store import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('store/pad/', include('store.urls', namespace="store_pad")),
    path('store/goods/', include('goods.urls', namespace="store_goods")),
    path('', include('subscription.urls', namespace="subscription")),
    path('mypage/', include('mypage.urls', namespace="mypage")),
    path('store/cart/', include('cart.urls', namespace="cart")),
    path('notice_list/', include('notice_list.urls', namespace="notice_list")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
