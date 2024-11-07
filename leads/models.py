from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass 


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.email}"


class Lead(models.Model):
    
    SOURCES_CHOICES = (
        ('YT', 'YOUTUBE'),
        ('Google', 'GOOGLE'),
        ('FB', 'FACEBOOK'),   
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCES_CHOICES, max_length=100)
    
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} by {self.source}"
    
