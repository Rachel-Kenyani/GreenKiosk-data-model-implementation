from django.contrib import admin

# Register your models here.

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","birth_date","email","phone_number")

admin.site.register(User,UserAdmin)
   