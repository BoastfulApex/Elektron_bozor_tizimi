from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import *
from .serializer import *
import json


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CategoriesView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductByCategoryView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def retrieve(self, request, *args, **kwargs):
        category_id = kwargs['pk']
        products = self.queryset.filter(category_id=category_id)
        serializer = self.get_serializer(products,many=True)
        return Response(serializer.data)


class OrdersView(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        order = self.queryset.get(id=id)
        order.set_bal_emp()
        serializer = self.get_serializer(order)
        return Response(serializer.data)


class OrderDetailsView(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer


class OrderDetailsActionsView(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer

    def update(self, request, *args, **kwargs):
        od_id = kwargs['pk']
        data = json.loads(request.body)
        order_detail = self.queryset.get(id=od_id)
        order_detail.actions(data)
        return Response({'quantity': order_detail.quantity})

