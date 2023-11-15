from django.db import models

# Create your models here.
class Obat(models.Model):
    obatId =  models.CharField(max_length=5, primary_key=True)
    namaObat = models.CharField(max_length=255)
    
    
    
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
