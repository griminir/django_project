from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem
# Create your views here.

# remember you can chain queries together or you can save it to a variable then query it again
def queries(request): 
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
    
    # limiting the number of results
        # queryset = Product.objects.all()[:3] 0,1,2
        # queryset = Product.objects.all()[3:6] 3,4,5
    
    # selecting fields
        # collection__title lets us grab the title of the collection with an inner join
        # queryset = Product.objects.values('title', 'unit_price', 'collection__title')
        # queryset = Product.objects.values_list('title', 'unit_price')
    
    # what a more complex query looks like
        # this gets the products that have been ordered
        # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    

    return render(request, 'hello.html', {'name': 'timmy', 'products': list(queryset)})
