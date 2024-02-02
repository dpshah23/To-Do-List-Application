from django.db import models

# Create your models here.

class customertodo(models.Model):
    uid=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=25)
    email=models.EmailField()
    mobileno=models.CharField(max_length=12)
    password=models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.email
    
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    subject=models.TextField()
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    
class Task(models.Model):
    tname=models.CharField(max_length=250)
    desc=models.TextField()
    status=models.CharField(max_length=50)
    date=models.DateField()
    email=models.CharField(max_length=250)
    category=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tname
