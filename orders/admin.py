from django.contrib import admin

# Register your models here.
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display=('user_id' , 'total_price', 'address', 'order_date', 'delivery_date','order_id'
)

admin.site.register(Order,OrderAdmin)