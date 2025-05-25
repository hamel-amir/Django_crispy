from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    message = models.TextField()
    choix_contact = models.BooleanField(null=None,  default=True)

