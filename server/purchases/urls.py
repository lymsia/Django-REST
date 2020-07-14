from django.urls import path
from purchases.views.purchaser import PurchaserList, PurchaserDetail
from purchases.views.product import ProductList, ProductDetail
from purchases.views.history import HistoryList
from purchases.views.purchaser_history import PurchaserHistory
from rest_framework.urlpatterns import format_suffix_patterns
from purchases.root_view import api_root


urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('purchaser/', PurchaserList.as_view(), name='purchaser-list'),
    path('purchaser/<int:pk>/', PurchaserDetail.as_view(), name='purchaser-detail'),
    path('purchaser/<int:pk>/product/', PurchaserHistory.as_view(), name='purchaser-history'),
    path('product/', ProductList.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('purchaser-product/', HistoryList.as_view(), name='history-list'),
])
