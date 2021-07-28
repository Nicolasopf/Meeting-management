from rest_framework import serializers
from .models import Reservation, Catering, Room
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'last_modified', 'created_at', 'capacity')

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'last_modified', 'created_at', 'room', 'user_id',
                  'starts_at', 'ends_at', 'cancelled')

class CateringSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catering
        fields = ('id', 'last_modified', 'created_at', 'reservation', 'Lunch1',
                  'Lunch2', 'BreakfastA', 'BreakfastB', 'WaterJar', 'CofeeJar')
