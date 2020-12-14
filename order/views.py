import decimal
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets

from .models import (
    Size,
    Pizza,
    Order,
    Topping,
    ToppingType,
    Order
)
from .serializers import (
    SizeSerializer,
    ToppingSerializer,
    CreateToppingSerializer,
    ToppingTypeSerializer,
    CreateToppingTypeSerializer,
    PizzaSerializer,
    OrderSerializer
)


class SizeViewSet(viewsets.ModelViewSet):
    """ pizza size model viewset """
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

    def list(self, request):
        serializer = SizeSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToppingTypeViewSet(viewsets.ModelViewSet):
    """ pizza topping type model viewset """
    queryset = ToppingType.objects.all()
    serializer_class = ToppingTypeSerializer

    def list(self, request):
        serializer = ToppingTypeSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            size = Size.objects.get(id=request.data['size'])
            topping_obj = ToppingType.objects.create(
                name=request.data['name'],
                price=request.data['price'],
                size=size
            )
            serializer = CreateToppingTypeSerializer(topping_obj)
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ToppingViewSet(viewsets.ModelViewSet):
    """ pizza topping model viewset """
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

    def list(self, request):
        serializer = ToppingSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            topping_type = ToppingType.objects.get(
                id=request.data['topping_type'])
            topping_obj = Topping.objects.create(
                name=request.data['name'],
                topping_type=topping_type,
            )
            serializer = CreateToppingSerializer(topping_obj)
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PizzaViewSets(viewsets.ModelViewSet):
    """ pizza model viewsets """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def list(self, request):
        serializer = PizzaSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            size_obj = Size.objects.get(name=request.data['size'])
            pizza = Pizza.objects.create(
                size=size_obj
            )
            pizza.price = size_obj.price
            toppings = request.data['toppings']
            for topping in toppings:
                pizza.toppings.add(topping)
                for p in pizza.toppings.all():
                    pizza.price += p.topping_type.price
                    break
            pizza.save()
            serializer = PizzaSerializer(pizza)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.ModelViewSet):
    """ pizza order viewset  """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):
        serializer = OrderSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            order = Order.objects.create()
            pizzas = request.data['pizzas']
            for pizza in pizzas:
                order.pizzas.add(pizza)
                order.total = decimal.Decimal('0.00')
                for o in order.pizzas.all():
                    order.total += o.price
            order.subtotal = decimal.Decimal('0.00')
            vat = order.total * decimal.Decimal('0.16')
            subtotal = order.total + vat
            order.subtotal += subtotal
            order.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
