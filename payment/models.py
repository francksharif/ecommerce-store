from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=250)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250, null=True, blank=True)
    zip_code = models.CharField(max_length=250)
   
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return 'Shipping Adress - ' + str(self.id)
    