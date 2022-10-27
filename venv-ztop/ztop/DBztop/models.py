from django.db import models

# Create your models here.

# Inventory section of the database

class Inventory(models.Model):
    location = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    serial_num = models.CharField(max_length=50)
    inv_num =  models.CharField(max_length=50)

class Consumables(models.Model):
    ID_inv = models.ForeignKey(Inventory, on_delete = models.CASCADE)
    typeOf = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

class ItemType(models.Model):
    ID_inv = models.ForeignKey(Inventory, on_delete = models.CASCADE)
    typeOf = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    
class History(models.Model):
    ID_inv = models.ForeignKey(Inventory, on_delete = models.CASCADE) 
    date = models.DateTimeField('Date logged')
    updated = models.BooleanField()
    user = models.CharField(max_length=100)

# Ticket and users section of the database

class UserRegular(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    email = models.EmailField()

class UserTech(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    roles = models.CharField(max_length=300)

class Request(models.Model):
    ID_inv = models.ForeignKey(Inventory, on_delete = models.CASCADE)
    ID_user = models.ForeignKey(UserRegular, on_delete = models.CASCADE)
    date = models.DateTimeField('Date created')
    assignedTo = models.CharField(max_length=100)

class Ticket(models.Model):
    ID_req = models.ForeignKey(Request, on_delete = models.CASCADE)
    ID_tech = models.ForeignKey(UserTech, on_delete = models.CASCADE)
    assigned = models.BooleanField()
    dateCreation = models.DateTimeField('Date created')
    dateAssign = models.DateTimeField('Date assigned')
    dateFinish = models.DateTimeField('Date finished')
    


