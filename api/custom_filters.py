from django_filters import rest_framework as filters
from . import models

class customer_api_filter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    father_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.customer_model
        fields = ['name','father_name']

class product_api_filter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = models.product_model
        fields = ['name',]