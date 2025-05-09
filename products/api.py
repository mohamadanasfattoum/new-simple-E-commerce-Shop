from django.shortcuts import render
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer



class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateApi(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
