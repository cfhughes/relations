from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shoe(models.Model):
    color = models.CharField(max_length=45)
    brand = models.CharField(max_length=45)
    owners = models.ManyToManyField(Person, related_name="shoes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

