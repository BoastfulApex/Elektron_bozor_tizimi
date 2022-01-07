from django.db import models
from django.contrib.auth.models import User
class Moderator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20,null=True)
    image = models.ImageField(null=True)
    @property
    def full_name(self):
        return self.user.first_name+' '+self.user.last_name
    def __str__(self):
        return self.full_name
