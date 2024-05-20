from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class product_category_model(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class product_model(models.Model):
    name = models.CharField(max_length=100 , blank=True, null=True)
    category = models.ForeignKey(product_category_model, on_delete=models.SET_NULL, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.IntegerField( blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class customer_model(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} | {self.father_name}"
    
class order_model(models.Model):
    PAYMENT_CHOICES = [
        ('PAID', 'Paid'),
        ('PAY_LATER', 'Pay Later'),
    ]

    customer = models.ForeignKey(customer_model, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='PAID',blank=True, null=True)
    transaction_id = models.CharField(max_length=100,blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class orderitem_model(models.Model):
    product = models.ForeignKey(product_model, on_delete=models.SET_NULL,blank=True, null=True)
    order = models.ForeignKey(order_model, on_delete=models.SET_NULL,blank=True, null=True)
    quantity = models.IntegerField(default=0,blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name
