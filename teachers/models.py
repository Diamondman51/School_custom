import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
from django.db import models
from authentication.models import User
from multiselectfield import MultiSelectField

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


LANG_CHOICES = (
    ("1", "UZ"),
    ("2", "RU"),
    ("3", "EN"),
)


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(default=3, help_text='3')
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, help_text='1100000')
    teacher = models.ManyToManyField(Teacher, default=None, blank=True)
    read_more = models.ForeignKey('ReadMore', on_delete=models.SET_DEFAULT, default=None, null=True, blank=False)
    max_student = models.IntegerField(default=10)
    contact_number = models.CharField(max_length=100, null=True)
    langs = MultiSelectField(choices=LANG_CHOICES, null=True)
    course_photo = models.ImageField(upload_to='courses/course_photo/%Y/%m', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def f_price(self):
        return f'{self.price:,}'

    def __str__(self):
        return f'{self.name}'


class Group(models.Model):
    name = models.ForeignKey(Course, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    course_code = models.CharField(max_length=100, null=True)
    description = models.TextField()
    start_from = models.DateField(null=True)
    duration = models.IntegerField(default=3)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    read_more = models.ForeignKey('ReadMore', on_delete=models.SET_DEFAULT, default=None, null=True, blank=False)
    max_student = models.IntegerField(default=10)
    contact_number = models.CharField(max_length=100, null=True)
    lang = models.CharField(max_length=20, choices=LANG_CHOICES, null=True)
    group_photo = models.ImageField(upload_to='courses/course_photo/%Y/%m', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def f_price(self):
        return f'{self.price:,}'

    def __str__(self):
        return f'{self.name}. Language: {self.get_lang_display()}'

    def delete(self, using =None, keep_parents =False):
        if self.group_photo:
            path = self.group_photo.path
            if path:
                os.remove(path)
        return super().delete(using, keep_parents)


class ReadMore(models.Model):
    language = models.CharField(max_length=50, null=True, blank=True)
    about_course = models.TextField(blank=True, null=True)
    course_info = models.TextField(blank=True, null=True)
    course_id = models.ForeignKey(Course, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Read More"

    def __str__(self):
        return f'{self.language}'

    def get_about_course(self) -> list[str]:
        return self.about_course.split('\n')
    
    def get_course_info(self) -> list[str]:
        full = self.course_info.split('\n')
        start = full[0]
        mid = full[1:-1]
        end = full[-1]
        return start, mid, end
