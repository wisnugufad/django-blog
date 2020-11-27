from django.db import models

class article(models.Model):
  judul = models.CharField(max_length=100,null=False,blank=False)
  isi = models.TextField()
