from django.db import models

# Create your models here.
class customer (models.Model):		
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
         
class product (models.Model):		
    pro_name = models.CharField(max_length=50)
    pro_id = models.CharField(max_length=50)
    pro_price = models.IntegerField()
    
    def __str__(self):
        return self.pro_id + " " + self.pro_name

class Contact(models.Model):
    cp_name = models.CharField(max_length=100)
    cp_phone = models.CharField(max_length=100)
    cp_email = models.CharField(max_length=100)
    cp_msg = models.CharField(max_length=100)
    
    def __str__(self):
        return self.cp_name + " " + self.cp_phone + " " + self.cp_email + " " + self.cp_msg
    
    
class proimage (models.Model):
    p_name = models.CharField(max_length=50)
    p_image = models.ImageField(upload_to= 'productimages')
    p_price = models.IntegerField()
    
    def __str__(self):
        return  self.p_name