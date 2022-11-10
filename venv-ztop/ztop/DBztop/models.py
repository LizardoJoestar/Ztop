from django.db import models
from django.db.models import Q
from .field_choices import *

# Create your models here.

# Inventory section of the database


class Inventory(models.Model):
    location = models.CharField(
        max_length=50,
        choices=LOCATION_CHOICES
    )
    dept = models.CharField(
        max_length=50,
        choices=DEPARTMENTS_CHOICES
    )
    serial_num = models.CharField(max_length=50)
    inv_num = models.CharField(max_length=50)

    def __str__(self):
        return self.inv_num

    # Meta means model metadata, check django documentation for more
    class Meta:
        verbose_name_plural = 'Inventory'
        constraints = [
            models.UniqueConstraint(
                fields=['serial_num'], name='unique_serial'),
            models.UniqueConstraint(fields=['inv_num'], name='unique_inv'),
            models.UniqueConstraint(
                fields=['serial_num', 'inv_num'], name='unique_idnumbers'),
            models.CheckConstraint(check=Q(inv_num__endswith='_ITT') | Q(
                inv_num__endswith='_Otay') | Q(inv_num__endswith='_Radio'), name='check_inv_location'),
            models.CheckConstraint(check=Q(location__iexact='tomas aquino') | Q(
                location__iexact='otay') | Q(location__iexact='fracc monterrey'), name='check_location')
        ]


class Consumables(models.Model):
    ID_inv = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    typeOf = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.typeOf + ' ' + self.brand

    class Meta:
        verbose_name_plural = 'Consumables'


class ItemType(models.Model):
    # General characteristics. Defines item type and general attributes
    ID_inv = models.ForeignKey(Inventory, on_delete=models.CASCADE)

    typeOf = models.CharField(
        max_length=10,
        choices=ITEM_TYPE_CHOICES
    )

    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    # Monitor specific attributes
    vga = models.CharField(
        max_length=20,
        choices=MONITOR_PORT_CHOICES,
        default=INVALID
    )

    hdmi = models.CharField(
        max_length=20,
        choices=MONITOR_PORT_CHOICES,
        default=INVALID
    )

    display_port = models.CharField(
        max_length=20,
        choices=MONITOR_PORT_CHOICES,
        default=INVALID
    )

    screen_size = models.IntegerField()

    # PC specific attributes
    os = models.CharField(
        max_length=20,
        choices=OS_CHOICES,
        default=WINDOWS_10
    )

    ram = models.IntegerField()
    cpu = models.CharField(max_length=50)

    driveType = models.CharField(
        max_length=5,
        choices=DRIVE_TYPE_CHOICES,
        default=HDD
    )

    driveSize = models.IntegerField()

    def __str__(self):
        return self.typeOf + ' ' + self.brand + ' ' + self.model

    class Meta:
        verbose_name_plural = 'ItemType'


class History(models.Model):
    # History log fields
    ID_inv = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    date = models.DateTimeField('Date logged')
    location = models.CharField(max_length=50)  # This must be Unit + Dept
    user = models.CharField(max_length=100)
    job_notes = models.TextField()

    # Component fields, at time of logging
    os = models.CharField(
        max_length=20,
        choices=OS_CHOICES,
        default=NONE
    )

    driveType = models.CharField(
        max_length=10,
        choices=DRIVE_TYPE_CHOICES,
        default=NONE
    )

    driveSize = models.IntegerField()
    ram = models.IntegerField()
    cpu = models.CharField(max_length=50)

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
            models.UniqueConstraint(
                fields=['name', 'email'], name='unique_employee')
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
            models.UniqueConstraint(
                fields=['name', 'email'], name='unique_technician')
        ]


class Request(models.Model):
    ID_inv = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    ID_user = models.ForeignKey(UserRegular, on_delete=models.CASCADE)
    date = models.DateTimeField('Date created')
    assignedTo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = 'Request'


class Ticket(models.Model):
    ID_req = models.ForeignKey(Request, on_delete=models.CASCADE)
    ID_tech = models.ForeignKey(UserTech, on_delete=models.CASCADE)
    assigned = models.BooleanField()
    dateCreation = models.DateTimeField('Date created')
    dateAssign = models.DateTimeField('Date assigned', null=True, blank=True)
    dateFinish = models.DateTimeField('Date finished', null=True, blank=True)

    def __str__(self):
        return 'Ticket from' + ' ' + str(self.dateCreation)

    class Meta:
        verbose_name_plural = 'Ticket'
