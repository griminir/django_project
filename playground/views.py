from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product
# Create your views here.


def say_hello(request):
    # complex lookup needs the Q object ~Q means not, (| or), (& and)
        # Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))

    # F object allows us to reference the value of a field in the database
        # queryset = Product.objects.filter(inventory=F('unit_price'))
        # queryset = Product.objects.filter(inventory=F('collection__id'))

    # sorting adding a - in front of the field name reverses the order
        # queryset = Product.objects.order_by('unit_price', '-title')
    # grabbing the one specific object
        # product = Product.objects.order_by('unit_price')[0]
        # procuct = Product.objects.earliest('unit_price')
    
    

    return render(request, 'hello.html', {'name': 'timmy', 'products': list(queryset)})
