from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .serializer import *
class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            user = User.objects.create(
                first_name=data['user']['first_name'],
                last_name=data['user']['last_name'],
                username=data['user']['username'],
                email=data['user']['email'],
                password=data['user']['password'],
            )
            user.save()
            employee = Employee.objects.create(
                user=user,
                phone = data['phone'],
                image = data['image'],
                address = data['address'],
            )
            employee.save()
            return Response({'status':'created'},status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def update(self, request, *args, **kwargs):
        print('update..')
        id = kwargs['pk']
        emp = self.queryset.get(id=id)
        user = emp.user
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            print(data)
            if data['user']['first_name']:
                user.first_name = data['user']['first_name']
            if data['user']['last_name']:
                user.last_name = data['user']['last_name']
            if data['user']['username']:
                user.username = data['user']['username']
            if data['user']['password']:
                user.password = data['user']['password']
            if data['user']['email']:
                user.email = data['user']['email']
            user.save()
            if data['phone']:
                emp.phone = data['phone']
            if data['image']:
                emp.image = data['image']
            if data['address']:
                emp.address = data['address']
            if data['territorie']:
                t = data['territorie']
                print(t)
                emp.territorie.clear()
                for i in t:

                    emp.territorie.add(i)
            emp.save()
        return Response({'status':'OK'})
