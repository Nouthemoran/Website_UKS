from django.db import models

# Create your models here.
class Obat(models.Model):
    STATUS_CHOICES = [
        ('', 'Kapsul'),
      
    ]
    obatId =  models.CharField(max_length=5, primary_key=True)
    namaObat = models.CharField(max_length=255)
    fungsiObat = models.CharField(max_length=255)
    jenisObat = models.CharField
    
    
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
