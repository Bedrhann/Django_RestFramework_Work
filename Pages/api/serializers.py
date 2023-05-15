from rest_framework import serializers
from ..models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    explanation = serializers.CharField()
    # price = serializers.FloatField()

    def create(self, validated_data):
        print(validated_data)
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.explanation = validated_data.get('explanation',instance.explanation)
        # instance.price = validated_data.get('price',instance.price)
        instance.save()
        return instance
        






