from django.db import models

# Create your models here.
class Order(models.Model):
    user_id = models.CharField(max_length=32)
    total_price = models.DecimalField(max_digits=50,decimal_places=4)
    address= models.CharField(max_length=32)
    order_date= models.DateTimeField(auto_now_add=True)
    delivery_date=models.DateTimeField()
    order_id = models.CharField(max_length=32)

    def __str__(self):
        return self.user_id
    
    #Attribute



