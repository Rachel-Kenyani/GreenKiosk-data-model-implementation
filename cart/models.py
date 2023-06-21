from django.db import models

# Create your models here.
class Shopping_cart(models.Model):
    user_id = models.CharField(max_length=32)
    total_price = models.DecimalField(max_digits=50,decimal_places=2)
    stock = models.PositiveIntegerField()
    

    def __str__(self):
        return self.user_id