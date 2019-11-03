from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from purchases.pviews import PurchaserViewSet, ProductViewSet, HistoryViewSet 


router = routers.DefaultRouter()
router.register(r'purchaser', PurchaserViewSet)
router.register(r'product', ProductViewSet)
router.register(r'purchaser-product', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
