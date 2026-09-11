from django.db import models
import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return self.name

class Meeting(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField(default=datetime.time(9, 0))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.title