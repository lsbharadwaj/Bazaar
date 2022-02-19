from xml.etree.ElementInclude import include
from django.urls import include,path
from rest_framework import routers
from .views import ManageProductViewSet, ProductViewSet, StoreViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'stores',StoreViewSet)
router.register(r'products',ProductViewSet)
router.register(r'manage_products',ManageProductViewSet,basename='manage_product')

urlpatterns = [
    path('',include(router.urls)),
]