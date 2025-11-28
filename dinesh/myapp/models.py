from django.db import models
from django.contrib import admin
class bigbasket(models.Model):
	product_name=models.CharField(max_length=100)
	price=models.IntegerField(primary_key=True)
	quantity=models.CharField(max_length=10)
	dimensions=models.CharField(max_length=20)
	model_year=models.DateField()
	body_material=models.CharField(max_length=20)
	email=models.EmailField()
class bigbasketAdmin(admin.ModelAdmin):
	
	list_display=["product_name","price","quantity","dimensions","model_year","body_material","email"]