from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Author = models.CharField(max_length=100,null=True,blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Published_at = models.DateTimeField(auto_now=True)
    Updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['Name']
    
    def __str__(self):
        return self.Name


class Author(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Book = models.ForeignKey(Books,on_delete=models.CASCADE)
    Age= models.CharField(max_length=2,null=True,blank=True)
    Place = models.CharField(max_length=100,null=True,blank=True)
    
    # class Meta:
    #     ordering = ['Name']
    
    def __str__(self):
        return self.Name

class Products(models.Model):
    Book_name = models.CharField(max_length=150,null=True,blank=True)
    Book_details = models.ForeignKey(Books,on_delete=models.CASCADE,null=True,blank=True)
    Author_details = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,blank=True)
    Stock = models.PositiveIntegerField()
    Price = models.DecimalField(max_digits=10,decimal_places=3)
    Available = models.BooleanField(default=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Published_at=models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True,blank=True)

    class Meta:
        ordering = ['Book_name']

    def __str__(self):
        return self.Book_name

class Mobile(models.Model):
    brand = models.CharField(max_length=30,null=True,blank=True)
    mobile_model = models.CharField(max_length=30,null=True,blank=True)
    price = models.CharField(max_length=10,null=True,blank=True)
    stock = models.PositiveIntegerField(null=True,blank=True)
    available = models.BooleanField(default=True,null=True,blank=True)
    
    class Meta:
        ordering = ['brand']

    # def __str__(self):
    #     return self.brand

class Category(models.Model):
    mobile = models.ForeignKey(Mobile,on_delete=models.CASCADE,null=True,blank=True)
    books = models.ForeignKey(Books,on_delete=models.CASCADE,null=True,blank=True)

class Cart(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    book = models.ForeignKey(Products,on_delete=models.CASCADE,null=True,blank=True,related_name="book")
    book_price = models.ForeignKey(Products,on_delete=models.CASCADE,null=True,blank=True)
    book_quantity = models.PositiveIntegerField(default=1)
    mobile = models.ForeignKey(Mobile,on_delete=models.CASCADE,null=True,blank=True)
    

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title



class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='profile',null=True,blank=True)
        
class BaseImage(models.Model):
    image = models.TextField(max_length=10000,null=True,blank=True)
    base_image = models.FileField(upload_to='base_64',null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    






