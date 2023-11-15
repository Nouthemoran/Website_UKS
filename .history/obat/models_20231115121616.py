from django.db import models

# Create your models here.
class Obat(models.Model):
    ObatId =  models.CharField(max_length=5, primary_key=True)
    
    
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
