from rest_framework import generics 
from .serializers import CartListSerializer
from .models import Cart, CartList

class CartList(generics.ListCreateAPIView):
    serializer_class = CartListSerializer
    def get_queryset(self):
        queryset = CartList.objects.filter(user_id = self.kwargs['pk'])
        price = queryset.get_product_name
        name = queryset.get_price
        context = {'name': name, 'price': price}
        return context    
    