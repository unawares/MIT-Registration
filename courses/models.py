from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Speaker(models.Model):
    image = models.ImageField(upload_to = 'media/', default = 'media/none/no-img.jpg')
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.surname, self.name)
        

class Course(models.Model):
    image = models.ImageField(upload_to = 'media/', default = 'media/none/no-img.jpg')
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
    active = models.BooleanField(default=True)
    description = models.TextField()
    speaker = models.OneToOneField(Speaker, related_name='course', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Registration(models.Model):
    course = models.ForeignKey(Course, related_name='registrations', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return '{} {}'.format(self.surname, self.name)
