from django.db import models
from django.contrib.auth.models import User
class OtherUsers(models.Model):
    user = models.CharField(max_length=50,blank=False)
    phone = models.IntegerField(blank=False)
    rollNo=models.CharField(max_length=40,blank=False)
    Mail_Id = models.CharField(max_length=200, blank=False )

    def __str__(self):
        return self.user
