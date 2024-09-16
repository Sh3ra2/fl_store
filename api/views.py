from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from django.views import View
from rest_framework import permissions, status, generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from django_filters import rest_framework as filters
from . import custom_filters
from . import models
from . import serializer
from django.views.decorators.cache import cache_page
# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100000


class product_api_class(viewsets.ModelViewSet):

    permission_classes = [AllowAny]
    queryset = models.product_model.objects.all().order_by('name')
    serializer_class = serializer.product_model_serializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = custom_filters.product_api_filter


# -------------------cache-----------------
@cache_page(60*15)
def cached(request):
    model = models.customer_model.objects.all()
    return HttpResponse('<html><body><h1>{0} .users cached</h1></body></html>'. format(len(model)))

def cacheless(request):
    model = models.customer_model.objects.all()
    return HttpResponse('<html><body><h1>{0} .users cacheless</h1></body></html>'. format(len(model)))


# Not used API view because it is easy to just 
# send request in this generic view, to delete/edit it in apis
class customer_api_class(generics.ListCreateAPIView):

    permission_classes = [AllowAny]
    queryset = models.customer_model.objects.all().order_by('name')
    serializer_class = serializer.customer_model_serializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class =  custom_filters.customer_api_filter


class customer_details_class(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [AllowAny]

    queryset = models.customer_model.objects.all()
    serializer_class = serializer.customer_model_serializer
