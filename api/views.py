from rest_framework import viewsets
from .serializers import ReservationSerializer, CateringSerializer, RoomSerializer, UserSerializer
from .models import Reservation, Catering, Room
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsSameUser, ReadOnly


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('id')
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, ReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by('created_at')
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated, IsSameUser]

class CateringViewSet(viewsets.ModelViewSet):
    queryset = Catering.objects.all().order_by('created_at')
    serializer_class = CateringSerializer
    permission_classes = [IsAuthenticated, IsSameUser]
