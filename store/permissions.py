from rest_framework import permissions
from store.models import Product, Store


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user



class IsProductOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        permitted = False
        try:
            store = Store.objects.get(user=request.user)
            permitted = obj.store == store #If user has store check if the store of the product belongs to user
        except:
            permitted = False # If user doesnt have store then he can't have products to edit
        return permitted



class IsProductOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        # Write permissions are only allowed to the owner of the snippet.
        permitted = False
        try:
            store = Store.objects.get(user=request.user)
            permitted = obj.store == store #If user has store check if the store of the product belongs to user
        except:
            permitted = False # If user doesnt have store then he can't have products to edit
        return permitted # Permitted if published or is the owner