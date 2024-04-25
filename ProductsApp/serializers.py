from rest_framework import serializers
from .models import AppFile, Product, ProductImage, Likes


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class AppFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppFile
        fields = '__all__'
