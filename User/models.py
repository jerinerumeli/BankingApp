from django.db import models

from BankingApp.settings import time as datetime
# Create your models here.


MONTH_CHOICES = (
    ("Credited", "CR"),
    ("Debited", "DD"),
)

class authCredentials(models.Model):
    id = models.BigAutoField(primary_key=True)
    emailid = models.CharField(max_length=300,unique=True)
    password = models.CharField(max_length=500)
    token = models.CharField(max_length=500, null=True)
    timestamp = models.CharField(default=datetime,editable=True,max_length=50)

    def __str__(self):
        return self.id


class userAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_number = models.CharField(max_length=100,null=True)
    transaction = models.IntegerField(editable=True)
    transaction_id = models.CharField(max_length=500,default=100)  #,unique=True
    type = models.CharField(max_length=100,choices=MONTH_CHOICES,default="failed")
    account = models.ForeignKey(authCredentials,on_delete=models.CASCADE,related_name="account",null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

class createUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15,unique=True)
    address = models.TextField()
    account_number = models.CharField(max_length=100,null=True)
    balance = models.IntegerField(null=True,editable=True)
    auth = models.OneToOneField(authCredentials,on_delete=models.CASCADE,related_name="userinfo",null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name