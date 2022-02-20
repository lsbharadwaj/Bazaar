from rest_framework import viewsets
from .models import Product, Store
from .serializers import ManageProductSerializer, ProductSerializer, StoreSerializer, StoreWithContactSerializer
from rest_framework import permissions
from rest_framework import exceptions
from .permissions import IsOwnerOrReadOnly,IsProductOwner,IsProductOwnerOrReadOnly
from rest_framework.decorators import action

# Create your views here.
class StoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint which allows displaying stores
    """
    queryset =  Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        try:
           serializer.save(user=self.request.user)
        except Exception as e:
            raise exceptions.ValidationError('Store already exists')
    
    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return StoreWithContactSerializer
        else:
            return StoreSerializer



class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoing which allows displaying products
    """
    queryset =  Product.objects.filter(publish=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    

class ManageProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint which allows managing products
    """
    serializer_class = ManageProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsProductOwner]
    def get_queryset(self):
        queryset = Product.objects.none()
        try:
            store = Store.objects.get(user=self.request.user)
            queryset =  Product.objects.filter(store=store)
        except:
            pass
        return queryset

    def perform_create(self, serializer):
        try:
            store = Store.objects.get(user=self.request.user)
            serializer.save(store=store)
        except Exception as e:
            raise exceptions.ValidationError('Create a Store first')