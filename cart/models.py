from django.db import models
from register.models import CustomUser
from product.models import Product, Manufacturer, Category
# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.customuser.email

class CartList(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quatity = models.PositiveIntegerField()

    def __str__(self):
        return '{}, {}'.format(self.product.name, self.quatity)
    
    


    
