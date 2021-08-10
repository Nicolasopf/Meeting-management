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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room_id'].required = True

    class Meta:
        model = Reservation
        fields = ('id', 'user_id', 'room_id', 'starts_at', 'ends_at', 'cancelled')
        read_only_fields = ('created_at', 'last_modified')


class CateringSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catering
        fields = ('id', 'last_modified', 'created_at', 'reservation', 'Lunch1',
                  'Lunch2', 'BreakfastA', 'BreakfastB', 'WaterJar', 'CofeeJar')
