from django.db import models
from django import forms
# Create your models here.

class AddRoom(models.Model):
    ROOM_TYPES = (
        ('Lecture', 'Lecture'),
        ('Lab', 'Lab'),
    )

    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    port = models.CharField(max_length=100)
    detail = models.TextField()
    image = models.FileField(upload_to='upload', null=True, default=True)

    def __str__(self):
        return f"Room {self.name}"

class Booking(models.Model):
    room_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    subject = models.CharField(max_length=255)
    purpose = models.TextField()

    def __str__(self):
        return f"{self.room_name} - {self.full_name} - {self.start_datetime} - {self.end_datetime}"

