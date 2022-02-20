from dataclasses import fields
from pyexpat import model
from turtle import title
from rest_framework import serializers
from .models import Product, Store

class StoreSerializer(serializers.HyperlinkedModelSerializer):

    products = serializers.StringRelatedField(many=True)
    class Meta:
        model = Store
        fields = ['name','shop_img','url','products','id']

class StoreWithContactSerializer(serializers.HyperlinkedModelSerializer):
    # products = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='product-detail')
    products = serializers.HyperlinkedIdentityField(many=True,view_name='product-detail')
    class Meta:
        model = Store
        fields = ['name','contact_no','shop_img','url','products','id']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description','price','url','product_img','store','id']
        # extra_kwargs = {'shop_url':{'lookup_field':'store'}}



class ManageProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description','price','url','publish','product_img','id']
        extra_kwargs={'url':{'view_name':'manage_product-detail'}}