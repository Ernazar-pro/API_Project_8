from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):


    def __str__(self):
        return f'{self.username}'
    
    class Meta:
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['id']
    
class Post(models.Model):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        ordering = ['id']

