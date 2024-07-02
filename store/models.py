from django.db import models
from django.urls import reverse 


# Create your models here.


class Category(models.Model):
    """ Product category model """
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category-page", args=[self.slug])
    

    


class Product(models.Model):
    """ Product Model """
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='unbranded')
    description = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product-page", args=[self.slug])
    

    
