from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.customer_model)
admin.site.register(models.order_model)
admin.site.register(models.product_model)

