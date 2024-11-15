from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# Create your views here.


def say_hello(request):
    queryset = Product.objects.filter(inventory__lt=10)

    return render(request, 'hello.html', {'name': 'timmy', 'products': list(queryset)})
