from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    slug = models.SlugField(max_length=150, blank=True)
    available = models.BooleanField(default=False)
    catergory = models.ForeignKey('Category', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_product_name(self):
        return self.name

    def get_price(self):
        return self.price

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    

class Category(models.Model):
    name = models.CharField(max_length = 150)
    slug =  models.SlugField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    


    
    
    
    
