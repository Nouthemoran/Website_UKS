from django.db import models

# Create your models here.
class Obat(models.Model):
    JENIS_CHOICES = [
        ('Obat Cair', 'Obat Cair'),
        ('Obat Padat', 'Obat Padat'),
        ('Obat Luar', 'Obat Luar'),
        ('-', 'none'),
      
    ]
    obatId =  models.CharField(max_length=5, primary_key=True)
    namaObat = models.CharField(max_length=255)
    fungsiObat = models.CharField(max_length=255)
    jenisObat = models.CharField(
        max_length=255,
        choices=JENIS_CHOICES, default='')
    
    
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
