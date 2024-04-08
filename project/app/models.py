from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Company(models.Model):
   name = models.CharField(max_length=20)  
   def __str__(self):
        return self.name

class Mobile(models.Model):
  Name=models.CharField(max_length=20)
  Price=models.PositiveSmallIntegerField()
  img=models.ImageField(upload_to='images/')
  Description=models.TextField()
  RAM = models.CharField(max_length=10)
  Camera=models.CharField(max_length=25)
  Display=models.CharField(max_length=10)
  OS=models.CharField(max_length=30)
  company_id=models.ForeignKey(Company,on_delete=models.CASCADE)

  def  __str__(self):
      return self.Name
  
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # items = models.ForeignKey(Cart, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE, related_name='cart_items')
    quantity=models.PositiveSmallIntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} x {self.mobile.Name} in {self.user.username}'s cart"