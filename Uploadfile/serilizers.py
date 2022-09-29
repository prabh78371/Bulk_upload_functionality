from .models import Product
from rest_framework import serializers

class Productserilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 0