from django.db import models
from django.contrib.auth.models import User
from territorie.models import *
from employee.models import Employee
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=200,null=True)
    territorie = models.ForeignKey(Territorie,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.user.username
    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name
class Categories(models.Model):
    category_name = models.CharField(max_length = 200,null=False)
    description = models.CharField(max_length=300,null=True)
    def __str__(self):
        return self.category_name


class Products(models.Model):
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200,null=False)
    price = models.FloatField(null=False)
    image = models.ImageField(null=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE,null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='start',max_length=10)
    employee = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True)
    delivered_date = models.DateTimeField(null=True)

    def set_bal_emp(self):
        print('set_bal_...')
        tr = self.customer.territorie
        emp = Employee.objects.filter(territorie__region=tr)
        for e in emp:
            s,created = Statistic.objects.get_or_create(
                customer=self.customer,
                employe=e
            )
            if e.territories == self.customer.territorie:
                s.ball = 2
            else:
                s.ball = 1
            s.save()
        print(emp)

    def __str__(self):
        return str(self.id) + self.status


class OrderDetails(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,null=True)

    @property
    def total(self):
        return self.quantity * self.product.price

    def add(self,quantity=1):
        self.quantity += quantity
        self.save()

    def sub(self):
        if self.quantity - 1 > 0:
            self.quantity -= 1
            self.save()
        else:
            self.delete()

    def actions(self,data):
        if data['action']=='add':
            self.add(data['quantity'])
        else:
            self.sub()


class Statistic(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    employe = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True)
    ball = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.customer} -> {self.employe} ball: {self.ball}'

