from django.shortcuts import render, redirect, HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from api.models import product_model
from django.views import View
import requests
import json
# Create your views here.

class dashboard_class(View):
    product_url = 'http://127.0.0.1:8000/api/products/products/?page_size=100000'
    costumer_url =  'http://127.0.0.1:8000/api/customers/?page_size=100000'
    
    def get(self, request):
        
        product_response = requests.get(url=self.product_url)
        if product_response.status_code==200:
            product_data = product_response.json()
        
        customer_response = requests.get(url=self.costumer_url)
        if customer_response.status_code==200:
            customer_data = customer_response.json()

        context = {"product_data":product_data, "customer_data": customer_data}
        return render(request=request, template_name='p_o_s/dashboard.html', context=context)

    def post():
        pass


class product_class(ListAPIView):
    base_url =  'http://127.0.0.1:8000/api/products/products/'
    # queryset = product_model.objects.all()
    headers = {}
    
    # @method_decorator(cache_page(60*15))
    
    def get(self, request, **kwargs):
        
        if kwargs:
            if kwargs['method'] == 'PAGE':
                url = f'{self.base_url}?page={kwargs['id']}'
            
            elif kwargs['method'] == 'ADD':
                context = {}
                return render(request=request, template_name='p_o_s/product_new.html', context=context)
            
            elif kwargs['method'] == 'DELETE':
                url = f'{self.base_url}{kwargs["id"]}/'
                response = requests.delete(url=url)
                if response.status_code==204:
                    return redirect("product")
                else:
                    return HttpResponse(response.content)
            
            elif kwargs['method'] == 'UPDATE':
                url = f'{self.base_url}{kwargs["id"]}'
                response = requests.get(url=url, headers=self.headers)
                if response.status_code==200:
                    data = response.json()
                else:
                    return HttpResponse(response.content)
                context = data
                return render(request=request, template_name='p_o_s/product_new.html', context=context)
        else:
            url = self.base_url
        
        response = requests.get(url, headers=self.headers)
        print(f"response is {response}, for url {url}")
        if response.status_code == 200:
            data = response.json()
            context = data
            return render(request=request, template_name='p_o_s/product.html', context=context)
        else:
            return HttpResponse(response.content)


    def post(self, request, *args, **kwargs):

        if request.method == "POST":
            data = request.POST.dict()
            for key, value in data.items():
                if not value:
                    value = None
        
        if kwargs:            
            if kwargs['method'] == 'ADD':
                response = requests.post(url = self.base_url, headers=self.headers, json = data )
                if response.status_code==201:
                    return redirect("product")
                else:
                    return HttpResponse(response.content)
            elif kwargs['method'] == 'UPDATE':
                url = f'{self.base_url}{kwargs["id"]}/'
                response = requests.put(url=url, json=data)
                if response.status_code==200:
                    return redirect('product')
                else: 
                    return HttpResponse(response.content)
                
        context = {}
        return render(request=request, template_name='p_o_s/product_new.html', context=context)

class customer_class(View):
    
    url =  'http://127.0.0.1:8000/api/customers/'

    def get(self, request, *args, **kwargs):

        if kwargs:
            if kwargs['method'] == 'ADD':
                context = {}
                return render(request=request, template_name='p_o_s/customer_new.html', context=context)
            
            if kwargs['method'] == 'UPDATE':
                url = self.url + f'/{kwargs['id']}'
                headers = {}
                response = requests.get(url,headers=headers)
                if response.status_code == 200:
                    data = response.json()
                else:
                    HttpResponse('error')

                context = data
                print("context of updated data is ",context)
                print(context['name'])
                print("returning the data to template")
                return render(request=request, template_name='p_o_s/customer_new.html', context=context)
        
        context = {}
        print("default of get in customers")
        return render(request=request, template_name='p_o_s/customer.html', context=context)

    def post(self, request, *args, **kwargs):

        url =  self.url
        headers = {'Content-Type': 'application/json'}

        if request.method == "POST":
            payload = request.POST.dict()
            print("recieved data is :", payload)

            for key, value in payload.items():
                if not value:
                    payload[key] = None
            
            print("data updated: ", payload)

        if kwargs:
            if kwargs['method']=='ADD':
                response = requests.post(url, headers=headers, json=payload)
                if response.status_code==201:
                    return redirect('customer')
                else:
                    return HttpResponse(f'Error: {response.content}')

            if kwargs['method']=='UPDATE':
                url = self.url + f'/{kwargs['id']}/'
                response = requests.put(url, headers=headers, json=payload)
                if response.status_code==200:
                    return redirect('customer')
                else:
                    return HttpResponse(f'Error: {response.content}')
        

        else:
            return render(request=request, template_name='p_o_s/customer.html', context={})

class stats_class(View):
    
    def get(self, request):
        context = {}
        return render(request=request, template_name='p_o_s/stats.html', context=context)

    def post():
        pass

class settings_class(View):
    
    def get(self, request):
        context = {}
        return render(request=request, template_name='p_o_s/settings.html', context=context)

    def post():
        pass