import django_filters
from django_filters import DateFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    # Sets filter for greater then or equal to date specified 
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    # Sets filter for less then or equal to date specified 
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']