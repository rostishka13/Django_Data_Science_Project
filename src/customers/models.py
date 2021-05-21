from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='customers', default='no_picture.png')

    #string representation
    def __str__(self):
        return str(self.name)


