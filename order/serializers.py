from rest_framework import serializers
from .models import (
    Size,
    Pizza,
    Order,
    Topping,
    ToppingType
)


class SizeSerializer(serializers.ModelSerializer):
    """ Pizza size serializer """
    class Meta:
        model = Size
        fields = '__all__'
        read_only_fields = ('id',)


class ToppingTypeSerializer(serializers.ModelSerializer):
    """ Topping Type serializer """
    size = SizeSerializer(read_only=True)

    class Meta:
        model = ToppingType
        fields = '__all__'


class CreateToppingTypeSerializer(serializers.ModelSerializer):
    """ Create Topping Type Serializer """
    class Meta:
        model = ToppingType
        fields = [
            'name',
            'price',
            'size'
        ]


class ToppingSerializer(serializers.ModelSerializer):
    """ Pizza Topping serializer """
    topping_type = ToppingTypeSerializer(read_only=True)

    class Meta:
        model = Topping
        fields = '__all__'
        read_only_fields = ('id',)


class CreateToppingSerializer(serializers.ModelSerializer):
    """ create pizza topping serializer """
    class Meta:
        model = Topping
        fields = [
            'topping_type',
            'name'
        ]


class PizzaSerializer(serializers.ModelSerializer):
    """ pizza serializer """
    class Meta:
        model = Pizza
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """ order serializer """
    class Meta:
        model = Order
        fields = '__all__'
