from django.db import models
class Region(models.Model):
    region_name = models.CharField(max_length=100,null=True)
    longitute = models.CharField(max_length=20,null=True)
    latitute = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.region_name
class Territorie(models.Model):
    territorie_name = models.CharField(max_length=100, null=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    longitute = models.CharField(max_length=20, null=True)
    latitute = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.territorie_name
