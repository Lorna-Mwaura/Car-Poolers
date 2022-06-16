from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from car.models import Driver
# Create your models here.


class Profile(models.Model):
    '''
    Model for customer profile
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.user.username}Profile'
    @receiver(post_save,sender=User) 
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User) 
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()
        
        
class Rating(models.Model):
    '''
    This model will contain the ratings for diffrent categories
    '''
    experience = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.user.username} {self.project.title} Rating'