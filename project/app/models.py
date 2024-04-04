from django.db import models

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