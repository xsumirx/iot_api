from django.db import models

# Create your models here.

class User(models.Model):

    GENDER_CHOICE = (
        ('M','MALE'),
        ('F','FEMALE')
    )

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    about = models.TextField()
    active = models.BooleanField()
    lastActive = models.DateField()
    joinDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.name