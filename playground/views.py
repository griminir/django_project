from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Sum, Avg, Min, Max
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import connection
from store.models import Product, OrderItem, Order, Customer
from tags.models import TaggedItem
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

    # selecting fields value gives us a dictionary
    # collection__title lets us grab the title of the collection with an inner join
    # queryset = Product.objects.values('title', 'unit_price', 'collection__title')
    # queryset = Product.objects.values_list('title', 'unit_price')

    # what a more complex query looks like
    # this gets the products that have been ordered
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    # defering fields gives us instance of the product class
    # the only method can be end up sending multiple queries to the database if you ask for something that is not in the cache
    # queryset = Product.objects.only('id', 'title')
    # the defer method is the opposite of only it defers the fields that you don't want to see
    # queryset = Product.objects.defer('description')

    # selecting releated objects
    # selected_related is used when (1) one collection (foreign key)
    # queryset = Product.objects.select_related('collection').all()
    # prefetch_related is used when (n) many promotions (many to many)
    # queryset = Product.objects.prefetch_related('promotions').all()
    # since both return a queryset you can chain them together
    # queryset = Product.objects.select_related('collection').prefetch_related('promotions').all()

    # more complex example return the 5 last orders with their customer
    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # return render(request, 'hello.html', {'name': 'timmy', 'orders': list(queryset)})

    # aggregating data
    # result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'), max_price=Max('unit_price'), avg_price=Avg('unit_price'), total_price=Sum('unit_price'))
    # return render(request, 'hello.html', {'name': 'timmy', 'result': result})

    # annotating can add new fields to the queryset
    #  queryset = Product.objects.annotate(new_id=F('id') + 100)

    # using database functions
    # queryset = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    # shortcut using Concat
    # queryset = Customer.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))

    # grouping data
    # little quirk here is that you cant count order_set you have to count order
    # queryset = Customer.objects.annotate(orders_count=Count('order'))

    # expression wrappers
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(discounted_price=discounted_price)

    # working with generic relations
    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects \
    #     .select_related('tag') \
    #     .filter(
    #         content_type=content_type,
    #         object_id=1
    #     )
    # using the custom manager code would look like this
    # queryset = TaggedItem.objects.get_tags_for(Product, 1)
    # return render(request, 'hello.html', {'name': 'timmy', 'tags': list(queryset)})

    # raw sql queries
    # queryset = Product.objects.raw('SELECT * FROM store_product WHERE id = %s', [1])
    # plain sql not using model
    # with helps us close the connection automatically when we are done
    # with connection.cursor() as cursor:
    # cursor.execute('SELECT * FROM store_product WHERE id = %s', [1])
    # store procedures
    # cursor.callproc('my_procedure', [1, 2])

    return render(request, 'hello.html', {'name': 'timmy', 'products': list(queryset)})
