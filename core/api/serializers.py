from rest_framework import serializers
from core.models import product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ["title", "author", "price"]