from django.db import models
from decimal import Decimal
from django.contrib.auth.models import AbstractUser, Group, Permission

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = "Product Category"
        verbose_name = "Product Categories"
        
    def str(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    price = models.DecimalField(max_digits=999999999999, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/products{self.slug}/'
    
    
class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255,blank=True)
    phone_number = models.CharField(max_length=255,blank=True)
    is_active = models.BooleanField(default=True)
    
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)
    
    
    def __str__(self):
        return self.email
    
    
