from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
#an organistion having multiple agents who can have mulitple leads:

class User(AbstractUser):
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

class UserProfile(models.Model):
    # it doesn't get created automatically after the User is created, use signals bro
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
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
    

def post_user_created_signal(sender, instance, created, **kwargs):
     if created:
         UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)      #model that sends the event to create a userprofile after a newUser joins