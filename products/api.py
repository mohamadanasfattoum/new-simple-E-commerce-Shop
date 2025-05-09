from django.shortcuts import render
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer



class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
