from rest_framework import serializers
from . import models

class customer_model_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.customer_model
        fields = '__all__'


class product_model_serializer(serializers.ModelSerializer):
    class Meta:
        model =  models.product_model
        fields = '__all__'
