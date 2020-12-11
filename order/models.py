from django.db import models
import decimal
from decimal import Decimal

quant = Decimal('0.01')


class Size(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


TOPPING_TYPE = (
    ('Basic Toppings', 'Basic Toppings'),
    ('Deluxe Toppings', 'Deluxe Toppings'),
)


class Topping(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    topping_type = models.CharField(choices=TOPPING_TYPE, max_length=20)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    size = models.ForeignKey(Size, null=True, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if not Pizza.objects.filter(id=self.id):
            super(Pizza, self).save(*args, **kwargs)
        unit_price = Decimal('0.00')
        if self.size:
            unit_price = self.size.price
            for topping in self.toppings.all():
                if topping.price:
                    unit_price += topping.price
        self.price = decimal.Decimal(str(unit_price)).quantize(quant)
        print(unit_price)
        super(Pizza, self).save(*args, **kwargs)

    def __str__(self):
        if self.size.name:
            name = self.size.name
        name = 'Pizza'
        for topping in self.toppings.all():
            if topping.name:
                name = name + ', ' + topping.name
        return name


class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza, blank=True)
    subtotal = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)
