from django.db import models
import decimal
from decimal import Decimal

quant = Decimal('0.01')


class Size(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


TOPPING_TYPE = (
    ('Basic Toppings', 'Basic Toppings'),
    ('Deluxe Toppings', 'Deluxe Toppings'),
)


class ToppingType(models.Model):
    name = models.CharField(choices=TOPPING_TYPE, max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    size = models.ForeignKey(Size, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=30)
    topping_type = models.ForeignKey(
        ToppingType, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    size = models.ForeignKey(Size, null=True, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        if self.size.name:
            name = self.size.name
        name = 'Pizza'
        for topping in self.toppings.all():
            if topping.name:
                name = name + ', ' + topping.name + \
                    ', ' + str(topping.topping_type.price)
        return name


class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza, blank=True)
    subtotal = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)
