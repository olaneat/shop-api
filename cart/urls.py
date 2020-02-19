from django.urls import path
from .apiviews import CartList

app_name = 'cart'

urlpatterns = [
    path('<int:pk>/list', CartList.as_view(), name='shopping_list'),
]
