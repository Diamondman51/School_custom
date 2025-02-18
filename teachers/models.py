from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission

from authentication.models import User

# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='teacher_profile')
    profile_image = models.ImageField(upload_to='teacher_profile/images/', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        
        self.profile_image.delete()

        return super().delete(*args, **kwargs)





@receiver(post_delete, sender=Teacher)
def delete_profile_image(sender, instance, **kwargs):
    # Check if the file exists and delete it
    if instance.profile_image and default_storage.exists(instance.profile_image.name):
        instance.profile_image.delete(save=False)
