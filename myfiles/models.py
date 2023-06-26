from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=60)
    company_name = models.CharField(max_length=60)
    link = models.CharField(max_length=200)
    deadline = models.DateField()
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    description = models.TextField()
    pictures1 = models.ImageField(upload_to='media')
    pictures2 = models.ImageField(upload_to='media',null=True,blank=True)
    pictures3= models.ImageField(upload_to='media',null=True,blank=True)
    date = models.DateTimeField(auto_now=True)




class Services(models.Model):
    pictures1 = models.ImageField(upload_to='media')
    name = models.CharField(max_length=60)
    description = models.TextField()



class Team(models.Model):
    pictures1 = models.ImageField(upload_to='media')
    name = models.CharField(max_length=60)
    lavozim = models.CharField(max_length=60)
    description = models.TextField()

class Malumot_saqlash(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    subject = models.CharField(max_length=60)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)


class Subr(models.Model):
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)

