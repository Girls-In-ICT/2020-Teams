from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=False, blank=False)
    address = models.TextField(max_length=200, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to='images/profile')
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class LibraryBook(models.Model):
    bookName = models.CharField(max_length=200)
    bookfile = models.FileField(upload_to='images/libraryBooks')
    bookpicture = models.FileField(upload_to='images/bookpicture', default='')


class BookComment(models.Model):
    bookId = models.ForeignKey(LibraryBook, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)


class Video(models.Model):
    title = models.CharField(max_length=50)
    video = models.FileField(upload_to='images/Videos')


class VideoComment(models.Model):
    videoId = models.ForeignKey(Video, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
