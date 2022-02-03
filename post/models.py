from django.db import models

# Create your models here.
class Post(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=15, blank=True, null=True)
    affiliation = models.IntegerField()
    age = models.IntegerField() 

    def __str__(self):
        """A string representation of the model."""
        return self.email
