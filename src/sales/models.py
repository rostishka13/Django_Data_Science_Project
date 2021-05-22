from django.db import models
from django.shortcuts import reverse
from products.models import Product
from customers.models import Customers
from profiles.models import Profile
from django.utils import timezone
from .utils import generate_code
# Create your models here.
#product times quantity
class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"id:{self.id}, product: {self.product.name}, quantity: {self.quantity}"



class Sales(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()

        if self.created is None:
            self.created = timezone.now()

        return super().save(*args, **kwargs)

    #this method allow us to navigate to particular page based on the app name and the name that we''e set in the path
    def get_absolute_url(self):
        return reverse('sales:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return f"Sales for the amount of $: {self.total_price}"
    def get_positions(self):
        return self.positions.all()



class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)