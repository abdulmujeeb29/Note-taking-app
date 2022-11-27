from django.db import models

# Create your models here.

class Note(models.Model):
    title =models.CharField(max_length =1000)
    body =models.CharField(max_length =10000000)
    date_created =models.DateTimeField()

    def __str__(self) :
        return self.title 
