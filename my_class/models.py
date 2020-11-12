from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class Class(models.Model):
    name = models.CharField(max_length=32)
    teacher = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name+str(self.pk)

    def pin(self):
        return self.pk

    def get_absolute_url(self):
        return self.name+"-"+str(self.pk)

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    city = models.CharField(max_length=16)
    institution = models.CharField(max_length=64, blank=True)
    grade = models.CharField(max_length=2, blank=True)
    classes = models.ManyToManyField(Class, verbose_name='Классы', 
         through='ProfileClass')
    
    def __str__(self):
        return self.user.username+"_profile"+str(self.pk)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ProfileClass(models.Model):
    date_join = models.DateTimeField(auto_now_add=True) 
    current_class = models.ForeignKey(Class,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

