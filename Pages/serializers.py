from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    explanation = serializers.CharField()

    def create(self, validated_data):
        return Product.objects.create(validated_data)







