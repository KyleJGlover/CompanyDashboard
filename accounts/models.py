from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# class BaseUser(BaseUserManager):    
#     def create_user(self, email, user_name, password, **other_fields):
#         if not email:
#             raise ValueError(_('You must provide an email address'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user
        
#     def create_superuser(self, email, user_name, password, **other_fields):
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_activated', True)
#         if other_fields.get('is_staff'):
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True.'
#             )
#         if other_fields.get('is_superuser'):
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.'
#             )
#         return self.create_user(email, user_name, password, **other_fields)
        
        

class Customer(models.Model):
    USER_ROLES = {
        'admin': 'admin',
        'customer' : 'customer'
    }
    
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null = True)
    phone = models.CharField(max_length=200, null = True)
    email = models.CharField(max_length=200, null = True)
    date_created = models.DateTimeField(auto_now_add=True)
    group = models.CharField(max_length=200, null = True)
    profile_pic = models.ImageField(default="DisplayPlant.jpeg", null = True, blank=True)
    
    def __str__(self):
        return self.name 
    
    class Meta:
        ordering = ['name']
    
# Filter class
class Tag(models.Model):
    name = models.CharField(max_length=200, null = True, unique=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200, null = True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null = True, choices=CATEGORY)
    description = models.CharField(max_length=200, null = True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null = True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null = True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.name