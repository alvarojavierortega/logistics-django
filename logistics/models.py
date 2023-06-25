from django.db import models
from django.db.models.deletion import CASCADE

class Client(models.Model):
    class Meta:
        db_table = "client"
        verbose_name_plural = "clients"

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Carrier(models.Model):
    class Meta:
        db_table = "carrier"
        verbose_name_plural = "carriers"

    CHOICES = [
        ("Plane", "Plane"),
        ("Truck", "Truck"),
        ("Ship", "Ship")] 

    name = models.CharField(max_length=50)
    vehicle_type = models.CharField(
        max_length=5,
        choices=CHOICES
    )
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Package(models.Model):
    class Meta:
        db_table = 'package'
        verbose_name_plural = "packages"
    
    CHOICES = [
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Canceled", "Canceled")]
    
    owner = models.ForeignKey(Client, related_name='packages', on_delete=models.CASCADE)
    carrier = models.ForeignKey(Carrier, related_name='packages', on_delete=models.CASCADE, null=True)
    weight = models.IntegerField()
    size = models.CharField(max_length=50)
    origin_address = models.CharField(max_length=200)
    destination_address = models.CharField(max_length=200)
    delivery_status = models.CharField(
        max_length=9,
        choices=CHOICES,
        null=True,
    )
    

    


