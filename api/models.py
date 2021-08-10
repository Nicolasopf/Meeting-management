from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
from uuid import uuid4


class Base(models.Model):
    ''' Base class, all tables should have the following columns '''
    last_modified = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    class Meta:
        abstract = True


class Room(Base):
    ''' Room table, the rooms should be created by an administrator.
    As there is only one floor and one building, this id is Small Integer
    It means the id can be from 0 to 32767, enough for one building rooms.
    '''
    id = models.PositiveSmallIntegerField(primary_key=True)
    capacity = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        ''' String representation of object '''
        return "Room {} Capacity {}".format(self.id, self.capacity)

class Reservation(Base):
    ''' Reservation table, must be vinculated to an user '''
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    cancelled = models.BooleanField(default=False)

    def __str__(self):
        ''' String representation of object '''
        return "{} User Reservation's, room {} ".format(self.user, self.room.id)

class Catering(Base):
    ''' Catering table, catering are additional things that the user can add
    to the reservation, as launchs, breakfasts, etc. '''
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, editable=False)
    Lunch1 = models.PositiveSmallIntegerField(default=0)
    Lunch2 = models.PositiveSmallIntegerField(default=0)
    BreakfastA = models.PositiveSmallIntegerField(default=0)
    BreakfastB = models.PositiveSmallIntegerField(default=0)
    WaterJar = models.PositiveSmallIntegerField(default=0)
    CofeeJar = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        ''' String representation of object '''
        return "{} Catering's, Lunchs {}, Breakfasts {}".format(
            self.reservation.user.username,
            self.Lunch1 + self.Lunch2,
            self.BreakfastA + self.BreakfastB)
