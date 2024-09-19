from django.db import models




class SoldierModel(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    
    
class BioModel(models.Model):
    firstname = models.CharField(max_length=100) 
    lastname = models.CharField(max_length=100) 
    location = models.CharField(max_length=100) 
    company = models.CharField(max_length=100) 
    favouritecar = models.CharField(max_length=100) 
    notes = models.CharField(max_length=100)    



class StudentModel(models.Model):
    firstname = models.CharField(max_length=100) 
    lastname = models.CharField(max_length=100) 
    




