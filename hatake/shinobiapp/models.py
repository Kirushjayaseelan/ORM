
from django.db import models
from django.contrib import admin

class user(models.Model):
    Gmail=models.EmailField()
    Mobile_No=models.IntegerField()
    Username=models.CharField(max_length=10,primary_key=True)
    Address=models.TextField()
    Product_Type=models.CharField(max_length=15)
    Product_Name=models.CharField(max_length=15)
    Apply_Coupon=models.CharField(max_length=10)
    
class userinfo(admin.ModelAdmin):
    list_display=["Gmail","Mobile_No","Username","Address","Product_Type","Product_Name","Apply_Coupon"]
