from django.db import models

# Create your models here.

# Inventory section of the database

class Inventory(models.Model):
    location = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    serial_num = models.CharField(max_length=50)
    inv_num =  models.CharField(max_length=50)

    def __str__(self):
        return self.inv_num

    # Meta means model metadata, check django documentation for more
    class Meta:
        verbose_name_plural = 'Inventory'
        constraints = [
            models.UniqueConstraint(fields=['serial_num', 'inv_num'], name = 'unique_idnumbers')
        ]

class Consumables(models.Model):
    ID_inv = models.ForeignKey(Inventory, on_delete = models.CASCADE)
    typeOf = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.typeOf + ' ' + self.brand

    class Meta:
        verbose_name_plural = 'Consumables'

class ItemType(models.Model):
    ID_inv = models.ForeignKey(Inventory, on_delete = models.CASCADE)
    typeOf = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.typeOf + ' ' + self.brand + ' ' + self.model

    class Meta:
        verbose_name_plural = 'ItemType'
    
class History(models.Model):
    ID_inv = models.ForeignKey(Inventory, on_delete = models.CASCADE) 
    date = models.DateTimeField('Date logged')
    updated = models.BooleanField()
    user = models.CharField(max_length=100)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = 'History'

# Ticket and users section of the database

class UserRegular(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name + ' ' + self.dept

    class Meta:
        verbose_name_plural = 'UserRegular'
        constraints = [
            models.UniqueConstraint(fields=['name', 'email'], name='unique_employee')
        ]

class UserTech(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    roles = models.CharField(max_length=300)

    def __str__(self):
        return self.name + ' ' + self.dept 
    
    class Meta:
        verbose_name_plural = 'UserTech'
        constraints = [
            models.UniqueConstraint(fields=['name', 'email'], name='unique_technician')
        ]

class Request(models.Model):
    ID_inv = models.ForeignKey(Inventory, on_delete = models.CASCADE)
    ID_user = models.ForeignKey(UserRegular, on_delete = models.CASCADE)
    date = models.DateTimeField('Date created')
    assignedTo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = 'Request'

class Ticket(models.Model):
    ID_req = models.ForeignKey(Request, on_delete = models.CASCADE)
    ID_tech = models.ForeignKey(UserTech, on_delete = models.CASCADE)
    assigned = models.BooleanField()
    dateCreation = models.DateTimeField('Date created')
    dateAssign = models.DateTimeField('Date assigned', null=True, blank=True)
    dateFinish = models.DateTimeField('Date finished', null=True, blank=True)

    def __str__(self):
        return 'Ticket from' + ' ' + str(self.dateCreation)

    class Meta:
        verbose_name_plural = 'Ticket'
    


