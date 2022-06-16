from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Driver(models.Model):
    name = models.TextField(max_length=30)
    profile_pic = models.ImageField( upload_to='profile/', blank ='true',default='default.png')
    description = models.TextField(max_length=300)
    bio = models.TextField()
    location = models.TextField(max_length=30)
    date_joined= models.DateField(auto_now_add=True )

    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Driver.objects.create(user=instance)






